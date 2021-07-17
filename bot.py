import asyncio
import logging
import os
import sys
import aiogram
import time
import data
import scapers
import json


bot = aiogram.Bot(token=data.TOKEN)

dp = aiogram.Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def start_command(message):
    await bot.send_message(message.chat.id, "Привет! Давай скрапить каналы. /help для полной информации")

@dp.message_handler(commands=['help'])
async def start_command(message):
    await bot.send_message(message.chat.id, "/help - полная информация \n"
                                            " /add - добавить канал \n"
                                            " /remove - исключить канал, \n"
                                            " /go - ищем видео \n")

@dp.message_handler(commands=['add'])
async def start_command(message):
    data.adding_flag = 1
    await bot.send_message(message.chat.id, "Пришли ссылку на страницу с видео канала (вкладка \"Видео\")."
                                            " \"back\" для отмены действия добавления или удаления канала")

@dp.message_handler(commands=['remove'])
async def start_command(message):
    data.removing_flag = 1
    await bot.send_message(message.chat.id, "Пришли название канала или ссылку на канал, который ты хочешь исключить"
                                            " \"back\" для отмены действия добавления или удаления канала")


@dp.message_handler(commands=['go'])
async def start_command(message):
    r = open("YT.json")
    str = r.read()
    YT = json.loads(str)
    r.close()
    for channel in YT:
        try:
            await scapers.scrap(channel, YT[channel])
        except:
            pass

    if len(data.final_data) == 0:
        await bot.send_message(message.chat.id, "Новых видео не было", parse_mode=aiogram.types.ParseMode.MARKDOWN)
    else:
        for i in range(len(data.final_data)):
            try:
                await bot.send_message(message.chat.id, data.final_data[i], parse_mode=aiogram.types.ParseMode.MARKDOWN)
            except:
                pass

    data.final_data.clear()


@dp.message_handler(content_types=['text'])
async def send_text(message):
    if message.text == "back":
        data.adding_flag = 0
        data.removing_flag = 0
        await bot.send_message(message.chat.id, "Отмена")
    elif data.adding_flag:
        if message.text.find("https://www.youtube.com/") != -1:
            await scapers.add_channel(message.text)
        else:
            await bot.send_message(message.chat.id, "Некорректные данные. вот пример: https://www.youtube.com/user/psychodozerLive")
        data.adding_flag = 0
        await bot.send_message(message.chat.id, "Сделано")
    elif data.removing_flag:
        if message.text.find("https://www.youtube.com/") != -1:
            await scapers.remove_channel(await scapers.find_name(message.text))
        else:
            r = open("YT.json")
            str = r.read()
            YT = json.loads(str)
            r.close()
            if YT.get(message.text) is None:
                await bot.send_message(message.chat.id, "Такого канала нет в моем списке")
            else:
                await scapers.remove_channel(message.text)
        data.adding_flag = 0
        await bot.send_message(message.chat.id, "Сделано")
    else:
        await bot.send_message(message.chat.id, "Даже не знаю, что сказать...")


def main():
    # Запуск бота
    aiogram.executor.start_polling(dp, skip_updates=True)
