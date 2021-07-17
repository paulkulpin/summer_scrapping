import logging
from aiogram import Bot, Dispatcher, types
import lxml
import asyncio
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
import data
import json

async def scrap(name, url):

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get(url)
    html = driver.page_source
    html_soup = BeautifulSoup(html, "html.parser")


    links = html_soup.findAll("a", {"id": "video-title"})
    #print(links)
    for i in range(3):

        video_name = links[i].contents[0]

        info = links[i].attrs["aria-label"]

        pos = info.find(data.keywords["Author"])
        pos += len(data.keywords["Author"]) + 1 + len(name) + 1

        ago = info.find(data.keywords["ago"])
        time = info[pos:ago - 1].split()

        video_url = "https://www.youtube.com" + links[i].attrs["href"]

        if time[1] in data.time_ago:
            data.final_data.append("**" + video_name + "**" + "\n" + name + "\n" + video_url)
            #print(final_data[-1])
    driver.close()


async def find_name(url):
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get(url)
    html = driver.page_source
    html_soup = BeautifulSoup(html, "html.parser")

    name = html_soup.find("div", {"class": "style-scope ytd-channel-name"}).text.split()
    driver.close()
    return name[0]

async def add_channel(url):
    name = await find_name(url)
    #name = "Fenya"
    r = open("YT.json")
    str = r.read()
    YT = json.loads(str)
    #print(YT["Fenya"])
    r.close()

    YT[name] = url
    #print(YT[name])

    w = open("YT.json", 'w')
    str = json.dumps(YT)
    w.write(str)
    w.close()


async def remove_channel(name):
    r = open("YT.json")
    str = r.read()
    YT = json.loads(str)
    print(YT["Fenya"])
    r.close()

    YT.pop(name)

    w = open("YT.json", 'w')
    str = json.dumps(YT)
    w.write(str)
    w.close()

#
# async def main():
#     #polling_task = asyncio.create_task(dp.start_polling())
#     await add_channel("https://www.youtube.com/user/Wylsacom/videos")
#
#
# loop = asyncio.get_event_loop()
# if __name__ == '__main__':
#     loop.run_until_complete(main())
#     loop.close()
