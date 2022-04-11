from bottle import route, run, template


@route("/hello")
def index(name):
    return template("<b>Hello World !</b>!")


run(host="localhost", port=8080)
