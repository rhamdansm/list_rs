from flask import Flask, render_template, request

import lokasi , model

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():

    return render_template ("index.html", tempat = lokasi.tempat)

@app.route('/result', methods = ["POST"])
def result():
    if request.method == 'POST':
        kota = request.form["kota"] if request.form["kota"]!="" else 0
        kec = request.form["kec"] if request.form["kec"]!="" else 0
        kel = request.form["kel"] if request.form["kel"]!="" else 0

        pred = model.model(kel,kec)

    return render_template ("list.html",test=pred)
