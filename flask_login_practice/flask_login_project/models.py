from flask_login_project import db , login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):


    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text,unique=True,index=True)
    email = db.Column(db.Text,unique=True,index=True)
    password = db.Column(db.Text)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        
    def check_password(self,password):
        return check_password_hash(self.password,password)