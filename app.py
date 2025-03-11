import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db

app = None

def create_app():
    app = Flask(__name__)
    if os.getenv("FLASK_ENV", "development") == "production":
        raise Exception("Currently no production configuration available")
    else:
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    return app

app = create_app()

from application.controllers import *

if __name__ == "__main__":
    app.run(host="0.0.0.0")