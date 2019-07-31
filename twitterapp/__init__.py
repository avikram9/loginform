from flask import Flask 
import os
from flask_login import LoginManager

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')

login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS "] = False

app.config['SECRET_KEY'] = "you will never guess"



