import os
from flask import Flask
from flask import render_template

app = Flask (__name__)
    
@app.route('/')
def home():
    return render_template("home.html")

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
    
# if __name__ == "__main__":
#     port = int( os.environ.get("PORT", 5000) )
#     app.run( host='0.0.0.0', port = port )

if __name__ == '__main__':
    app.run('localhost', 5555)