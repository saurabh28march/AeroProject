from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/ticketoneway" , methods = ["GET", "POST"])
def ticket1():
    return render_template("oneway.html")

app.run(debug=True)