import numpy as np
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
from waterer import Watererer

@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    water = Watererer
    water.main_loop()
