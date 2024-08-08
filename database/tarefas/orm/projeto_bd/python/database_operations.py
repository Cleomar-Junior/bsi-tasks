import psycopg2

# Configuração da conexão
connection = psycopg2.connect(
    dbname="atividadesbd",
    user="usuario",
    password="senha",
    host="localhost",
    port="5432"
)

cursor = connection.cursor()

# Função para inserir uma atividade
def inserir_atividade(nome_atividade, descricao, projeto_id):
    cursor.execute(
        "INSERT INTO atividades (nome, descricao, projeto_id) VALUES (%s, %s, %s)",
        (nome_atividade, descricao, projeto_id)
    )
    connection.commit()

# Função para atualizar o líder de um projeto
def atualizar_lider_projeto(projeto_id, novo_lider):
    cursor.execute(
        "UPDATE projetos SET lider = %s WHERE id = %s",
        (novo_lider, projeto_id)
    )
    connection.commit()

# Função para listar todos os projetos e suas atividades
def listar_projetos_e_atividades():
    cursor.execute(
        "SELECT p.nome, a.nome, a.descricao FROM projetos p JOIN atividades a ON p.id = a.projeto_id"
    )
    for row in cursor.fetchall():
        print(f"Projeto: {row[0]}, Atividade: {row[1]}, Descrição: {row[2]}")

# Exemplo de uso das funções
if __name__ == "__main__":
    # Inserir uma nova atividade
    inserir_atividade("Desenvolvimento Backend", "Implementar a lógica do servidor", 1)

    # Atualizar o líder de um projeto
    atualizar_lider_projeto(1, "Novo Líder")

    # Listar todos os projetos e suas atividades
    listar_projetos_e_atividades()

# Fechar a conexão
cursor.close()
connection.close()
