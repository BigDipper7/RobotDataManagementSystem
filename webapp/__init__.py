#!/usr/bin/env python
# coding=utf-8

from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fuck u, you can not guess it'



# seems circular import
import webapp.view.views