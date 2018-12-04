class Config(object):
    TESTING = False


class DevelopmentConfig(Config):
    TESTING = True


class TestingConfig(Config):
    TESTING = True
