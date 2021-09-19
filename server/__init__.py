from flask import Flask
# # from config import Config

# from flask_migrate import Migrate
#
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# # app.config.from_object(Config)
#
# # from server import app, models
db = SQLAlchemy(app)
# # migrate = Migrate(app, db)

from .app import *
from .database_settings import *
from .db_crud import *
from .elastic import *
from .models import *
