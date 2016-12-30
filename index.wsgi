import sae
from flaskbb import create_app
app = create_app(Config)
application = sae.create_wsgi_app(app)  