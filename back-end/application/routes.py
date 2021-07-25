from flask import request, render_template, url_for, redirect
from application import db, app
from os import uname
from datetime import datetime
# import models
# import forms

# db.create_all()

# test page
@app.route("/", methods=["Get"])
def home():
    return render_template('index.html', host=uname().nodename, time=datetime.now())
