CREATE TABLE projetos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    lider VARCHAR(255)
);

CREATE TABLE atividades (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    projeto_id INTEGER NOT NULL,
    FOREIGN KEY (projeto_id) REFERENCES projetos (id)
);