import os
from dotenv import load_dotenv
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
WHERE = os.environ.get('WHERE')
print(WHERE)
print(basedir)

class db:
    user = os.environ.get('db_user')
    name = os.environ.get('db_name')
    host = os.environ.get('db_host')
    password = os.environ.get('db_password')
    
