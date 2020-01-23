#!/usr/bin/python3
"""
starts a flask web aplication
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return ('Hello HBNB!')


if __name__ == '__main__':
    app.run()
