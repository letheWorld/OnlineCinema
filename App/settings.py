import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_db_uri(dbinfo):

    engine = dbinfo.get('ENGINE') or 'sqlite'
    driver = dbinfo.get('DRIVER') or 'sqlite'
    user = dbinfo.get('USER') or ''
    password = dbinfo.get('PASSWORD') or ''
    host = dbinfo.get('HOST') or ''
    port = dbinfo.get('PORT') or ''
    name = dbinfo.get('NAME') or ''

    return '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, user, password, host, port, name)

class Config():

    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'wang'

    DEBUG_TB_INTERCEPT_REDIRECTS = False

class DevelopConfig(Config):

    DEBUG = True

    dbinfo = {

        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'MySQL用户名',
        'PASSWORD': 'MySQL密码',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'OnlineCinema',

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestConfig(Config):
    TESTING = False

    dbinfo = {

        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'MySQL用户名',
        'PASSWORD': 'MySQL密码',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'OnlineCinema',

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):

    dbinfo = {

        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'MySQL用户名',
        'PASSWORD': 'MySQL密码',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'OnlineCinema',

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):

    dbinfo = {

        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'MySQL用户名',
        'PASSWORD': 'MySQL密码',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'OnlineCinema',

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    'develop': DevelopConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig,
}

ADMINS = ('wang', 'zhang', 'zhao', 'lethe')

FILE_PATH_PREFIX = '/static/uploads/icons'

UPLOADS_DIR = os.path.join(BASE_DIR, 'App/static/uploads/icons')
