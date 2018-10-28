from secrets import *
from flask import *
app = Flask(__name__)

admin_pw = "password123"
admin_token = ""

@app.route("/")
@app.route("/name/<name>")
def hello(name=None):
    return render_template("index.html", name=name)

@app.route("/admin", methods=['GET', 'POST'])
def admin():
 if request.form.get("password") == admin_pw:
      global admin_token
      admin_token = token_urlsafe(16)
      resp = make_response(render_template('admin.html'))
      resp.set_cookie('token', admin_token)
      return resp
 elif request.form.get("password") != admin_pw:
     return render_template('admin_login.html', error=True)
 elif request.cookies.get("token") == admin_token:
     return render_template('admin.html')
 else:
     return render_template('admin_login.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
