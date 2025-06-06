import os

def create_project_structure():
    # Estrutura de diretórios relativa ao diretório atual
    directories = [
        'data/raw',
        'data/processed',
        'reports/csv',
        'reports/plots',
        'src',
        'tests'
    ]

    # Arquivos que devem ser criados
    files = {
        'src/__init__.py': '',
        'src/etl.py': '# Lógica de extração, transformação e carregamento\n',
        'src/database.py': '# Funções para interagir com o SQLite\n',
        'src/reporting.py': '# Geração de relatórios quantitativos\n',
        'src/plotting.py': '# Geração de gráficos usando Plotly\n',
        'tests/test_etl.py': '# Testes para o módulo etl.py\n',
        'tests/test_database.py': '# Testes para o módulo database.py\n',
        'requirements.txt': '# Lista de dependências do projeto\n'
    }

    # Criar diretórios
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Criar arquivos
    for file_path, file_content in files.items():
        with open(file_path, 'w') as f:
            f.write(file_content)

    print("Estrutura de pastas e arquivos criada com sucesso!")

if __name__ == "__main__":
    create_project_structure()