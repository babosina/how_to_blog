import requests
import smtplib
import os

from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from datetime import datetime, date
from post_form import PostForm

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    posts = db.session.execute(db.Select(BlogPost)).scalars().all()
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        with smtplib.SMTP(SMTP_SERVER, port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"""Subject:Feedback Form\n\nGreetings from {request.form.get('name')}.
Message from {request.form.get('email')}: {request.form.get('message')}
""")
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
