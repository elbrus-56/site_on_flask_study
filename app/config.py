

class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SECRET_KEY = "qwerty qwerty"
    SECURITY_PASSWORD_SALT = 'qwerty'
    SECURITY_PASSWORD_HASH = 'bcrypt'

