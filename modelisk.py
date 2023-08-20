from flask import Flask, url_for, render_template


app = Flask("modelisk")

@app.route("/")
def index():
    return 'Index Page'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/reference-data')
def reference_data():
    return 'not implemented'

@app.route('/business-data')
def business_data():
    return 'not implemented'

