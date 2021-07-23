from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQL_URI")
app.config["SECRET_KEY"] = "my_key"
app.config["SQL_ALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from application import routes
