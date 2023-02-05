from flask import Flask
from firebase_admin import credentials, initialize_app

cred = credentials.Certificate('api/key.json')
default_app = initialize_app(cred)

def create_app():
    app=Flask(__name__,static_folder='client/build')
    app.config['SECRET_KEY'] = '12345rtfescdvf'
    return app