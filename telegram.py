import requests

class telegram_bot():
    '''
    token: controls the bot
    chat: ID for recipient user or channel
    '''

    def __init__(self,token,chat):
        self.base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat}&text='

    def send_message(self,msg):
        if msg is not None:
            url = self.base + msg
            requests.get(url)
            print('Sent message:\n',msg,'\n')

    def wake_up(self):
        msg = 'Initializing Multicharts alert monitor... Get that bread!'
        url = self.base + msg
        requests.get(url)
        print('Sent wakeup message:\n',msg,'\n')