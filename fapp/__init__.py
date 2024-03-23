import os

from flask import Flask

from config import AppConfig
from fapp.models import db

app = Flask(__name__)
app.config.from_object(AppConfig)

# If not exists, create required directories.
resources_dir = app.config["RESOURCES_DIR"]
if not os.path.exists(resources_dir):
    os.mkdir(resources_dir)

with app.app_context():
    db.init_app(app=app)
    db.create_all()
    db.session.commit()

    from fapp.viewers import app_mod

    app.register_blueprint(app_mod)
