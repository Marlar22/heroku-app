from flask import Flask

myapp = flask(__Flask__)

@myapp.route("/")
def hello():
    return "Hello from Heroku test"

