from flask import Flask
from service import *

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, World!"

@app.route("/genres")
def genres():
    # print(getGenres())
    return "genres"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)