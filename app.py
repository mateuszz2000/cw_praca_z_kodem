"""Flask app"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """
    Function which represent endpoint which return h1 marker with text content
    """
    return "<h1>Hello WSB! Greetings from Flask & Docker!<h1>"


if __name__ == "__main__":
    app.run(debug=True)
