from flask import Flask
# from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# app.config.from_object(Config)

from server import app, models
db = SQLAlchemy(app)
migrate = Migrate(app, db)