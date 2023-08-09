"""Main flask file for stockenheimer project"""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """Index page, should hold a search bar."""
    
    return "<p>Hello world!</p>"


