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
					os.mkdir(os.getcwd()+'/'+name)
					os.mkdir(os.getcwd()+'/'+name+'/'+'static')
					os.mkdir(os.getcwd()+'/'+name+'/'+'templates')
					os.mkdir(os.getcwd()+'/'+name+'/'+'project')
				except OSError as e:
					cprint(f"Creation of folder failed\nError {e}", "red")
				else:
					cprint("Created project successfully", "green")
			else:
				dir = input("Enter absolute path to directory: ")
				

if __name__ == '__main__':
	main()
