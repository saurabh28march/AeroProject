from flask import Flask , redirect , render_template , url_for, request, session, flash, abort
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/ticketoneway" , methods = ["GET", "POST"])
def ticket1():
    return render_template("oneway.html")


@app.route("/fedback")
def feedback():
    return render_template('feedback.html')

app.run(debug=True)