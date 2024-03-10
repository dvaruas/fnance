import os


class AppConfig:
    DEBUG = True
    RESOURCES_DIR = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "resources",
        )
    )
    DB_PATH = os.path.join(RESOURCES_DIR, "data.db")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(16)
