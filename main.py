
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("indexx.html")

@app.route("/about")
def about():
    return render_template("/Fejkbuk/FejkBuk.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run(use_reloader=True)

