import sqlite3
from flask import redirect, url_for, render_template
from ..common.utils import autenticado
from .. import app

@app.errorhandler(sqlite3.Error)
def db_error(error):
    print(error)
    return render_template("500.html",
                           autenticado=autenticado()) , 500

@app.route('/500')
def server_error():
    return render_template("500.html",
                           autenticado=autenticado()) , 500
