import requests
from bs4 import BeautifulSoup

response = requests.get('https://enter.kg/')
soup = BeautifulSoup(response.text, 'lxml')

category_items = soup.find('div', {'class':'moduletable'})


category_list = [item.text.strip() for item in category_items]

def find_category(categories:list, keyword:str):
    result = []
    for category in categories:
        if keyword.lower() in category.lower():
            result.append(category)
    return result

print(find_category(category_list, 'Ноутбуки'))



