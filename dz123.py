import requests
import pprint

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title":"too",
    "body":"bar",
    "user":1
}

response = requests.post(url, data=data)

print(response.status_code)
print (f"содержимое ответа - {response.json()}")
