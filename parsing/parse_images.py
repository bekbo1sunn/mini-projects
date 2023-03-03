import requests, json
image_url = 'https://chelseablues.ru/images/news14/228c03bf904.jpg'

response = requests.get(image_url)

with open("test.jpg", "wb") as file:
    file.write(response.content)