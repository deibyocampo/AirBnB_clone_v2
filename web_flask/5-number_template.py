#!/usr/bin/python3
"""
starts a flask web aplication
"""
from flask import Flask
from flask import render_template


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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def magic(text='is cool'):
    return ("Python {}".format(text).replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
        return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
