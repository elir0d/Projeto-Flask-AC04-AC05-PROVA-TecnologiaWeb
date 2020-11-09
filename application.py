#----------------Libraries---------------------#

import os
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from connectionString import dbConnectString
#-------------------APP------------------------#

app = Flask (__name__)


#------------------Routes----------------------#
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/competidores')
def competidores():
    return render_template("competidores.html")
@app.route('/campeonato')
def campeonato():
    return render_template("campeonato.html")

@app.route('/vitorias')
def vitorias():
    return render_template("vitorias.html")

@app.route('/circuitos')
def circuitos():
    return render_template("circuitos.html")

@app.route( "/cadastro" )
def cadastro():
    return render_template("cadastro.html")
    
# if __name__ == "__main__":
#     port = int( os.environ.get("PORT", 5000) )
#     app.run( host='0.0.0.0', port = port )
    
#--------------Development-run----------------#
if __name__ == '__main__':
    app.run('localhost', 5555)
#---------------------------------------------#
