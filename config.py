import os
basedir = os.path.abspath(os.path.dirname(__file__))

username = 'team_60'
password = 'natesh'
url = 'nicolasviana.chhlcoydquoi.us-east-2.rds.amazonaws.com'
port = 5432
database = 'minjusticia'

connection_string = f'{username}:{password}@{url}:{port}/{database}'

class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://' + connection_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.environ['SECRET_KEY']