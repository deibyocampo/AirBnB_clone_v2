#!/usr/bin/python3
"""
starts a flask web aplication
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cool(text):
    return ("C {}".format(text).replace("_", " "))


if __name__ == '__main__':
    app.run()
