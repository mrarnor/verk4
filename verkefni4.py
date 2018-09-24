#from sys import argv
#verkefni 4




import bottle
from bottle import *
bottle.debug(True)
import urllib.request, json



@route("/")
def index():
    return """
    <h1> Verkefni 4 </h1>
    <a href="/a">Local Json</a> - 
    <a href="/b">Json API</a>
    """








with open("gengi.json","r") as skra:
    gengi = json.load(skra)
print(gengi)


@route("/a")
def index():
    return template("index.tpl")

with urllib.request.urlopen("http://docs.apis.is/currency/") as url:#http://docs.apis.is/#endpoint-currency
    data = json.loads(url.read().decode())

@route("/b")
def index():
    return template("index2.tpl", data = data)

@route("/Static/<skra>")
def static_skra(skra):
    return static_file(skra, root='./static')

@error(404)
def villa(error):
    return "<h2 style = color:red>Þessi síða finnst ekki</h2>"

run(host='localhost', port=8080, reloader=True, debug=True)






