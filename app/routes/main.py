from flask import Flask,render_template,request,redirect,url_for
from flask_login import login_required, current_user

def index():
    return render_template('main/index.html')

def profil():
    return render_template('main/profile.html', name = current_user.username)

# def charge():
