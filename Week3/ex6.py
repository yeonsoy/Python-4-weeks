import requests

url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json"

res = requests.get(url)
print(res.json())