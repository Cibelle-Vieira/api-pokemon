#bliblioteca 
import requests
from requests.api import get 

#configuração st 
host = "https://pokeapi.co/api/v2"

#conexão 
conexao = requests.get(f"{host}/pokemon/ditto")

#validação 
if conexao.status_code != 200:
    print("Deu erro")
else:
    print("Deu certo")
#operação get
pokemon = conexao.json()

for nome in pokemon ["abilities"]:
    print("nome abilidades", nome["ability"] ["name"])