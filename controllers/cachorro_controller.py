from models.cachorro import Cachorro, db

def criar_cachorro(nome, raca, idade):
    novo = Cachorro(nome=nome, raca=raca, idade=idade)
    db.session.add(novo)
    db.session.commit()
    return novo

def listar_cachorros():
    return Cachorro.query.all()

def get_cachorro_by_id(id):
    return Cachorro.query.get(id)
