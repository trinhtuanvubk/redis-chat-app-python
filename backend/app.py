import os
import sys

from flask import Flask
from flask_cors import CORS
from flask_session import Session
from flask_socketio import SocketIO

from .config import get_config

sess = Session()
app = Flask(__name__, static_url_path="", static_folder="../frontend/build/")
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

def run():
    pass