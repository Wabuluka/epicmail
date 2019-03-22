# epicmail/tests/base.py

from flask_testing import TestCase

from epicmail.app import app


class BaseTest(TestCase):
    """Base setup for testing the API"""

    def create_app(self):
        app.config.from_object('epicmail.app.config.TestingConfiguration')
        return app