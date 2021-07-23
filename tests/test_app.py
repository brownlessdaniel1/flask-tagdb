from flask import url_for
from flask_testing import TestCase
from application import app, db
# import models

class TestBase(TestCase):
    def createApp(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY="Testing",
            DEBUG=True,
            WTF_CSRF_ENABLED=False,
            SQL_ALCHEMY_TRACK_MODIFICATIONS=False
        )
        return app
    def setUp(self):
        db.create_all()
        ## initiate some test models & commit to db.
        db.session.commit()
    
    def tearDown(self):
        db.drop_all()

class TestRender(TestBase):
    def testHomeGet(self):
        self.assert200(self.client.get(url_for('home')))

