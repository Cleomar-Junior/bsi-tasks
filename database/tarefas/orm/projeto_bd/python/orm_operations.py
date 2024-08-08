from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "postgresql+psycopg2://usuario:senha@localhost:5432/atividadesbd"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelos do Banco de Dados
class Projeto(Base):
    __tablename__ = "projetos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    lider = Column(String)
    atividades = relationship("Atividade", back_populates="projeto")

class Atividade(Base):
    __tablename__ = "atividades"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    projeto_id = Column(Integer, ForeignKey("projetos.id"))
    projeto = relationship("Projeto", back_populates="atividades")

Base.metadata.create_all(bind=engine)

# Funções ORM
def inserir_atividade(session, nome_atividade, descricao, projeto_id):
    atividade = Atividade(nome=nome_atividade, descricao=descricao, projeto_id=projeto_id)
    session.add(atividade)
    session.commit()

def atualizar_lider_projeto(session, projeto_id, novo_lider):
    projeto = session.query(Projeto).filter(Projeto.id == projeto_id).first()
    projeto.lider = novo_lider
    session.commit()

def listar_projetos_e_atividades(session):
    projetos = session.query(Projeto).all()
    for projeto in projetos:
        print(f"Projeto: {projeto.nome}, Líder: {projeto.lider}")
        for atividade in projeto.atividades:
            print(f"  Atividade: {atividade.nome}, Descrição: {atividade.descricao}")

# Exemplo de uso das funções ORM
if __name__ == "__main__":
    session = SessionLocal()

    # Inserir uma nova atividade
    inserir_atividade(session, "Desenvolvimento Frontend", "Implementar a interface do usuário", 1)

    # Atualizar o líder de um projeto
    atualizar_lider_projeto(session, 1, "Outro Novo Líder")

    # Listar todos os projetos e suas atividades
    listar_projetos_e_atividades(session)

    session.close()
