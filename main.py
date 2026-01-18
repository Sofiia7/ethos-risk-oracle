import requests

def check_reputation(solana_address):
    # Запрос к API Ethos для проверки кошелька
    url = f"https://api.ethos.network/profile/address/{solana_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            score = response.json().get('score', 1200)
            print(f"Address: {solana_address} | Ethos Score: {score}")
            return score
    except:
        return 1200

# Пример проверки создателя пула Meteora
check_reputation("CREATOR_ADDRESS_HERE")
