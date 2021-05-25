from flask import Flask,render_template,redirect,url_for
app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for("route",name = "RAMANUJAN"))


@app.route("/route/<string:name>")
def route(name):
    return name

if __name__ == "__main__":
    app.run(debug=True)
