#!/usr/bin/env python
"""
    hotface.celery_worker
    ~~~~~~~~~~~~~~~~~~~~~

    Prepares the celery app for the celery worker.
    To start celery, enter this in the console::

        celery -A celery_worker.celery --loglevel=info worker

    :copyright: (c) 2016 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
from flaskbb.configs.development import DevelopmentConfig as Config
from flaskbb.app import create_app
from flaskbb.extensions import celery

app = create_app(Config)
