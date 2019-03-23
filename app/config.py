# epicmail/app/config.py
import os
from app import app

class BaseConfiguration:
    """Base Configuration for the API."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'just anything secret')
    DEBUG = False


class DevelopmentConfiguration(BaseConfiguration):
    """Development Configuration"""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    DATABASE_URI = os.getenv("DATABASE_URL" + "challengethree") 


class TestingConfiguration(BaseConfiguration):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    DATABASE_URI = os.getenv("DATABASE_URL" + "challengethree_test")

class ProductionConfiguration(BaseConfiguration):
    """Production configuration."""
    SECRET_KEY = 'just anything secret'
    DEBUG = False
    DATABASE_URI = 'postgresql:///'