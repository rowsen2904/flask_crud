from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html"), 500123


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            if username == "admin" and password == "adminadmin":
                return "You logged in!"
            return "You sent wrong account credentials!"

    return render_template('auth/login.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7777, debug=True)
