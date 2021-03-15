import requests
from bs4 import BeautifulSoup as bs
import os
import time

total_imgs = 0


class Clothing:
    def __init__(self, url, maxPages, folder, filename):
        self.url = url
        self.maxPages = maxPages
        self.folder = folder
        self.filename = filename


clothes = [
    Clothing(
        "https://www.redwolf.in/tees-t-shirts-india?page=",
        31,
        "tshirts",
        "/tshirt",
    ),
    Clothing(
        "https://www.redwolf.in/polo-collar-t-shirts?page=",
        2,
        "Polo Shirts",
        "/poloshirt",
    ),
    Clothing(
        "https://www.redwolf.in/full-sleeve-t-shirts-india?page=",
        2,
        "Full Sleeve Tshirts",
        "/fullsleeve",
    ),
    Clothing(
        "https://www.redwolf.in/sweatshirts-online-india?page=",
        7,
        "Sweatshirts",
        "/sweatshirt",
    ),
    Clothing(
        "https://www.redwolf.in/hooded-sweatshirts-india?page=",
        5,
        "Hoodies",
        "/hoodie",
    ),
    Clothing(
        "https://www.redwolf.in/sleeveless-t-shirts-india",
        0,
        "Sleeveless Tshirts & Tank Tops",
        "/sleeveless",
    ),
    Clothing(
        "https://www.redwolf.in/jackets-india",
        0,
        "Jackets",
        "/jacket",
    ),
    Clothing(
        "https://www.redwolf.in/boxer-shorts-online-india",
        0,
        "Boxer Shorts",
        "/boxer",
    ),
]

for num in range(len(clothes)):

    pages = clothes[num].maxPages + 1
    img_links = []

    if num < 5:

        for x in range(1, pages):
            url = clothes[num].url + str(x) + "&minimal=1&second_flag=1"

            r = requests.get(url)
            htmlContent = r.content

            soup = bs(htmlContent, "html.parser")

            img_data = soup.find_all("img", class_="cat_product_main_img")

            for i in range(0, len(img_data)):
                img_links.append(img_data[i].attrs["src"])

    else:

        url = clothes[num].url
        r = requests.get(url)
        htmlContent = r.content

        soup = bs(htmlContent, "html.parser")

        img_data = soup.find_all("img", class_="cat_product_main_img")

        for i in range(0, len(img_data)):
            img_links.append(img_data[i].attrs["src"])

    total_imgs = total_imgs + len(img_links)

    FOLDER = clothes[num].folder

    if not os.path.exists(FOLDER):
        os.mkdir(FOLDER)

    for i, img_link in enumerate(img_links):
        response = requests.get(img_link)

        img_name = FOLDER + clothes[num].filename + str(i + 1) + ".jpg"
        with open(img_name, "wb") as file:
            file.write(response.content)

    print(FOLDER, "done. Images downloaded: ", len(img_links))
    time.sleep(2)

print("Total images downloaded: ", total_imgs)