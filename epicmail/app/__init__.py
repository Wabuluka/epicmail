# epicmail/app/__init__.py

import os

from flask import Flask

app = Flask(__name__)

app_settings = os.getenv(
    'APP_SETTINGS',
    'epicmail.app.config.DevelopmentConfiguration'
)

app.config.from_object(app_settings)