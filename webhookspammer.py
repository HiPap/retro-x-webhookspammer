from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from colorama import Fore
import os


os.system('cls & title Webhook X by HiPapi')


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


    while True:
     webhook = DiscordWebhook(url=link, content=message, rate_limit_retry=True)
     time.sleep(3)
     response = webhook.execute()
     print(Fore.CYAN + 'Spamming webhook....')

 except:
      print(Fore.CYAN + 'Webhook has been deleted, try again!')
      MainMenu()
MainMenu()

