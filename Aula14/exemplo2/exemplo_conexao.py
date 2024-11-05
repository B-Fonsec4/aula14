from sqlalchemy import create_engine, text
import pandas as pd

# variaveis de conexão com o banco

host = 'localhost'
user='root'
password ='root'
database ='bd_produtos'
# Função para conectar ao banco
def conecta_banco():
    try:
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
        with engine.connect() as conexao:
            query = "SELECT * FROM vendas"
            resultados = conexao.execute(text(query))
            for item in resultados:
                # print(f' {item[0]},  {item[1]}, {item[2]}')
                df = pd.DataFrame(resultados)
                print(df)
    except ImportError as e:
        print(f'Erro: {e}')

# Chama função que conecta  ao banco de dados
conecta_banco()