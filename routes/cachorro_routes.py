from flask import Blueprint, request, jsonify
from controllers.cachorro_controller import criar_cachorro, listar_cachorros, get_cachorro_by_id

cachorro_bp = Blueprint("cachorro_bp", __name__)

# POST - cadastrar cachorro
@cachorro_bp.route("/", methods=["POST"])
def cadastrar():
    dados = request.get_json()
    nome = dados.get("nome")
    raca = dados.get("raca")
    idade = dados.get("idade")

    cachorro = criar_cachorro(nome, raca, idade)
    return jsonify({
        "id": cachorro.id,
        "nome": cachorro.nome,
        "raca": cachorro.raca,
        "idade": cachorro.idade
    })

# GET - listar todos
@cachorro_bp.route("/", methods=["GET"])
def listar():
    cachorros = listar_cachorros()
    return jsonify([
        {
            "id": c.id,
            "nome": c.nome,
            "raca": c.raca,
            "idade": c.idade
        } for c in cachorros
    ])

@cachorro_bp.route("/<int:id>", methods=["GET"])
def buscar_por_id(id):
    cachorro = get_cachorro_by_id(id)
    if cachorro:
        return jsonify({
            "id": cachorro.id,
            "nome": cachorro.nome,
            "raca": cachorro.raca,
            "idade": cachorro.idade
        })
    else:
        return jsonify({"erro": "Cachorro não encontrado"}), 404
