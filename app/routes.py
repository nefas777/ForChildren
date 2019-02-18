# -*- coding: utf-8 -*-
from app import app
from flask import render_template, Response, stream_with_context , request
import os
import time
import shutil
@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/img', methods=['GET', 'POST'])
def show_img():
    if request.method == 'GET':
        return render_template("show_img.html")
    if request.method == 'POST':
        scr = r'C:\Users\Nefedov Alex\Desktop\ForCh\ForChildren\fake\camel.jpg'
        dst = r'C:\Users\Nefedov Alex\Desktop\ForCh\ForChildren\app\static\0.jpg'
        time.sleep(3)
        shutil.copy(scr, dst)
        
        return render_template("show_fake.html")

