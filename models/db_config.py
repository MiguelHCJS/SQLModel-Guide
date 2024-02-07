from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    Session,
)
from typing import Optional


class Engine():
    def __init__(self):
        self.__engine = create_engine('sqlite:///db/abda.db')

    def create_all(self):
        SQLModel.metadata.create_all(self.__engine)

    def makesession(self):
        with Session(self.__engine) as session:
            self.session = session

    def __enter__(self):
        self.makesession()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        print("Sessão fechada com sucesso!")


"""Obter regras posteriormente"""


class Jogador(SQLModel, table=True):
    """Nome do jogador

    Para registrar o jogador, dono do personagem ou dos personagens.
    """
    id_jogador: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False)


class Signo(SQLModel, table=True):
    id_signo: Optional[int] = Field(default=None, primary_key=True)
    descricao_do_signo: str = Field(nullable=False)


class Origem(SQLModel, table=True):
    """Angelical, demoniaca, animal...

    Inserir origem diversas.
    """
    id_origem: Optional[int] = Field(default=None, primary_key=True)
    descricao_da_origem: str = Field(nullable=False)


class Casta(SQLModel, table=True):
    """Derivada da origel angelical ou demoniaca.
    """
    id_casta: Optional[int] = Field(default=None, primary_key=True)
    descricao_da_casta: str = Field(nullable=False)


class Habilidade(SQLModel, table=True):
    id_habilidade: Optional[int] = Field(default=None, primary_key=True)
    nome_da_habilidade: str = Field(nullable=False)
    descricao: str = Field(nullable=False)


class Item(SQLModel, table=True):
    id_item: Optional[int] = Field(default=None, primary_key=True)
    nome_do_item: str = Field(nullable=False)
    descricao: str = Field(nullable=False)


class Personagem(SQLModel, table=True):
    """Personagem no RPG

    Centraliza toda a informacao geral do personagem.
    """
    id_personagem: Optional[int] = Field(default=None, primary_key=True)
    nome_do_personagem: str = Field(nullable=False)
    # Atributos Pag. 20
    # Habilidades Pag. 21
    # Caracteristicas/Positivas e Negativas Pag. 27
    # Casta
    # Signo
    # Origem
    # Aura Pag. 35
    # Divindades Pag. 36
    # Gloria


"""Regras de combate, posterior a construir o Banco de Dados"""


if __name__ == "__main__":
    ENGINE = Engine(nome_do_banco='abda')
    ENGINE.create_all()
