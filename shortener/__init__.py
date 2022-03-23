from flask import Flask
from config import Config
from flask_migrate import Migrate
from .site.routes import site
from .models import db

app = Flask(__name__)
app.register_blueprint(site)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)