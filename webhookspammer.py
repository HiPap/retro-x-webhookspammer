from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from colorama import Fore
import os


os.system('cls & title Webhook X by HiPapi, optimised by kelpdude89')


def MainMenu():
 print(Fore.CYAN + '''

 ____     ___ ______  ____   ___       __ __ 
|    \   /  _]      ||    \ /   \     |  |  |
|  D  ) /  [_|      ||  D  )     |    |  |  |
|    / |    _]_|  |_||    /|  O  |    |_   _|
|    \ |   [_  |  |  |    \|     |    |     |
|  .  \|     | |  |  |  .  \     |    |  |  |
|__|\_||_____| |__|  |__|\_|\___/     |__|__|


                                                                        
''')


 try:
    link = input(Fore.CYAN + 'Enter your Webhook $ ')
    message = input(Fore.CYAN + 'Enter your webhook content $ ')
    message_number = input("how many messages would you like to send? ('i' for infinite) $ ") #* added options for how long you want the spam to last
    delay = float(input("How long do you want the delay between messages (in seconds) $ "))

    if message_number == 'i':
        while True: #* controls infinite spam
            webhook = DiscordWebhook(url=link, content=message, rate_limit_retry=True)
            time.sleep(delay) #* changed delay from 3 to user input
            response = webhook.execute()
            print(Fore.CYAN + 'Spamming webhook....')
    else:
        for i in range(int(message_number)): #* controls numbered spam
            webhook = DiscordWebhook(url=link, content=message, rate_limit_retry=True)
            time.sleep(delay) #* changed delay from 3 to user input
            response = webhook.execute()
            print(Fore.CYAN + 'Spamming webhook....')
        MainMenu()

 except:
      print(Fore.CYAN + 'Webhook has been deleted, try again!')
      MainMenu()

MainMenu()

