"""Main flask file for stockenheimer project"""

from flask import Flask
from asx_price_getter import get_stock_daily_change

app = Flask(__name__)


@app.route("/")
def index():
    """Index page, should hold a search bar."""
    
    return "<p>Hello world!</p>"


@ app.route("/<string:ticker>")
def stock_page(ticker: str):
    """Stock page, displays the meme"""

    # perform stock test
    # need to escape the input string :)
    happy = True


    image_path = ""
    if (happy):
        image_path = "images/happyheimer.jpg"
    else:
        image_path = "images/sadenheimer.png"
    # need to have these images the same type for my sake

    
    return f'<img src="{image_path}" alt="oppenheimer">'

