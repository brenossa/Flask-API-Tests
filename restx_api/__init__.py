from flask import Blueprint
from flask_restx import Api

restx_blueprint = Blueprint("restx_api", __name__)
api = Api(restx_blueprint, version="1.0", title="Documentação das APIs",
          description="APis foram feitas para fins de aprendizado.",
          doc="/swagger")

from app import database

from restx_api import models
from restx_api import api_routes
