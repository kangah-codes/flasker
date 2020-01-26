import os
import time
import click
import sys
from colorama import init
from termcolor import cprint
init(strip=not sys.stdout.isatty())
from pyfiglet import figlet_format


# main code
@click.command()
@click.option('--template', default=True, help="Create a template directory or not")
@click.option('--static', default=True, help='Create a static directory or not')
@click.option('--add',  default=True, help='Write basic programs')
def main(template, static, add):
	"""flasker - Simple CLI tool to create flask project structures"""
	cprint(figlet_format('flasker'), 'green')
	if template:
		if static:
			#click.echo(f"Create the project in current directory? {os.getcwd()} (Y/N)")
			choice = input(f"Create the project in current directory? {os.getcwd()} (Y/N)")
			if choice.lower() == 'y':
				name = input("Enter a project name: ")
				cprint(f"Creating project in {os.getcwd()}...", 'green')
				time.sleep(1)
				try:
					os.mkdir(f"{os.getcwd()}/{name}")
					os.mkdir(f"{os.getcwd()}/{name}/static")
					os.mkdir(f"{os.getcwd()}/{name}/templates")
					#os.mkdir(f"{os.getcwd()}/{name}/project")
					with open(f"{os.getcwd()}/{name}/app.py", 'w') as app:
						app.write("""from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n\treturn "Hello World"\n\nif __name__ == '__main__':\n\tapp.run(debug=True)""")
						app.close()
				except OSError as e:
					cprint(f"Creation of folder failed\nError {e}", "red")
				except Exception as e:
					cprint(f"Error {e}", 'red')
				else:
					cprint("Created project successfully", "green")
			else:
				dir_input = input("Enter absolute path to directory: ")
				if os.path.isdir(dir_input):
					cprint(f"Creating project in {dir_input}...", 'green')
				time.sleep(1)
				try:
					os.mkdir(dir_input+'/'+name)
					os.mkdir(dir_input+'/'+name+'/'+'static')
					os.mkdir(dir_input+'/'+name+'/'+'templates')

					with open(f"{dir_input}/name/app.py", 'w') as app:
						app.write("""from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n\treturn "Hello World"\n\nif __name__ == '__main__':\n\tapp.run(debug=True)""")
						app.close()
						
				except OSError as e:
					cprint(f"Creation of folder failed\nError {e}", "red")
				else:
					cprint("Created project successfully", "green")

				

if __name__ == '__main__':
	main()
