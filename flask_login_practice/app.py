from flask_login_project import app, db
from flask import Flask, render_template, url_for, redirect, flash, request
from flask_login_project.forms import RegistrationForm, LoginForm
from flask_login_project.models import User
from flask_login import login_required, login_user, logout_user


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out of your account!')
    return redirect(url_for('home'))

@app.route('/login',methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Logged in successfully')

            next = request.args.get('next')

            if next == None or not next.startswith('/'):
                return redirect(url_for('welcome'))
            
            return redirect(next)

    return render_template('login.html',form=form)



@app.route('/register',methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        username = form.username.data
        email = form.email.data
        password = form.password.data

        new_user = User(username=username,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Thanks for the registraion!')

        return redirect(url_for('login'))
    
    return render_template('register.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)