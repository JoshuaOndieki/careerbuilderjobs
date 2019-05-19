"""
    Web scraper configurations
"""

import os


class Config:
    """
    Scraper configuration base class
    """
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(Config):
    """
        Scraper configuration for development
        Using SqliteDB
    """
    DATABASE_NAME = 'careerbuilderjobs'


class ProductionConfig(Config):
    """
        Scraper configuration for production
    """
    pass


config = {'development': DevelopmentConfig,
          'production': ProductionConfig}
