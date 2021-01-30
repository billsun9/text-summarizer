import os
from flask import render_template, Flask, request

#from werkzeug.utils import secure_filename
from extractive_summarizer import generate_summary

ALLOWED_EXTENSIONS = {'pdf','txt'}

app = Flask(__name__)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/') # home page
def index():
    return render_template('index.html')

@app.route("/results", methods=["POST"]) # shows results of ML prediction and further info
def results():
    form = request.form
    if request.method == "POST":
        text_input = request.form['text-input']
        prediction = generate_summary(text_input,3)
        return render_template("results.html", message = prediction)


if __name__ == '__main__':
    app.run(debug=False)