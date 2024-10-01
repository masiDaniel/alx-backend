#!/usr/bin/env python3
""" Flask barbel """
from flask import Flask, render_template
from flask_babel import Babel, request


class Config(object):
    """ Flask babel config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_local() -> str:
    """Gets locale based on the best match"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def Hello() -> str:
    """ Home page"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
