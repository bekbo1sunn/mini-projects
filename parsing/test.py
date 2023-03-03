import requests 
from bs4 import BeautifulSoup

main_url = 'https://www.kivano.kg/'

responce = requests.get(main_url)
# print(responce.text)

soup = BeautifulSoup(responce.text, 'lxml')
# print(dir(soup))
phones_span = soup.find('span', {'id':'phones'})
row_phones = phones_span.text
phones_list = []
for phone in row_phones.split('\n'):
    clear_phone = phone.replace('r', '').strip()
    # print(clear_phone)
    if clear_phone:
        phones_list.append(clear_phone)

# print(phones_list)


product_url = 'product/view/sotovyy-telefon-apple-iphone-14-pro-256gb-fioletovyy'

responce = requests.get(main_url+product_url)
soup = BeautifulSoup(responce.text, 'lxml')

product_card = soup.find('div', {'class':'product-view oh'})

title = product_card.find('h1').text
print(title)
# print(len(product_card.find_all('img')))

image_box = product_card.find('div', {'class':'img_full addlight'})
image = image_box.find('img').get('src')
# print(image)

price = product_card.find('span', {'itemprop':'price'}).text
print(price)
database = {'title':title, 'image':image, 'price': price}
print(database)