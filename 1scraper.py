import requests
from bs4 import BeautifulSoup
from word2number import w2n
import csv
from time import sleep

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

def get_url():
    
    for count  in range(1, 4):
        print(f"page {count}\n")
        site=f"https://books.toscrape.com/catalogue/page-{count}.html"
        response = requests.get(site,headers=headers)

        answer = BeautifulSoup(response.text, "lxml")

        data = answer.find_all("li", class_= "col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for i in data:
            link = "https://books.toscrape.com/catalogue/" + i.find("a").get("href")
            yield link
        try:
            waytonext = answer.find("li", class_="next")
            next = waytonext.find("a").get("href")
            page_next="https://books.toscrape.com//" + next
        except AttributeError:
            print("end")
            break
n=0
def array():
    for link in get_url():
        sleep(1)
        response = requests.get(link,headers=headers)

        answer = BeautifulSoup(response.text, "lxml")
        data = answer.find("article", class_="product_page")
        #title = data.find("div", class_="col-sm-6 product_main").text
        price = data.find("p", class_="price_color").text.replace("Â", "")
        stock = data.find("p", class_="instock availability").text.replace(" ", "").replace("\n", "")
        img = "https://books.toscrape.com/" + data.find("img").get("src")
        description_tag = answer.select_one('div#product_description ~ p')
        no_title = data.find("div", class_="col-sm-6 product_main")
        title = no_title.find("h1").text
        if description_tag:
            description_text = description_tag.text
        rateStr = data.find("p", class_="star-rating").get("class")[1]
        rate=w2n.word_to_num(rateStr)

        yield title, price, stock, img, rate, link, description_text
        
    
    
