from sys import argv

import bottle
from bottle import *
bottle.debug(True)

#templates

@route("/")
def index():
    return """
    <h3>verkefni 3<h3>
    <p><a href="/a">lidur A</a></p>
    <p><a href="/b">lidur B</a></p>
    """


@route("/a")
def index():
    return template("tempA.tpl")


@route("/sida/<kt>")
def page(kt):
    return template("temp_kt.tpl",kt=kt)


@route("/static/<skra>")
def static_skra(skra):
    #return static file(skra, root='/static')

@route("/b")
def index():
    return template("index.tpl")


@error(404)
def villa(error):
    return "<h2 style = color:red>dessi sida finnst ekki</h2>"


bottle.run(host='0.0.0.0', port=argv[1])
#run(host = 'localhost',port= 5000, reloader=True, debug=True)
