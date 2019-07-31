from flask_sqlalchemy import SQLAlchemy
from twitterapp import app
from werkzeug.security import generate_password_hash, check_password_hash

#Flask-Login Imports
from flask_login import UserMixin
from twitterapp import login_manager 

db = SQLAlchemy(app)    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False) 
    post = db.relationship('Post', backref= "author", lazy= True)



    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def __repr__(self):
        return "{} has been created".format(self.username)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(290))
    date_created = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    def __repr__(self):
        return "The Title is {} and the user is {}".format(self.title, self.user_id)

