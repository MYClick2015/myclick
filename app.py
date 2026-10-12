from flask import Flask, render_template, request

app = Flask(__name__)

MAINTENANCE_MODE = True  # Skift til False når du vil vise den rigtige side

@app.before_request
def check_maintenance():
    if MAINTENANCE_MODE and request.path != '/admin':
        return render_template('maintenance.html')

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
