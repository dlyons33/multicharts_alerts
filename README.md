# multicharts_alerts
Monitors for alerts from Multicharts and pushes through telegram

With a PowerLanguage indicator or signal script:  
Upon a condition you wish to receive alerts (if ... then begin ... end;)  
Use: Print(<path>,<message>) to save a txt file to a set directory (path) with a given message (message).

Create a config.cfg file with the following parameters:

[telegram]  
token=  
chat=  
path=  

token: your bot token generated by BotFather in Telegram  
chat: the channel or user chat id # (who you want to send the message to)  
path: the directory where you are printing the alert messages to with PowerLanguage script  

*Note: do not use quotations when setting the parameters in config.cfg