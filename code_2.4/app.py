
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        return process_form()


def process_form():
    email = request.form["email"]
    password = request.form["password"]

    if email == "" or password == "":
        return render_template("register.html", error=True)
    else:
        return render_template("register_confirmation.html")


if __name__ == "__main__":
    app.run()


