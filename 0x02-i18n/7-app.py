#!/usr/bin/env python3
""" Flask barbel """
from flask import g, Flask, render_template
from flask_babel import Babel, request
from typing import Optional

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
def get_locale() -> str:
    """Gets locale from query string"""
    req = request.query_string.decode('UTF-8').split("&")
    table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        req,))
    if "locale" in table:
        if table["locale"] in Config.LANGUAGES:
            return table["locale"]
    if "login_as" in table:
        if g.user['locale'] in Config.LANGUAGES:
            return g.user['locale']
    if request.headers.get('Accept-Language') in Config.LANGUAGES:
        return request.header.get('Accept-Language')
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user() -> Optional[dict]:
    """
    Returns a users dictionary or None is user doesn't exist
    """
    req = request.query_string.decode("UTF-8").split("&")
    table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        req,))
    user_id = table.get('login_as', None)
    if user_id is not None:
        user_id = int(user_id)
        if user_id in users:
            return users[user_id]
    return None


@app.before_request
def before_request():
    """
    sets g.user before every request
    """
    user = get_user()
    g.user = user


@app.route("/")
def Hello() -> str:
    """ Home page"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run()
