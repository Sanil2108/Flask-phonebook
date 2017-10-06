from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    name=StringField('Name', validators=[DataRequired("Enter name")])
    email=StringField('Email address', validators=[DataRequired("Enter a email address"), Email("Enter your email")])
    phone=StringField('Phone number', validators=[DataRequired("Enter a phone number"), Length(min=8, message="Enter a valid phone number")])
    submit=SubmitField('Sign Up')