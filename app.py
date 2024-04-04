from flask import Flask

app = Flask('Hello')

@app.route('/')
def ola():
    return 'Hello World'