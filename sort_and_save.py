import requests
import json
import pandas as pd

from bs4 import BeautifulSoup

df = pd.read_csv(f'./all_companies_ever_listed_on_CVM_and_their_status.csv')

cancelado = []
cancelado_nome = []
ativo = []
ativo_nome = []

i = 0

while i < len(df['Situacoes']):

    if "Cancelado" in df['Situacoes'][i]:
        cancelado.append(df['Situacoes'][i])
        cancelado_nome.append(df['Names'][i])
    else:
        ativo.append(df['Situacoes'][i])
        ativo_nome.append(df['Names'][i])

    i +=1 

ativos = {
            "Names": ativo_nome, 
            "Situacoes": ativo,
        }

cancelados = {
            "Names": cancelado_nome, 
            "Situacoes": cancelado,
        }

da = pd.DataFrame(ativos, columns=ativos.keys())
dc = pd.DataFrame(cancelados, columns=cancelados.keys())

print(da)
print(dc)

da.to_csv(f'./CVM_active_listed.csv')
dc.to_csv(f'./CVM_cancelled_listing.csv')

# df['Names']
# df['Situacoes']