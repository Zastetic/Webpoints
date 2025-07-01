from sqlalchemy import create_engine, String, Integer, Column # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base # type: ignore
from sqlalchemy.inspection import inspect

# BANCO SQLITE
db = create_engine ("sqlite:///database/meu_banco.db")
Session = sessionmaker(bind=db)
session = Session()

# dados e tipo de dados do banco
Base = declarative_base()

class Classe_manha(Base):
    __tablename__='Classe_manha'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, unique=True)
    ponto = Column("ponto", Integer)

    def __init__(self,nome,ponto):
        self.nome = nome
        self.ponto = ponto

    def __repr__(self):
        return f"Casa: {self.nome}, ponto: {self.ponto}"

class Classe_tarde(Base):
    __tablename__='Classe_tarde'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, unique=True)
    ponto = Column("ponto", Integer)

    def __init__(self,nome,ponto):
        self.nome = nome
        self.ponto = ponto

    def __repr__(self):
        return f"Casa: {self.nome}, ponto: {self.ponto}"

class Classe_noite(Base):
    __tablename__='Classe_noite'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, unique=True)
    ponto = Column("ponto", Integer)

    def __init__(self,nome,ponto):
        self.nome = nome
        self.ponto = ponto

    def __repr__(self):
        return f"Casa: {self.nome}, ponto: {self.ponto}"


# cria requisicao de senha e usuaio do banco de dados update futuro
class Adm(Base):
    __tablename__ = 'Adms'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    senha = Column(String)

    def __init__(self,usuario,senha):
        self.usuario = usuario
        self.senha = senha

    def __repr__(self):
        return f" senha{self.senha} usuario{self.usuario}"


# dados = [
#     Classe_noite(nome='vcqsefoda', ponto=1202),
#     Classe_noite(nome='template', ponto=0),
#     Classe_noite(nome='erri essi', ponto=2),
# ]
# session.add_all(dados)
# session.commit()

Base.metadata.create_all(bind=db)
