import requests, json, math, locale, re
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import numpy as np

glob_url = f'https://ecommerce.datablitz.com.ph/collections/nintendo-switch'
glob_web = requests.get(glob_url)
glob_doc = doc = BeautifulSoup(glob_web.text, 'html.parser')

display_page, nsw_page = 24, 24#3103

consolidated_list = []

total = math.ceil(nsw_page/display_page) + 1

#pbar = tqdm(total=total-1)

for i in range(1, total):

    #pbar.update()

    url = f'https://ecommerce.datablitz.com.ph/collections/nintendo-switch?page={i}'

    web = requests.get(url)

    doc = BeautifulSoup(web.text, 'html.parser')

    product = doc.find_all(class_='product-item__title text--strong link')
    price = doc.find_all(class_='product-item__price-list price-list')
    stock = doc.find_all(string=['Add to cart', 'Sold out'])

    for product, price, stock in zip(product, price, stock):
        raw_dict = {'product_name':product.string, 'price': list(price)[0].string, 'availability': stock.string}
        consolidated_list.append(raw_dict)

# Convert into dataframe so perform data transformation

df = pd.json_normalize(consolidated_list)

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') # setting up locale to convert string with ##,###.00 format
df['price'] = df['price'].str.replace('₱','').apply(locale.atof).astype(float) # converting price string to float

df['availability'] = np.where(df['availability'].str.lower() == 'add to cart', 'In stock', 'Sold out')

def region_check(self):
    if re.search(r'\(mde', self.lower()):
        return 'MDE'
    elif re.search(r'\(us', self.lower()):
        return 'US'
    elif re.search(r'\(eu', self.lower()):
        return 'EU'
    elif re.search(r'\(jpn', self.lower()):
        return 'JPN'
    elif re.search(r'\(asian', self.lower()):
        return 'Asian'
    elif re.search(r'\(au', self.lower()):
        return 'AU'
    else:
        return 'Not Specified'

df['region'] = df['product_name'].apply(region_check)

def specification_check(self):

    accessories = ['thumbstick',
                   'cover',
                   'card',
                   'case',
                   'analog',
                   'protector'
                   ]

    if any(re.search(accessories, self.lower()) for accessories in accessories):
        return 'Accessories'
    else:
        return 'Game'

df['product_category'] = df['product_name'].apply(specification_check)

data_nsw = df.to_json(orient='records')

print(data)