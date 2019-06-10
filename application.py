import os

from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

counter = 1000


@app.route("/")
def index():
    user = session.get('user', None)
    return f"<html><body>User is {user}</body></html>"


@app.route("/create")
def create_session():
    if 'user' in session:
        return redirect('/')

    global counter
    counter += 1

    user = {'username': "joe", 'email': 'joe@example.com', 'user_id': counter}
    session['user'] = user

    return redirect('/')


@app.route("/clear")
def clear_session():
    user = session.pop('user', None)
    value_now = session.get('user', None)
    return f"Removed session for user {user} value is now {value_now}"


@app.route("/clearall")
def clear_all():
    session.clear()
    return redirect("/")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
