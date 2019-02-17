from flask import Flask, render_template
import os

app = Flask(__name__)
# app.config["UPLOAD_FOLDER"] = os.path.join('app', 'resources')
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
from app import routes