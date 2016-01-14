#!/usr/bin/env python
# coding=utf-8

from flask import session, render_template

from webapp import app



@app.route('/rdms/index', methods=['GET','POST'])
@app.route('/rdms/home', methods=['GET','POST'])
def index():
    return 'Hello Flask!'


@app.route('/rdms/test')
def test():
    return 'test'
