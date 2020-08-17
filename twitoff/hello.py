#!/usr/bin/env python

"""
Example of a very basic web application
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'