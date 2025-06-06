import os
import glob
import pandas as pd
import sqlite3

def extract(file_path):
    """
    Extrai dados de um arquivo CSV localizado no caminho especificado.
    
    :param file_path: Caminho para o arquivo CSV.
    :return: DataFrame com os dados extraídos.
    """
    try:
        data = pd.read_csv(file_path, encoding='latin1')
        print(f"Dados extraídos do arquivo: {file_path}")
        return data
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        return None

def transform(data):
    """
    Transforma os dados conforme necessário. Exemplo: limpeza de dados.
    
    :param DataFrame com os dados extraídos.
    :return: DataFrame com os dados transformados.
    """
    try:
        # Exemplo de transformação: remover linhas duplicadas
        transformed_data = data.drop_duplicates()
        # Exemplo de transformação: preencher valores nulos
        transformed_data.fillna(method='ffill', inplace=True)
        print("Dados transformados com sucesso.")
        return transformed_data
    except Exception as e:
        print(f"Erro ao transformar dados: {e}")
        return None

def load(data, db_path):
    """
    Carrega os dados transformados para um banco de dados SQLite.
    
    :param DataFrame com os dados transformados.
    :param db_path: Caminho para o banco de dados SQLite.
    """
    try:
        conn = sqlite3.connect(db_path)
        data.to_sql('operacao_disparos', conn, if_exists='append', index=False)
        conn.close()
        print("Dados carregados no banco de dados com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

def etl_process():
    """
     Executa o processo ETL completo: extração, transformação e carregamento para todos os arquivos CSV na pasta especificada.
    """
    # Caminho para o arquivo CSV
    file_path = 'data/raw/Operação_ate_0406.csv'
    # Caminho para o banco de dados SQLite
    db_path = 'data/processed/operação_disparos.db'

    # Executa cada etapa do ETL
    data = extract(file_path)
    if data is not None:
        transformed_data = transform(data)
        if transformed_data is not None:
            load(transformed_data, db_path)

if __name__ == "__main__":
    etl_process()