import requests
from flask import Flask

app = Flask(__name__)

"""
flask run
flask run --debug

app.route("/path/<type:var")
def method(var):

return "method()" => go to method route
ou 
from flask import redirect, url_for
return redirect(url_for('login'))
@app.route('/login')

@app.get("route") ou app.post("") pour que ça soit géré auto

return render_template('hello.html', person=name)
template doit etre dispo: 
Cas 1 : Module
/application.py
/templates
    /hello.html
Case 2: a package:
/application
    /__init__.py
    /templates
        /hello.html

Ex template :
<!doctype html>
<title>Hello from Flask</title>
{% if person %}
  <h1>Hello {{ person }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}

Cookies loading: 
from flask import request
username = request.cookies.get('username')
# use cookies.get(key) instead of cookies[key] to not get a KeyError if the cookie is missing.
Cookie storing:
from flask import make_response
resp = make_response(render_template(...))
resp.set_cookie('username', 'the username')
return resp
"""

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")


@app.route("/")
def index():
    return response.json()
