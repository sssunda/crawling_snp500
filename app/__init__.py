# Third Party Module Import
from flask import Flask

# Apps Module Import
from app.crawling.views import crawling_blueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(crawling_blueprint)
    return app