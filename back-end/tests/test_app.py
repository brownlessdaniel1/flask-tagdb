from flask import url_for
from flask_testing import TestCase
from application import app, db
# import models

class TestBase(TestCase):
    def create_app(self):
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

    def testCreateObjGet(self):
        self.assert200(self.client.get(url_for('createObj')))

    def testCreateTagGet(self):
        self.assert200(self.client.get(url_for('createTag')))

    def testReadAllGet(self):
        self.assert200(self.client.get(url_for('readAll')))
    
    # more reads?
    def testRenameObjGet(self):
        self.assert200(self.client.get(url_for('renameObj')))
    
    def testUpdateTagGet(self):
        self.assert200(self.client.get(url_for('updateTag')))
    # Delete
    def testRemoveObjGet(self):
        self.assert200(self.client.get(url_for('remobeObj')))

    def testRemoveObjGet(self):
        self.assert200(self.client.get(url_for('removeTag')))
