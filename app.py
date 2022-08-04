from markupsafe import escape
from flask import Flask
app = Flask(__name__)
from flask import url_for
from flask import request
@app.route('/login', methods=['POST', 'GET'])
def login_get(request.form['password']):
    X=escape(X)
    return "get"

