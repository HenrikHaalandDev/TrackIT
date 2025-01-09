from flask import Flask, render_template, url_for, request, redirect
import os


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        login_content = request.form['content']
    else:
        return render_template('home.html') 