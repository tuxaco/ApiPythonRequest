import requests
import json
api_url="https://jsonplaceholder.typicode.com/todos"
todo={"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url,json=todo)
print(response.status_code)
print(response.json())



yepa={"userId": 2, "title": "Buy Bread", "completed": False}
headers = {"Content-Type": "application/json"}
response2 = requests.post(api_url,data=json.dumps(yepa),headers=headers)
print(response2.status_code)
print(response2.json())



