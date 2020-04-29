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
	

				

if __name__ == '__main__':
	main()
