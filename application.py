#----------------Libraries---------------------#
import os
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from connectionString import dbConnectStringMySql

#-------------------APP------------------------#

app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = dbConnectStringMySql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   

db = SQLAlchemy(app)

basedir = os.path.dirname((os.path.abspath(__file__)))
app.config['UPLOAD_FOLDER'] = basedir+"/static/img"


#------------------Classes----------------------#

class cadastroEquipe(db.Model): 
    __tablename__='equipe'
    id     = db.Column( db.Integer, primary_key=True, autoincrement = True )
    nome   = db.Column( db.String(50) )
    numero = db.Column( db.String(2) )

    
    def __init__(self, nome, numero):
        self.nome     = nome
        self.numero = numero
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

@app.route('/cadastro', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        nome     =  ( request.form.get("nome") )
        numero   =  ( request.form.get("numero"))

        if nome:
            tempForm = cadastroEquipe( nome, numero )
            db.session.add( tempForm )
            db.session.commit()
        
        return redirect(url_for('cadastro'))

if __name__ == "__main__":
    port = int( os.environ.get("PORT", 5000) )
    app.run( host='0.0.0.0', port = port )
    
#--------------LocalHost-run----------------#
# if __name__ == "__main__":
#     app.run( debug = True )
#---------------------------------------------#
