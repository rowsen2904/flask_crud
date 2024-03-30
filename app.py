from datetime import datetime

from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(150), nullable=False)
    page_size = db.Column(db.Integer, nullable=False)
    released_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Author: {self.author}>"


@app.route("/", methods=["GET", "POST"])
def books_list_create():
    status_code = 200
    books = Book.query.all()
    if request.method == "POST":
        author = request.form.get("author")
        page_size = request.form.get("page_size")
        released_date = request.form.get("released_date")
        if author and page_size and released_date:
            released_date = datetime.strptime(released_date, "%Y-%m-%d")
            book = Book(author=author, page_size=page_size, released_date=released_date)
            db.session.add(book)
            db.session.commit()
            status_code = 201

    return render_template("index.html", books=books), status_code


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
