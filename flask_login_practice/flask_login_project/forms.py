
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_login_project.models import User



class RegistrationForm(FlaskForm):

    username = StringField('Username',validators=[DataRequired(),Length(min=8,max=16)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8,max=16),EqualTo('confirm_password',message='Password must match!')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self,email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email is already registered')

    def validate_username(self,username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username is already taken!')


class LoginForm(FlaskForm):

    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')
