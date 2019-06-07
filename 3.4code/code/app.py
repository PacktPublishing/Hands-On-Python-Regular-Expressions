
from flask import Flask, render_template, request
from pprint import pprint
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        return process_form()

def process_form():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]

    validations = {
        "ok": True, 
        "first_name": {
            "ok": True,
            "msg": "Invalid First Name",
            "val": first_name,
        },
        "last_name": {
            "ok": True,
            "msg": "Invalid Last Name",
            "val": last_name,
        },
        "email": {
            "ok": True,
            "msg": "Invalid Email",
            "val": email,
        },
        "password": {
            "ok": True,
            "msg": "Invalid Password",
            "val": password,
        },
    }

    if not re.match("[A-Z][a-z]", first_name):
        validations["ok"] = False
        validations["first_name"]["ok"] = False
    if not re.match("[A-Z][a-z]", last_name):
        validations["ok"] = False
        validations["last_name"]["ok"] = False
    if not valid_email(email):
        validations["ok"] = False
        validations["email"]["ok"] = False
    if not valid_password(password):
        validations["ok"] = False
        validations["password"]["ok"] = False

    pprint(validations)
    
    if validations["ok"]:
        return render_template("register_confirmation.html")
    else:
        return render_template("register.html",
                               error=validations)


def valid_email(email):
    if re.search(r"^[a-z]{1,8}\.[a-z]+@[a-z]+\.[a-z]{2,4}$", email):
        return True

    return False
    

def valid_password(password):
    if (re.search(r"^.{8,16}$", password) and re.search(r"\d", password) 
        and re.search(r"[A-Z]", password) and re.search(r"\W", password)) != None:
        return True

    return False


if __name__ == "__main__":
    app.run()


