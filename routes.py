from flask import render_template, Flask, request

app = Flask(__name__)

app.secret_key="development-key"

@app.route("/")
def index():
    return "Hello world"