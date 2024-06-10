import requests
import pprint
response = requests.get ('https://api.github.com/')
# print(response.status_code)
# if response.ok:
#     print("запрос успешно выполнен")
# else:
#     print("произошла ошибка")
#print(response.text)
response_json = response.json()
pprint.pprint(response_json)