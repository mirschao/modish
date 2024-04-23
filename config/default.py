


class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URL = 'mysql://username:password@localhost/dbname'
    SECRET_KEY = '90d5092e335f04dc8018386fe5369287'


class TestingConfig(Config):
    DATABASE_URL = 'mysql://modish:Abc123!!@localhost/modish'
