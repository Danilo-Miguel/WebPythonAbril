from flask import Flask

app = Flask("Ola")

@app.route('/')
def ola():
    return "Olá mundo"