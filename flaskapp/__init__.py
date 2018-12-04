from flask import Flask


def create_app(config: str = "config.DevelopmentConfig"):
    """
    Create an app instance
    """
    app = Flask(__name__)
    app.config.from_object(config)
    from flaskapp.views import data

    app.register_blueprint(data)
    return app
