import requests
api_url="https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}

response = requests.get(api_url)

print(response.status_code)
print(response.json())

response = requests.patch(api_url, json=todo)

print(response.status_code)
print(response.json())
