from flask import Flask , redirect , render_template , url_for, request, session, flash, abort
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/ticketoneway" , methods = ["GET", "POST"])
def ticket1():
    return render_template("oneway.html")


@app.route("/fedback")
def feedback():
    return render_template('feedback.html')

@app.route("/bugreport")
def bugreport():
    return render_template('bugreport.html')

@app.route("/")
def demo():
    return render_template('demo.html')


@app.route("/index1")
def index1():
    return render_template('index1.html')

@app.route("/widget")
def widget():
    return render_template('widget.html')


@app.route("/assistance", methods=["GET"])
def assistance():
    return render_template("assistance.html")

@app.route("/assistance/specialassistance")
def special():
    return render_template("specialassist.html")

@app.route("/disabledassistance")
def disable():
    return render_template("disabledassist.html")

app.run(debug=True)