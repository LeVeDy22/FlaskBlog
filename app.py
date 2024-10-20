from flask import Flask, render_template
from models import db, Post

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html", content=Post.query.all())


@app.route("/base")
def base():
    return render_template("base.html")


if __name__ == "__main__":
    app.run()
