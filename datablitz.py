import requests, json, math
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

glob_url = f'https://ecommerce.datablitz.com.ph/collections/nintendo-switch'
glob_web = requests.get(glob_url)
glob_doc = doc = BeautifulSoup(glob_web.text, 'html.parser')

display_page, page = 24, 3103

consolidated_list = []

total = math.ceil(page/display_page) + 1

pbar = tqdm(total=total)


for i in range(1, total):

    pbar.update()

    url = f'https://ecommerce.datablitz.com.ph/collections/nintendo-switch?page={i}'

    web = requests.get(url)

    doc = BeautifulSoup(web.text, 'html.parser')

    product = doc.find_all(class_='product-item__title text--strong link')
    price = doc.find_all(class_='product-item__price-list price-list')
    stock = doc.find_all(string=['Add to cart', 'Sold out'])

    for product, price, stock in zip(product, price, stock):
        dict = {'product_name':product.string, 'price': list(price)[0].string, 'availability':stock.string}

json_nsw = json.dumps(consolidated_list)