from flask import Flask, render_template, g
import sqlite3

app = Flask("Ola")

DATABASE  = "banco.bd"
SECRET_KEY = "1234"

app.config.from_object(__name__)

def conectar():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.bd = conectar()

@app.teardown_request    
def teardown_request(f):
    g.bd.close()    

@app.route('/')
def exibir_posts():
    
    sql = "SELECT titulo, texto, data_criacao FROM posts ORDER BY id DESC"
    resultado  = g.bd.execute(sql)
    
    posts = [
        {"titulo": "Memórias Póstumas de Brás Cubas", "texto":"Fui descalçar as botas, que estavam apertadas.", "data_criacao": "1881"},
        {"titulo": "Auto da Compadecida", "texto": "Matar Padre dá um azar danado", "data_criacao":"1955"}
            ]
    return render_template("ola.html", post=posts)



