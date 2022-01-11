# Bibliotecas
import csv
import requests
# Host PokeAPI
host = "https://pokeapi.co/api/v2"
# Conexão
conexao = requests.get(f"{host}/pokemon/ditto")
# Validação
if conexao.status_code != 200:
    print(f"Erro: Problema de conexão - {conexao.status_code}")
else:
    print("API conectada com sucesso")
# Operação get
pokemon = conexao.json()
with open('pokemon.csv', 'w') as file:
    coluna = ["Nome Habilidade", "Poder"]
    escrever = csv.DictWriter(file, fieldnames=coluna, lineterminator="\n", delimiter=';')
    escrever.writeheader()
    for nome in pokemon["abilities"]:
        escrever.writerow(
            {
                "Nome Habilidade": nome["ability"]["name"],
                "Poder": "1000"
            }
        )