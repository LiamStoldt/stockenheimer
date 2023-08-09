"""Main flask file for stockenheimer project"""

from flask import Flask
from asx_price_getter import get_stock_daily_change
import os


app = Flask(__name__)


img = os.path.join('static', 'Image')


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
        image_path = "happyheimer.jpg"
    else:
        image_path = "sadenheimer.png"
    # need to have these images the same type for my sake
    file = os.path.join(img, image_path)

    
    return f'<img src="{image_path}" alt="oppenheimer">'

