from bottle import route, run, template


@route('/hello/')
@route('/hello')
def index():
    return '<b>Hello World !</b>'


run(host='localhost', port=8080, reloader=True)
