#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fuck u, you can not guess it'
    Bootstrap(app)

    return app


app = create_app()



# seems circular import
import webapp.view.views
