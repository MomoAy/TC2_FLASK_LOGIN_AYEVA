from urllib.parse import quote_plus
#importation de flask
from flask import Flask,render_template,request,redirect,url_for

#importation de flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from app.routes.authentification import *
from app.routes.main import *

#creation de l'intance de la BD
db = SQLAlchemy()

from flask_login import LoginManager
from flask_login import login_user, logout_user, login_required


def create_app():
    #Demarrage de l'apk
    app = Flask(__name__)
    app.secret_key = "some_secret_key"

    #Chaîne de connexion à la base de donnée
    password = quote_plus('1994')
    chaine = "postgresql://postgres:{}@localhost:5432/gestperson".format(password)
    app.config["SQLALCHEMY_DATABASE_URI"] = chaine

    #masquer les notifications
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.route('/login', methods=['GET', 'POST'])(login)
    app.route('/signup', methods=['GET', 'POST'])(signup)
    app.route('/logout')(logout)
    app.route('/', methods=['GET', 'POST'])(index)
    app.route('/profil', methods=['GET', 'POST'])(login_required(profil))
    
    login_manager = LoginManager()
    login_manager.login_view = 'routes.login'
    login_manager.init_app(app)

    from .models import Users

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Users.query.get(int(user_id))

    return app


