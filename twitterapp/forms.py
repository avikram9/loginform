from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import input_required, EqualTo,Email
from flask_wtf import FlaskForm 



class SignUpForm(FlaskForm):
    username = StringField("username", validators = [input_required()]) 
    email = StringField("Email", validators = [input_required(), Email()])
    password = PasswordField("password", validators = [input_required()])
    confirm_pass = PasswordField("Confirm Password", validators = [input_required(), EqualTo('password')])
    submit = SubmitField()


class LoginForm(FlaskForm):
    email = StringField("Email", validators = [input_required(), Email()])
    password = PasswordField("password", validators = [input_required()])
    submit = SubmitField()

class PostForm(FlaskForm):
    title = StringField("Title", validators = [input_required()])
    content = StringField("Content", validators = [input_required()])
    submit = SubmitField()