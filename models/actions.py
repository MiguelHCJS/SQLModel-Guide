from sqlmodel import Session
from db_config import Pessoa, ToDo


""" CRUD PESSOAS """


def criar_pessoa(
    engine,
    nome_pessoaa: str
):
    session = Session(engine)

    pessoa = Pessoa(nome=nome_pessoaa)

    session.add(pessoa)
    session.commit()


def buscar_pessoa():
    ...


def buscar_pessoas():
    ...


def alterar_pessoa():
    ...


def alterar_pessoas():
    ...


""" CRUD TAREFAS """


def criar_tarefa(
    engine,
    nome_tarefa: str,
    status_tarefa: str,
    pessoa: int
):
    session = Session(engine)

    tarefa = ToDo(
        tarefa=nome_tarefa,
        status=status_tarefa,
        id_pessoa=pessoa
    )

    session.add(tarefa)
    session.commit()
