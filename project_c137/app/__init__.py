from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)

    CORS(app)
    db.init_app(app)

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    return app
