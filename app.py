from flask import Flask, render_template, request

app = Flask(__name__)

MAINTENANCE_MODE = True

@app.before_request
def check_maintenance():
    if MAINTENANCE_MODE:
        # Tillad static filer (ellers virker billeder ikke!)
        if request.path.startswith('/static/'):
            return None
        return render_template("maintenance.html"), 503

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quotes")
def quotes():
    return render_template("quotes.html")

@app.route("/python")
def python_page():
    return render_template("python.html")

if __name__ == "__main__":
    app.run(debug=True)
