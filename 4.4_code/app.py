
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
    url = request.form["url"]

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
        "url": {
            "ok": True,
            "msg": "Invalid URL",
            "val": url,
        },
    }

    if not re.search(r"[a-z]", first_name, re.IGNORECASE):
        validations["ok"] = False
        validations["first_name"]["ok"] = False
    if not re.search(r"[a-z]", last_name, re.IGNORECASE):
        validations["ok"] = False
        validations["last_name"]["ok"] = False
    if not valid_email(email):
        validations["ok"] = False
        validations["email"]["ok"] = False
    if not valid_password(password):
        validations["ok"] = False
        validations["password"]["ok"] = False
    if not re.search(r"^https?:\/\/(www\.)?linkedin\.com\/\w{2}/(\w+)$", url):
        validations["ok"] = False
        validations["url"]["ok"] = False

    if validations["ok"]:
        user_data = _get_user_data(first_name, last_name, email, url)
        return render_template("register_confirmation.html", user_data=user_data)
    else:
        return render_template("register.html",
                               error=validations)


def valid_email(email):
    if re.search(r"^[a-z]{1,8}\.[a-z]+@[a-z]+\.[a-z]{2,4}$", email):
        return True

    return False
    

def valid_password(password):
    if re.search(r"^(?=.{8,16}$)(?=.*\d)(?=.*[A-Z])(?=.*\W)", password):
        return True

    return False


def _get_user_data(first_name, last_name, email, url):
    full_name = first_name + " " + last_name
    
    # get domain of email
    m = re.search(r"^[a-z]{1,8}\.[a-z]+@([a-z]+\.[a-z]{2,4})$", email)
    email_domain = m.group(1)

    # get LinkedIn username
    m = re.search(r"^https?:\/\/(?:www\.)?linkedin\.com\/\w{2}/(\w+)$", url)
    linkedin_username = m.group(1)

    return {
        "full_name": full_name,
        "email": email,
        "email_domain": email_domain,
        "url": url,
        "linkedin_username": linkedin_username,
    }

    
if __name__ == "__main__":
    app.run()


