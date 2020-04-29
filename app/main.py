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
@click.option('--test', default=True, help="Create a test dir for your project")
@click.option('--add',  default=True, help='Write basic programs')
@click.option('--config',  default=True, help='Create a config file')
@click.option('--mkenv', default=True, help='Create a virtual env for the project')
def main(test, add, config, mkenv):
	"""flasker - Simple CLI tool to create flask project structures"""
	cprint(figlet_format('flasker'), 'green')

	choice = input(f"Create the project in the current directory? : {os.getcwd()} (Y/N)")
	if choice.lower() == 'y' or choice == '':
		project_name = input("Enter a project name: ")
		cprint(f"Creating a project in {os.getcwd()}...", "green")
		time.sleep(1)
		try:
			os.mkdir(f"{os.getcwd()}/{project_name}")
			os.mkdir(f"{os.getcwd()}/{project_name}/app")
			os.mkdir(f"{os.getcwd()}/{project_name}/app/test")
			os.mkdir(f"{os.getcwd()}/{project_name}/app/static")
			os.mkdir(f"{os.getcwd()}/{project_name}/app/{project_name}")
			os.mkdir(f"{os.getcwd()}/{project_name}/app/templates")
			with open(f"{os.getcwd()}/{project_name}/app/{project_name}/models.py", 'w') as models:
				models.write("""# your models go here""")
				models.close()
			with open(f"{os.getcwd()}/{project_name}/app/{project_name}/controllers.py", 'w') as controllers:
				controllers.write(f"""# your app controllers\nfrom flask import Blueprint, request, render_template, flash, g, session, redirect, url_for\nfrom flask_login import LoginManager, current_user, login_user, logout_user, login_required\nfrom app.module.models import *\n\ncontroller = Blueprint('{project_name}', __name__)\n\n@controller.route('/')\ndef index():\n\treturn "HELLO""""")
				controllers.close()
			with open(f"{os.getcwd()}/{project_name}/app/{project_name}/__init__.py", 'w') as init:
				init.close()
			with open(f"{os.getcwd()}/{project_name}/app/test/test_config.py", "w") as write:
				write.write("# your testing configs")
				write.close()
			with open(f"{os.getcwd()}/{project_name}/main.py", 'w') as main_file:
				main_file.write("""from app import app\nif __name__ == "__main__":\n\tapp.run()""")
				main_file.close()
			with open(f"{os.getcwd()}/{project_name}/requirements.txt", 'w') as requirements:
				requirements.write("""Flask==1.1.1\nFlask-Bcrypt==0.7.1\nFlask-Login==0.5.0\nFlask-Migrate==2.5.2\nflask-restplus==0.13.0\nFlask-Script==2.0.6\nFlask-Session==0.3.1\nFlask-SQLAlchemy==2.4.1\nFlask-Testing==0.7.1""")
				requirements.close()

		except OSError as e:
			cprint(f"Creation of folder failed\nError: {e}", "red")
			sys.exit()
		except Exception as e:
			cprint(f"Error: {e}", 'red')
			sys.exit()
		else:
			cprint("Created project successfully", "green")
	
		if config:
			cprint("Creating config file", 'green')
			try:
				with open(f"{os.getcwd()}/{project_name}/config.py", 'w') as config:
					config.write("# your configs go here")
					config.close()
			except OSError as e:
				cprint(f"Creation of config failed\nError: {e}", "red")
				sys.exit()
			except Exception as e:
				cprint(f"Error: {e}", 'red')
				sys.exit()
			else:
				cprint("Created config file successfully", "green")

		if mkenv:
			try:
				if sys.version[0] == '3':
					os.system("python3 -m venv env")
				else:
					os.system("python2 -m venv env")
			except:
				cprint("Making virtual environment failed", 'red')
				sys.exit()

	else:
		project_name = input("Enter a project name: ")
		directory = input("Enter absolute path to directory: ")
		cprint(f"Creating a project in {directory}...", "green")
		time.sleep(1)
		try:
			os.mkdir(f"{directory}/{project_name}")
			os.mkdir(f"{directory}/{project_name}/app")
			os.mkdir(f"{directory}/{project_name}/app/test")
			os.mkdir(f"{directory}/{project_name}/app/static")
			os.mkdir(f"{directory}/{project_name}/app/{project_name}")
			os.mkdir(f"{directory}/{project_name}/app/templates")
			with open(f"{directory}/{project_name}/app/{project_name}/models.py", 'w') as models:
				models.write("""# your models go here""")
				models.close()
			with open(f"{directory}/{project_name}/app/{project_name}/controllers.py", 'w') as controllers:
				controllers.write(f"""# your app controllers\nfrom flask import Blueprint, request, render_template, flash, g, session, redirect, url_for\nfrom flask_login import LoginManager, current_user, login_user, logout_user, login_required\nfrom app.module.models import *\n\ncontroller = Blueprint('{project_name}', __name__)\n\n@controller.route('/')\ndef index():\n\treturn "HELLO""""")
				controllers.close()
			with open(f"{directory}/{project_name}/app/{project_name}/__init__.py", 'w') as init:
				init.close()
			with open(f"{directory}/{project_name}/app/test/test_config.py", "w") as write:
				write.write("# your testing configs")
				write.close()
			with open(f"{directory}/{project_name}/main.py", 'w') as main_file:
				main_file.write("""from app import app\nif __name__ == "__main__":\n\tapp.run()""")
				main_file.close()
			with open(f"{directory}/{project_name}/requirements.txt", 'w') as requirements:
				requirements.write("""Flask==1.1.1\nFlask-Bcrypt==0.7.1\nFlask-Login==0.5.0\nFlask-Migrate==2.5.2\nflask-restplus==0.13.0\nFlask-Script==2.0.6\nFlask-Session==0.3.1\nFlask-SQLAlchemy==2.4.1\nFlask-Testing==0.7.1""")
				requirements.close()

		except OSError as e:
			cprint(f"Creation of folder failed\nError: {e}", "red")
			sys.exit()
		except Exception as e:
			cprint(f"Error: {e}", 'red')
			sys.exit()
		else:
			cprint("Created project successfully", "green")
	
		if config:
			cprint("Creating config file", 'green')
			try:
				with open(f"{directory}/{project_name}/config.py", 'w') as config:
					config.write("# your configs go here")
					config.close()
			except OSError as e:
				cprint(f"Creation of config failed\nError: {e}", "red")
				sys.exit()
			except Exception as e:
				cprint(f"Error: {e}", 'red')
				sys.exit()
			else:
				cprint("Created config file successfully", "green")

		if mkenv:
			try:
				if sys.version[0] == '3':
					os.system("python3 -m venv env")
				else:
					os.system("python2 -m venv env")
			except:
				cprint("Making virtual environment failed", 'red')
				sys.exit()

				

if __name__ == '__main__':
	main()
