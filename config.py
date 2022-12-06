##Open API
OPENAI_API_KEY = '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'



## Flask
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
