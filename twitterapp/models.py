from flask_sqlalchemy import SQLAlchemy
from twitterapp import app
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy(app)    

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False) 

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def __repr__(self):
        return "{} has been created".format(self.username)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash


