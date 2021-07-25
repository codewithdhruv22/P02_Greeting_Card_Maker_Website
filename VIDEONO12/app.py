from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)

#DATABASE DETAILS CONFIGURATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/shubhkamna'
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "shubhkamna"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


class Profile(db.Model):
    id = db.Column(db.Integer,primary_key = True,nullable = False)
    name = db.Column(db.String(255),nullable = False)
    email = db.Column(db.String(255),nullable = False)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginUser" , methods = ["POST", "GET"])
def loginUser():
    if request.method == "POST":
        name = request.form.get("Myname")
        email = request.form.get("Myemail")
        entry = Profile(name = name , email = email)
        db.session.add(entry)
        db.session.commit()
        print("DETAILS UPDATED")
    return render_template("index.html")

app.run(debug = True)