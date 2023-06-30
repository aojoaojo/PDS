#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

   
@app.route("/")
def index():
    return render_template('home.html')

@app.route("/segunda")
def segunda():
    return render_template('segunda.html')

if __name__ == '__main__':
    app.run(debug = True)