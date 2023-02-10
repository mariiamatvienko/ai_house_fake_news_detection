import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import re
from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


URL = "https://rusdisinfo.voxukraine.org/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

categories = soup.find_all("h2")

links = soup.find_all("div", class_="Home_container__bCOhY")

categories_lst = [category.text.strip("#") for category in categories]

texts_all = [ ]

for link in links:

        url_link = link.find_all("a")
        for path in url_link:
            certain_category = []

            # print(path["href"])
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-blink-features=AutomationControlled")
            driver = webdriver.Chrome(executable_path=r'path\to\chromedriver.exe', options=options)

            URL_next = f"https://rusdisinfo.voxukraine.org{path['href']}"
            print("url:", URL_next)

            match = re.search("narratives/", URL_next)
            if match:
                res = URL_next[match.end():]
                if res != "":

                    driver.get(URL_next)

                    soup = BeautifulSoup(driver.page_source, "html.parser")

                    text_in_categories = soup.find_all("div", class_= "Narrative_container__nU4Ms")

                    for cat in text_in_categories:
                        texts = cat.find_all("h3")
                        for text in texts:
                            print(text.text)
                            certain_category.append(text.text)
                    texts_all.append(certain_category)


# texts_all = list(list(map(str.strip, x)) for x in texts_all)
categories_lst = list(map(str.strip, categories_lst))

@app.route('/')
def home():             # return all categories names
    res = ''
    for category_name_ in categories_lst:
        res += '<br>' + category_name_ + '</br>'

    return res



@app.route("/" + categories_lst[0])
def page_0():
    records = texts_all[0]
    return render_template("template_fake_news.html", len = len(records), records = records)


@app.route("/" + categories_lst[1])
def page_1():
    records = texts_all[1]
    return render_template("template_fake_news.html", len = len(records), records = records)



@app.route("/" + categories_lst[2])
def page_2():
    records = texts_all[2]
    return render_template("template_fake_news.html", len = len(records), records = records)


@app.route("/" + categories_lst[3])
def page_3():
    records = texts_all[3]
    return render_template("template_fake_news.html", len = len(records), records = records)


@app.route("/" + categories_lst[4])
def page_4():
    records = texts_all[4]
    return render_template("template_fake_news.html", len = len(records), records = records)


@app.route("/" + categories_lst[5])
def page_5():
    records = texts_all[5]
    return render_template("template_fake_news.html", len = len(records), records = records)


@app.route("/" + categories_lst[6])
def page_6():
    records = texts_all[6]
    return render_template("template_fake_news.html", len = len(records), records = records)

@app.route("/" + categories_lst[7])
def page_7():
    records = texts_all[7]
    return render_template("template_fake_news.html", len = len(records), records = records)

@app.route("/" + categories_lst[8])
def page_8():
    records = texts_all[8]
    return render_template("template_fake_news.html", len = len(records), records = records)

@app.route("/" + categories_lst[9])
def page_9():
    records = texts_all[9]
    return render_template("template_fake_news.html", len = len(records), records = records)


@app.route("/" + categories_lst[10])
def page_10():
    records = texts_all[10]
    return render_template("template_fake_news.html", len = len(records), records = records)


@app.route("/" + categories_lst[11])
def page_11():
    records = texts_all[11]
    return render_template("template_fake_news.html", len = len(records), records = records)


@app.route("/" + categories_lst[12])
def page_12():
    records = texts_all[12]
    return render_template("template_fake_news.html", len = len(records), records = records)


app.run()