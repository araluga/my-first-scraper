import requests
from bs4 import BeautifulSoup
from word2number import w2n
import csv



for count  in range(1, 1000):
    print(f"page {count}\n")
    site=f"https://books.toscrape.com/catalogue/page-{count}.html"
    response = requests.get(site)

    answer = BeautifulSoup(response.text, "lxml")


    data = answer.find_all("li", class_= "col-xs-6 col-sm-4 col-md-3 col-lg-3")


    for i in data:
        title = i.find("h3").text
        price = i.find("p", class_="price_color").text.replace("Â", "")
        stock = i.find("p", class_="instock availability").text.replace(" ", "").replace("\n", "")
        img = "https://books.toscrape.com/" + i.find("img", class_="thumbnail").get("src")

        rateStr = i.find("p", class_="star-rating").get("class")[1]
        rate=w2n.word_to_num(rateStr)

        print(f"name - {title} \nprice - {price} \nstock - {stock} \nimg - {img} \nrate - {rate} stars\n")
        
    
    try:
        waytonext = answer.find("li", class_="next")
        next = waytonext.find("a").get("href")
        page_next="https://books.toscrape.com//" + next
    except AttributeError:
        print("конец")
        break
    
    