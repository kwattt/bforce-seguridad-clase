from flask import Flask, request, session, render_template
from flask_session import Session

from werkzeug.exceptions import BadRequest
from werkzeug.utils import redirect
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "redis"

app.config.from_object(__name__)
Session(app)

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

# Route called '/login/' with POST method, checks if the username and password are correct
total_passwords = 0

@app.route('/login', methods=['POST'])
def login():
    global total_passwords
    username = request.form['username']
    password = request.form['password']
    total_passwords+=1

    if total_passwords%1000 == 0:
        print(total_passwords, username, password)

    if username == 'jorge_gonzalez' and password == '&!pass542':
        session["username"] = request.form.get("username")
        return redirect('/')
    else:
        return 'Login failed', 401

@app.route('/logout')
def logout():
    session.pop("username", None)
    return 'Logout successful', 200 

@app.route('/')
def index():
    return render_template('index.html', user=session.get("username"))

if __name__ == '__main__':
    app.run(debug=True)