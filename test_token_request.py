import requests

url = "http://127.0.0.1:8000/solve/token"

payload = {
    "website_url": "https://demo.turnstile.workers.dev/",
    "sitekey": "1x00000000000000000000AA",  # тестовый sitekey
    "action": "login",
    "cdata": "",  # можно оставить пустым
    "pagedata": "",  # тоже пусто
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36"
}

response = requests.post(url, json=payload)

print("=== Ответ от решальщика ===")
print("Status:", response.status_code)
print("Body:", response.json())
