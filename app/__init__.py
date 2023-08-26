from flask import Flask
from restx_api import restx_blueprint

app = Flask(__name__)
app.register_blueprint(restx_blueprint, url_prefix='/api')

from . import routes
from . import database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_tests.db'
database.init_db(app)
