import requests
import json
import pandas as pd

from bs4 import BeautifulSoup

search_params = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'X', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

names = []
situacao = []

for param in search_params:
    r = requests.get(f'https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial={param}')
    page = BeautifulSoup(r.content, 'html5lib')

    i = 2

    while i < len(page.find_all('tr')):
        names.append(page.find_all('tr')[i].find_all('td')[1].find('a').contents[0])
        situacao.append(page.find_all('tr')[i].find_all('td')[4].find('a').contents[0])
        i += 1
    print(names)

companies = {
            "Names": names, 
            "Situacoes": situacao,
        }

df = pd.DataFrame(companies, columns=companies.keys())

df.to_csv(f'./all_companies_ever_listed_on_B3_and_their_status.csv')

print(df)