import requests

url = "http://localhost:8081/message/sendText/FinanceApp"

payload = {
    "number": "5511983998794",

    "textMessage": { "text": "Teste" }
}
headers = {
    "apikey": "123456",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())