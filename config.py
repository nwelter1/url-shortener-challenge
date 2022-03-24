import os
basedir = os.path.dirname(__file__)

class Config:
    SECRET_KEY = 'you will never guess!'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URI') or os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False