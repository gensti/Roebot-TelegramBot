import requests
import datetime
from time import sleep
import random
import json
botToken = "Fill in here your Telegram-Bot-Token"
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
#BOT-TOKEN!
global requestURL
global offset
offset = 0
datelist = []
x = 0
y = 0

requestsURL = "http://api.telegram.org/bot" + botToken+ "/getUpdates"
sendURL = "http://api.telegram.org/bot" + botToken+ "/sendMessage"

def update(url):
    global offset
    try:
        update_raw = requests.get(url +"?offset=" +str(offset))
        update = update_raw.json()
        final_result = extract_results(update)
        if final_result != False:
            offset = final_result['update_id'] +1
            text = final_result['message']['text']
            text.lower()
            chatId = final_result['message']['chat']['id']
            username = final_result['message']['chat']['username']
            make_message(text,username,chatId)
    except requests.exceptions.ConnectionError:
        print("Current date and time: ", datetime.datetime.now())
        pass

def extract_results(dict):
    resultArray = dict['result']

    #result_dic = resultArray[0]

    if resultArray == []:
        return False
    else:
        result_dic = resultArray[0]
        return result_dic

def make_message(text,username,chatId,):
    text_tmp = text
    text_tmp = text_tmp.lower()


    def get_answer(text_input):
        try:
            switcher = {
                "/start": f'Willkommen, {username} !! \n Ich bin Roe, ein Telegram-Bot.\n Gib "/befehle" für alle Befehle ein!'
                          f'\n ',
                "/befehle": 'Folgende Befehle gibt es: \n "würfeln" um zu Würfeln \n "flipcoin" um eine Münze zu werfen',
                "/würfeln": f'Der Würfel hat entschieden: {random.randint(1, 6)}',
                "/flipcoin":f'Du wirfst eine Münze! Sie fällt auf: {flip_coin()}',
            }
            output = switcher[text_input]
            send_message(chatId, output)
            return switcher.get(text_input)
        except:True
    get_answer(text_tmp)


def flip_coin():
    if random.randint(1, 2) == 1:
        flipcoin = "Kopf"
    else:
        flipcoin = "Zahl"
    return flipcoin

def megawurf(x, y):
   return random.randint(x, y)

def send_message(chatId, message):
    requests.post(sendURL +"?chat_id=" +str(chatId) +"&text=" +message)







while True:
    update(requestsURL)
    sleep(1)
