
from flask import Flask
app = Flask(__name__)

@app.route("/test")
def hello():
	return "Hello World!"

@app.route("/ruuuuuler")
def bjorn():
    return "Bjorn kan nå S2I"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
