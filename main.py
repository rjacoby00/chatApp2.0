from flask import *
app = Flask(__name__)

@app.route("/")
@app.route("/name/<name>")
def hello(name=None):
    return render_template("index.html", name=name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
