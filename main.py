from bottle import route, run
from misc import add


@route("/hello/")
@route("/hello")
def index():
    return "<b>Hello World !</b>"


@route('/add/<a>/<b>')
@route('/add/<a>/<b>/')
def route_add(a, b):
    return {'result': add(a, b)}


run(host="localhost", port=8080, reloader=True)
