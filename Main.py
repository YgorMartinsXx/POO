# %%
# imports
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from datetime import date
from Classes import (
    Unidade_Producao,
    Peca,
    Registro_Falha,
    Sopradora,
    Torno_Cnc,
    Fresadora,
    Impressora3D
)
import os
from dotenv import load_dotenv

load_dotenv('.env')

#%%
#Acessando o banco de dados

usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")

engine = create_engine(f"mssql+pymssql://{usuario}:{senha}@{host}/{banco_de_dados}")

#%%
#Criando sessão de interação com o banco de dados

Session = sessionmaker(bind=engine)
session = Session()

#%%
# POPULACAO UNIDADE_PRODUCAO

unidade_producao1 = Unidade_Producao(
    numero = 1,
    peca_hora_nominal = 10,
    )

session.add(unidade_producao1)
session.commit()

unidade_producao2 = Unidade_Producao(
    numero = 2,
    peca_hora_nominal = 5,
    )

session.add(unidade_producao2)
session.commit()

#%%
# POPULACAO REGISTRO_FALHA

registro_falha1 = Registro_Falha(id = 1, severidade = 1, inicio =date(2015, 1, 4), fim = date(2012, 5, 6), numero_unidade_producao = 1)
registro_falha2 = Registro_Falha(id = 2, severidade = 0, inicio =date(2017, 4, 1), fim = date(2014, 7, 5), numero_unidade_producao = 2)

session.add(registro_falha1)
session.commit()

session.add(registro_falha2)
session.commit()

#%%
# POPULACAO PECA

PECA1 = Peca(
    numero = 1, 
    status = 'Reprovada', 
    inicio_fabricacao =date(2017, 4, 1), 
    fim_fabricacao = date(2023, 1, 5), 
    numero_unidade_producao = 1)

PECA2 = Peca(
    numero = 2, 
    status = 'Aprovada', 
    inicio_fabricacao =date(2018, 5, 5), 
    fim_fabricacao = date(2023, 4, 5), 
    numero_unidade_producao = 2)

session.add(PECA1)
session.commit()

session.add(PECA2)
session.commit()

#%%
# POPULACAO FRESADORA

fresadora1 = Fresadora(numero = 1, velocidade_rotacao = 1500, profundidade_corte = 3.0)
fresadora2 = Fresadora(numero = 2, velocidade_rotacao = 2000, profundidade_corte = 4.0)

session.add(fresadora1)
session.commit()

session.add(fresadora2)
session.commit()

#%%
# POPULACAO IMPRESSORA_3D

impressora3d1 = Impressora3D(numero = 1, espessura_camada = 3.0, tipo_material = 'acrilico')
impressora3d2 = Impressora3D(numero = 2, espessura_camada = 2.0, tipo_material = 'acrilico')

session.add(impressora3d1)
session.commit()

session.add(impressora3d2)
session.commit()

#%%
# POPULACAO SOPRADORA

sopradora1 = Sopradora(numero = 1, vazao_sopro = 1300, pressao_sopro = 10)
sopradora2 = Sopradora(numero = 2, vazao_sopro = 1000, pressao_sopro = 15)

session.add(sopradora1)
session.commit()

session.add(sopradora2)
session.commit()

#%%
# POPULACAO TORNO_CNC

torno1 = Torno_Cnc(numero = 1, velocidade_rotacao = 1500, tolerancia = 3)
torno2 = Torno_Cnc(numero = 2, velocidade_rotacao = 1000, tolerancia = 2)

session.add(torno1)
session.commit()

session.add(torno2)
session.commit()

#%%
# FECHAR SESSAO
session.close()