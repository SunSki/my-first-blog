import random
import requests
from bs4 import BeautifulSoup as bs

def get_image_url():
    page = random.randint(1, 10)
    url = "https://pixabay.com/ja/images/search/person/?cat=nature&pagi=" + str(page)
    images = []
    response = requests.get(url)
    soup = bs(response.text, "lxml")
    images = soup.find_all("img")
    while True:
        image_id = random.randint(0,99)
        img = images[image_id]
        img_url = img.get("data-lazy")
        if img_url is not None:
            break
    return img_url

