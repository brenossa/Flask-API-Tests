from restx_api import api
from restx_api.models import *

from app.database import db, Cliente

from flask import request, jsonify
from flask_restx import Resource, fields

clientes = api.namespace("clientes",
                         description="Endpoint para controle de clientes")

@clientes.route("/")
class ClientesResource(Resource):
    @clientes.doc(
        responses={
            200: ('Lista de clientes exibida com sucesso', clientes_list_model)
        }
    )
    def get(self):
        """Ver lista de clientes"""
        clientes = Cliente.query.all()
        return jsonify([{
            "id": cliente.id,
            "nome": cliente.nome,
            "email": cliente.email,
            "telefone": cliente.telefone
        } for cliente in clientes])

    @clientes.doc(
        responses={
            201: ('Cliente criado com sucesso', api_response_model)
        },
        body=cliente_model
    )
    def post(self):
        """Criar um novo cliente"""
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        print(nome, email, telefone)

        novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
        db.session.add(novo_cliente)
        db.session.commit()

        return jsonify({
            "resultado": "cliente adicionado com sucesso"
        })

@clientes.route("/<int:id_cliente>")
class ClienteResource(Resource):
    @clientes.doc(
        responses={
            200: ('Cliente encontrado com sucesso', cliente_response_model)
        }
    )
    def get(self, id_cliente):
        """Buscar cliente por id"""
        cliente = Cliente.query.get(id_cliente)
        if cliente:
            return jsonify({
                "id": cliente.id,
                "nome": cliente.nome,
                "email": cliente.email,
                "telefone": cliente.telefone
            })
        else:
            return jsonify({"resultado": "cliente não encontrado"}), 404

    @clientes.doc(
        responses={
            200: ('Cliente deletado com sucesso', api_response_model)
        }
    )
    def delete(self, id_cliente):
        """Deletar cliente por id"""
        cliente = Cliente.query.get(id_cliente)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()
            return jsonify({
                "resultado": "cliente deletado com sucesso"
            })
        else:
            return jsonify({"resultado": "cliente não encontrado"}), 404

    @clientes.doc(
        responses={
            200: ('Cliente atualizado com sucesso', api_response_model)
        }
    )
    def put(self, id_cliente):
        """Atualizar cliente por id"""
        cliente = Cliente.query.get(id_cliente)
        if cliente:
            nome = request.form.get("nome")
            email = request.form.get("email")
            telefone = request.form.get("telefone")

            cliente.nome = nome
            cliente.email = email
            cliente.telefone = telefone

            db.session.commit()

            return jsonify({
                "resultado": "cliente atualizado com sucesso"
            })
        else:
            return jsonify({"resultado": "cliente não encontrado"}), 404
