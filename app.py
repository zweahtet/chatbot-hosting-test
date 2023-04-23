# import os
# from datetime import datetime

# from flask import Flask, redirect, render_template, request, url_for
# from model import initialize_index

# app = Flask(__name__)
# index = None

# @app.route("/")
# def home():
#     return render_template('chat.html')

# @app.route("/get")
# def get_bot_response():
#     query_text = request.args.get("msg", None)
#     if query_text is None:
#         return "Invalid input"
#     response = index.query(query_text)
#     return str(response), 200

# if __name__ == "__main__":
#     index = initialize_index("index.json")
#     app.run(debug=True)
import os
from datetime import datetime

import openai
from flask import Flask, redirect, render_template, request, session, url_for
from model import initialize_index

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'my-secret-key')
index = None

# Set up OpenAI authentication
# openai.api_key = os.environ.get('OPENAI_API_KEY')

@app.route("/")
def home():
    if 'access_token' not in session:
        return render_template('auth.html')
    global index
    try: 
        index = initialize_index("index.json")
    except:
        return render_template("auth.html", error="Invalid Token Key")
    return render_template('chat.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        access_token = request.form.get("access_token")
        openai.api_key = access_token
        session['access_token'] = access_token
        return redirect(url_for('home'))
    return render_template('auth.html')

@app.route("/logout")
def logout():
    session.pop('access_token', None)
    return redirect(url_for('home'))

@app.route("/chat")
def chat():
    query_text = request.args.get("msg", None)
    if query_text is None:
        return "Invalid input"

    if 'access_token' not in session:
        return redirect(url_for('login'))

    response = index.query(query_text)
    return str(response), 200


if __name__ == "__main__":
    app.run(debug=True)
