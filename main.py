
from flask import Flask
app = Flask(__name__)

@app.route("/test")
def hello():
	return "Hello World!"

@app.route("/hello")
def bjorn():
    return "Hello from python-flask-sti build image"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
