import os
from flaskapp import create_app

app = create_app(os.getenv(FLASK_CONFIG, default="config.DevelopmentConfig"))
