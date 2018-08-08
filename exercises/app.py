from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/<string:name>')
def display_student(name):
	return render_template("student.html", name=name)
	pass

app.run(debug=True)
