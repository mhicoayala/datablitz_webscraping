## About
This is a simple script to scrape data from the official ecommerce website of Datablitz, a one stop shop for games and multimedia here in the Philippines, dump it into json format and put it in a simple Flask API. This is written in Python using the following libraries:
* beautifulSoup4 == 4.12.0
* Flask == 2.2.3
* numpy == 1.24.2
* pandas == 1.5.3
* requests == 2.28.2
* tqdm == 4.65.0

## Dataset
The data that I've extracted at the moment contains three features:
```json
{
"product_name": "NSW POKEMON LEGENDS ARCEUS (MDE)",
"price": 2459,
"availability": "Add to Cart",
}
```

## Updates
* 2023-03-24 | Initial commit is scraping only data on Nintendo Switch related items. More platforms will be added soon.
* 2023-03-25 | Added two new features: region and product_category:
```json
{
"region": "MDE",
"product_category": "Game"
}
```
