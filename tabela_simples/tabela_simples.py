#pip install pandas

import pandas as pd

produtos = [
    {"nome": "cuscuz", "preço": 5,"quantidade": 300},
    {"nome": "bolacha", "preço":2.50, "quantidade": 20 },
    {"nome": "chilito", "preço": 3, "quantidade": 400},
]

tabela = pd.DataFrame(produtos)
tabela