import requests

URL = "https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"


def buscar_cotacao(moeda="USD"):
    resposta = requests.get(URL.format(moeda=moeda), timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()[f"{moeda}BRL"]
    return float(dados["bid"])