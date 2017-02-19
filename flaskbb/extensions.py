# -*- coding: utf-8 -*-
"""
    hotface.extensions
    ~~~~~~~~~~~~~~~~~~


"""
from celery import Celery
from flask_allows import Allows
from flask_sqlalchemy import SQLAlchemy
from flask_whooshee import Whooshee
from flask_login import LoginManager
from flask_mail import Mail
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_redis import Redis
from flask_migrate import Migrate
from flask_themes2 import Themes
from flask_plugins import PluginManager
from flask_babelplus import Babel
from flask_wtf.csrf import CsrfProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flaskbb.exceptions import AuthorizationRequired


# Permissions Manager
allows = Allows(throws=AuthorizationRequired)

# Database
db = SQLAlchemy()

# Whooshee (Full Text Search)
whooshee = Whooshee()

# Login
login_manager = LoginManager()

# Mail
mail = Mail()

# Caching
cache = Cache()

# Redis
redis_store = Redis()

# Debugtoolbar
debugtoolbar = DebugToolbarExtension()

# Migrations
migrate = Migrate()

# Themes
themes = Themes()

# PluginManager
plugin_manager = PluginManager()

# Babel
babel = Babel()

# CSRF
csrf = CsrfProtect()

# Rate Limiting
limiter = Limiter(auto_check=False, key_func=get_remote_address)

# Celery
celery = Celery("flaskbb")
