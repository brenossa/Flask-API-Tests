from restx_api import api
from flask_restx import fields

cliente_model = api.model('Cliente', {
    'nome': fields.String(required=True, description='Nome do cliente'),
    'email': fields.String(required=True, description='Endereço de e-mail do cliente'),
    'telefone': fields.String(required=True, description="Telefone do cliente")
})

cliente_response_model = api.clone('ClienteResponse', cliente_model, {
    'id': fields.String(required=True, description="Id do cliente")
})

clientes_list_model = api.model('ClientesList', {
    'clientes': fields.List(fields.Nested(cliente_model), description='Lista de clientes')
})

api_response_model = api.model('ApiResponse', {
    'resultado': fields.String(required=True, description='Resultado da requisição')
})
