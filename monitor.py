import os
from time import sleep
from telegram import telegram_bot
import configparser

# Global Vars
TIMER = 5
PATH = None
TOKEN = None
CHAT = None

def get_alert(file):
    file_path = PATH + file
    alert = None
    with open(file_path,'r') as f:
        alert = f.read()
        print(alert)
    return alert

def load_settings():
    global PATH
    global TOKEN
    global CHAT

    config = configparser.ConfigParser()
    config.read('config.ini')

    PATH = config['telegram']['path']
    TOKEN = config['telegram']['token']
    CHAT = config['telegram']['chat']

def main():

    print('\n')

    try:
        load_settings()
        print('Settings loaded')
    except Exception as e:
        print('ERROR loading telegram settings from config file!')
        print(e)
        raise

    if TOKEN and CHAT:
        bot = telegram_bot(TOKEN,CHAT)
        print('Bot initialized\n')
        bot.wake_up()
    else:
        raise Exception('ERROR initializing TOKEN or CHAT\n',
                        'TOKEN ==',TOKEN,'\n',
                        'CHAT ==',CHAT,'\n')

    if PATH:
        before = os.listdir(PATH)
        print('Current files:',before,'\n')
    else:
        raise Excption('ERROR initializing PATH varable\n',
                        'PATH ==',PATH,'\n')

    while True:
        sleep(TIMER)
        after = os.listdir(PATH)
        added = [f for f in after if f not in before]

        if len(added) > 0:
            print('Added:',added,'\n')
            for file in added:
                msg = get_alert(file)
                bot.send_message(msg)

        before = after

if __name__ == '__main__':
    main()