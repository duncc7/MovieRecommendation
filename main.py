from flask import Flask
from flask import render_template, url_for
from service import *

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/movie")
def movie():
    return render_template("movie.html")

@app.route("/tv")
def tv():
    return render_template("tv.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)