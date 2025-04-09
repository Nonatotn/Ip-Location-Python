import requests

api_ip = "https://api.ipify.org?format=json"
api_localizacao = "https://ipinfo.io/{}/geo"

try:
 
    print("Buscando IP...")
    resposta_ip = requests.get(api_ip)
    resposta_ip.raise_for_status()  
    ip_objeto = resposta_ip.json()
    ip = ip_objeto["ip"]

 
    url_localizacao = api_localizacao.format(ip)
    print("Buscando localização...")
    resposta_localizacao = requests.get(url_localizacao)
    resposta_localizacao.raise_for_status()
    localizacao = resposta_localizacao.json()

   
    print("Resposta:")
    print(f"\tCidade: {localizacao.get('city', 'N/A')}")
    print(f"\tEstado: {localizacao.get('region', 'N/A')}")
    print(f"\tPaís: {localizacao.get('country', 'N/A')}")
    print(f"\tLat e Lon: {localizacao.get('loc', 'N/A')}")
    print(f"\tCEP: {localizacao.get('postal', 'N/A')}")
    print(f"\tTimezone: {localizacao.get('timezone', 'N/A')}")

except requests.exceptions.RequestException as e:
    print(f"Erro ao realizar a requisição: {e}")
except KeyError as e:
    print(f"Erro ao acessar os dados da resposta: {e}")