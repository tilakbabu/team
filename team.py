from flask import Flask, render_template, request, make_response
import random
import os
import csv

from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
@app.route('/PythonTeamAPSSDC')
def handle_data():
    csvpath = "Untitled form (Responses) - Form Responses 1.csv"
    with open(csvpath, newline='') as csvfile:
        trainers = csv.reader(csvfile, delimiter=',', quotechar='|')
        # REPLACE
        # https://drive.google.com/open?
        # https://drive.google.com/uc?export=download&
        return render_template("index.html",trainers = trainers)


if __name__ == '__main__':
    app.run(debug=True)
