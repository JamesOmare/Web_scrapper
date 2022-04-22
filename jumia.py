from bs4 import BeautifulSoup
import requests
import re
import math


earpiece_product = input("What earpiece product brand are you searching for? Press 1 for options:")
if earpiece_product == "1":
    earpiece_product = input("a)Generic | b)Jbl | c)Oraimo | d)Sony | Choose Opton: ")

url = f"https://www.jumia.co.ke/electronics-headphone/{earpiece_product.lower()}/?page=1#catalog-listing"

page = requests.get(url)
doc = BeautifulSoup(page.text, "html.parser")

# prices = doc.find_all(text = 'KSh 2,790')
# # parent = prices[0].parent
# # span = parent.find('span')
# # print(span.string)

# search = doc.find_all(['span'], class_ = '-fs24')
# # print(search)

# tags = doc.find_all(text = re.compile('KSh', re.IGNORECASE), limit=5)
# for tag in tags:
#     print(tag.strip())

total_pages = doc.find(['p'], class_ = '-gy5 -phs')
total_pages = total_pages.string
total_pages = int(''.join([n for n in total_pages if n.isdigit()]))
pages = math.ceil(total_pages/48)

#the (1, pages +1) is used to find range from 1 and end at 
# the last page hence +1. Normal ranges start at zero 
for page in range(1, pages +1):
    url  = f"https://www.jumia.co.ke/electronics-headphone/{earpiece_product.lower()}/?page={page}#catalog-listing"
    page = requests.get(url)
    doc = BeautifulSoup(page.text, "html.parser")

    div = doc.find(['div'], class_ = '-pvs col12')
    items = div.find_all(['div'], class_ = 'info')
    prices = div.find_all(['div'], class_ = 'prc')

 
    earpiece_items = {}
    i = 0
    for item in items:
        parent = item.parent
        if parent.name == "a":
            link = "https://www.jumia.co.ke" + parent['href']
            name = item.h3.string
            cost = prices[i].string       
    
            earpiece_items[item] = {"name": name, "price": cost.replace(",", ""), "link": link}
            i += 1

sorted_items = sorted(earpiece_items.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
    print(f"Name: {item[1]['name']}")
    print(f"Price: {item[1]['price']}")
    print(f"Link: {item[1]['link']}")
    print("------------------------------------")


