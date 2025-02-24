import requests
try:
    response = requests.get("https://vnexpress.net")
    if response.status_code != 200:
        print("Service Down Alert!")
except Exception as e:
    print("Service Unreachable!")