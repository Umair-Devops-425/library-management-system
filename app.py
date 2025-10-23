import os
from flask import Flask, g, escape, session, redirect, render_template, request, jsonify, Response
from Misc.functions import *
from flaskext.mysql import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_DATABASE_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('DB_NAME')
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_DATABASE_PORT'] = int(os.environ.get('DB_PORT', 3306))

mysql = MySQL(app)


app = Flask(__name__)
app.secret_key = '#$ab9&^BB00_.'

# Setting DAO Class
from Models.DAO import DAO

DAO = DAO(app)

# Registering blueprints
from routes.user import user_view
from routes.book import book_view
from routes.admin import admin_view

# Registering custom functions to be used within templates
app.jinja_env.globals.update(
    ago=ago,
    str=str,
)

app.register_blueprint(user_view)
app.register_blueprint(book_view)
app.register_blueprint(admin_view)