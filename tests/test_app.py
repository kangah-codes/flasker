from flasker.app.main import *
import pytest
import os

# will only work on Linux
test_directory = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
project_name = 'testProject'

def testCreateProject():	
	assert createProject(test_directory, project_name) == f"{os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')}/{project_name}"

def testCreateConfig():
	assert createConfig(test_directory, project_name) == f"{os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')}/{project_name}/config.py"

def testCreateEnv():
	assert createEnv(test_directory, project_name) == f"{os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')}/{project_name}/env"