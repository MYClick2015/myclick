
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/python')
def python_page():
    return render_template('python.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
