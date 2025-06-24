from flask import render_template, url_for #type:ignore
from fakepinterest import app

@app.route('/')
def homepage():
    return render_template('homepage.html')

