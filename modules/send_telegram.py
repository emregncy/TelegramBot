import requests
import configparser

config = ConfigParser.ConfigParser()
config.read('config.json')
BotToken = config.get('config', 'bot_token')
ChatID = config.get('config', 'tg_chat_id')

def notis(message):
    url = f"https://api.telegram.org/bot{config.get('config', 'bot_token')}/sendMessage"
    data = {"ChatID": ChatID, "text": message}
    requests.post(url, data=data)

    send_notification("You have a new notification!")