"""
    hotface.configs.testing
    ~~~~~~~~~~~~~~~~~~~~


"""
from flaskbb.configs.default import DefaultConfig


class TestingConfig(DefaultConfig):

    # Indicates that it is a testing environment
    DEBUG = False
    TESTING = True

    # SQLAlchemy connection options
    # This will create in the applications folder (where manage.py is)
    # a database named flaskbb.sqlite.
    SQLALCHEMY_DATABASE_URI = (
        'sqlite://'
    )

    SERVER_NAME = "localhost:5000"

    # This will print all SQL statements
    SQLALCHEMY_ECHO = False

    # Security
    SECRET_KEY = "SecretKeyForSessionSigning"
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "reallyhardtoguess"

    # Recaptcha
    # To get recaptcha, visit the link below:
    # https://www.google.com/recaptcha/admin/create
    # Those keys are only going to work on localhost!
    RECAPTCHA_ENABLED = True
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = "6LcZB-0SAAAAAGIddBuSFU9aBpHKDa16p5gSqnxK"
    RECAPTCHA_PRIVATE_KEY = "6LcZB-0SAAAAAPuPHhazscMJYa2mBe7MJSoWXrUu"
    RECAPTCHA_OPTIONS = {"theme": "white"}

    # Mail
    # Local SMTP Server
    #MAIL_SERVER = "localhost"
    #MAIL_PORT = 25
    #MAIL_USE_SSL = False
    #MAIL_USERNAME = ""
    #MAIL_PASSWORD = ""
    #MAIL_DEFAULT_SENDER = "noreply@example.org"

    # Google Mail Example
    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = "linhanqiu1123@163.com"
    MAIL_PASSWORD = "linhanqiu1123"
    MAIL_DEFAULT_SENDER = ("linhanqiu", "linhanqiu1123@163.com")

    CELERY_ALWAYS_EAGER = True
    CELERY_RESULT_BACKEND = "cache"
    CELERY_CACHE_BACKEND = "memory"
    CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

    # The user who should recieve the error logs
    ADMINS = ["linhanqiu1123@163.com"]
