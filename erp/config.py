import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(os.path.join('.env'))
WHERE = os.environ.get('WHERE')


class db:
    user = os.environ.get('db_user')
    name = os.environ.get('db_name')
    host = os.environ.get('db_host')
    password = os.environ.get('db_password')
    
