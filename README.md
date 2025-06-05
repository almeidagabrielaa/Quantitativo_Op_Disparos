# Projeto de ETL e Análise de Dados com Python

Este projeto tem como objetivo realizar o processo de ETL (Extração, Transformação e Carregamento) de dados a partir de uma planilha, armazená-los num banco de dados SQLite, e gerar relatórios e visualizações com base nesses dados.

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

# Funcionalidades

ETL: Realiza a extração de dados de planilhas, transformação e carregamento no banco de dados SQLite.
Relatórios: Gera relatórios quantitativos em formato CSV.
Visualizações: Cria gráficos interativos utilizando Plotly.