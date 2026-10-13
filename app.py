from flask import Flask, render_template, request

app = Flask(__name__)
import os

@app.route("/debug-static")
def debug_static():
    path = os.path.join(app.static_folder, "images", "myclick-splash-final.webp")
    exists = os.path.exists(path)
    files = []
    try:
        files = os.listdir(os.path.join(app.static_folder, "images"))
    except Exception as e:
        files = [f"FEJL: {e}"]

    return f"""
    <h1>Debug Static</h1>
    <p>Static folder: {app.static_folder}</p>
    <p>Looking for: {path}</p>
    <p>Exists: {exists}</p>
    <p>Files in static/images: {files}</p>
    <p>Current dir: {os.getcwd()}</p>
    <p>List root: {os.listdir('.')}</p>
    """

# True = maintenance page
# False = normal website
MAINTENANCE_MODE = True

@app.before_request
def check_maintenance():
    if MAINTENANCE_MODE:
        # 1. TILLAD ALTID static filer - ellers får du 404!
        if request.path.startswith('/static/'):
            return None
        # 2. Tillad også selve static endpointet
        if request.endpoint == 'static':
            return None
        # 3. Alt andet = vis maintenance
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
