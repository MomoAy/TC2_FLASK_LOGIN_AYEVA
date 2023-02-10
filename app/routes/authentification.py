from flask import Flask,render_template,request,redirect,url_for, flash
from app.models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required
db = SQLAlchemy()

def login():
    if request.method == 'GET':
        return render_template('authentification/login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        user = Users.query.filter_by(username=username).first()


        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('profil'))

def signup():
    if request.method == 'GET':
        return render_template('authentification/register.html')
    else:
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists')
            return redirect(url_for('signup'))
        
        new_user = Users(username = username, email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

def logout():
    logout_user()
    return redirect(url_for('index'))