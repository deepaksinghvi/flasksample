from flask import Flask
app = Flask(__name__)


@app.route('/')
def hellodefault():
    return "Hello World!"

@app.route("/hello/")
def hello():
    return "Hello"

@app.route('/hello/<string:name>/')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)