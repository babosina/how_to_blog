import requests
import smtplib
import os

from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.npoint.io/405401fd224c5d58a066"

posts = requests.get(URL).json()
current_year = datetime.now().year
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def index():
    return render_template("index.html", posts=posts,
                           current_year=current_year)


@app.route("/about")
def about():
    return render_template("about.html",
                           current_year=current_year)


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
        return render_template("contact.html", current_year=current_year,
                               msg_sent=False)


@app.route("/post/<int:post_id>")
def post(post_id):
    requested_post = None
    for post in posts:
        if post.get('id') == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post,
                           current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
