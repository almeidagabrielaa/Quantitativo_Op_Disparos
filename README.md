# Projeto de ETL e Análise de Dados com Python

Este projeto realiza o ETL (Extração, Transformação e Carregamento) de dados a partir de planilhas, armazena-os em um banco de dados SQLite, e gera relatórios e visualizações com base nesses dados.

## Funcionalidades

### ETL (Extração, Transformação e Carregamento)

- **Extração:** Carrega dados de planilhas localizadas na pasta `data/raw/`.
- **Transformação:** Limpa e transforma os dados conforme necessário para análise.
- **Carregamento:** Insere os dados no banco SQLite em `data/processed/`, verificando duplicatas para evitar inserções redundantes.

### Banco de Dados SQLite

- **Estrutura Dinâmica:** Cria o banco de dados e as tabelas caso ainda não existam.
- **Inserção Segura:** Adiciona dados novos, garantindo que não ocorram duplicações.

### Relatórios

- **Geração de CSV:** Produz relatórios quantitativos com base nos dados do SQLite e os salva na pasta `reports/csv/`.

### Visualizações

- **Gráficos com Plotly:** Cria gráficos interativos, como histogramas e gráficos de linha, para visualização de tendências e distribuições, armazenando-os na pasta `reports/plots/`.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd my_project
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Coloque as planilhas na pasta `data/raw/`.
2. Execute o script principal para processar os dados:
    ```bash
    python src/etl.py
    ```
3. Confira os relatórios na pasta `reports/csv/` e os gráficos na pasta `reports/plots/`.

## Contribuição

Contribuições são bem-vindas! Por favor, siga o fluxo padrão de fork e pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Estrutura do Projeto

```plaintext
my_project/
│
├── data/
│   ├── raw/              # Planilhas originais
│   ├── processed/        # Arquivos CSV e SQLite
│
├── reports/
│   ├── csv/              # Relatórios quantitativos em CSV
│   ├── plots/            # Gráficos gerados com Plotly
│
├── src/
│   ├── __init__.py       # Indica que a pasta é um pacote Python
│   ├── etl.py            # Lógica de extração, transformação e carregamento
│   ├── database.py       # Funções para interagir com o SQLite
│   ├── reporting.py      # Geração de relatórios quantitativos
│   ├── plotting.py       # Geração de gráficos usando Plotly
│
├── tests/
│   ├── test_etl.py       # Testes para o módulo etl.py
│   ├── test_database.py  # Testes para o módulo database.py
│
├── README.md             # Instruções e documentação do projeto
├── requirements.txt      # Dependências do projeto
└── .gitignore            # Arquivos e pastas a serem ignorados pelo Git


