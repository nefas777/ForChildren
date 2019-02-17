# -*- coding: utf-8 -*-
from app import app
from flask import render_template, Response, stream_with_context
import os
import time

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return "Hello, World!"


@app.route('/img')
def show_img():
    return render_template("show_img.html")


