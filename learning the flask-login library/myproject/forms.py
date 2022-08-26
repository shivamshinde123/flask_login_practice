from flask_wtf import FlaskForm
from  wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from myproject.models import User


class RegistrationForm(FlaskForm):


    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('confirm',message='Passwords must match!')])
    confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self,email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email is already registerd')


    def validate_username(self,username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username is already taken!')


class LoginForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    password = StringField('password',validators=[DataRequired()])
    submit = SubmitField('Login')