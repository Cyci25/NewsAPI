import os

class Config:
    '''
    General configuration parent class
    '''
    # pass
    SOURCE_NEWS_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    # CATEGORIES_URL='https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'

    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}