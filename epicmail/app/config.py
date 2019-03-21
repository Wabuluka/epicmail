# epicmail/app/config.py

import os
postgres_local_base = 'postgresql://postgres:root123@localhost/'
database_name = 'challengethree'

class BaseConfiguration:
    """Base Configuration for the API."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'just anything secret')
    DEBUG = False


class DevelopmentConfiguration(BaseConfiguration):
    """Development Configuration"""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    DATABASE_URI = postgres_local_base + database_name


class TestingConfiguration(BaseConfiguration):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    DATABASE_URI = postgres_local_base + database_name + '_test'

class ProductionConfiguration(BaseConfiguration):
    """Production configuration."""
    SECRET_KEY = 'just anything secret'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///'