from datetime import datetime
from discord.ext import commands
from colorama import Fore, init, Style
import requests, discord, os, unidecode, json
init()

def PrintLogo():
	os.system("cls" if os.name == "nt" else "clear")
	print(f"""{Fore.LIGHTMAGENTA_EX}
	\t\t\t\t\t╔╦╗╦╔═╗╔═╗╔═╗╦═╗╔╦╗  ═╗ ╦  ╔═╗╔╗╔╦╔═╗╔═╗╦═╗
	\t\t\t\t\t ║║║╚═╗║  ║ ║╠╦╝ ║║  ╔╩╦╝  ╚═╗║║║║╠═╝║╣ ╠╦╝
	\t\t\t\t\t═╩╝╩╚═╝╚═╝╚═╝╩╚══╩╝  ╩ ╚═  ╚═╝╝╚╝╩╩  ╚═╝╩╚═""")

PrintLogo()
token = input("Token :")

client = commands.Bot(command_prefix = "!", self_bot = True)

@client.event
async def on_ready():
    print()
    print(Fore.RED + "        \t\t\t\t\tUsername: " + Fore.RESET + client.user.name + "#" + Fore.RESET + client.user.discriminator)
    print(Fore.RED + "        \t\t\t\t\tID: " + Fore.RESET + str(client.user.id))
    print(Fore.LIGHTCYAN_EX + '        \t\t\t\t     Sniping Discord Nitro on ' + str(len(client.guilds)) + ' Servers \n' + Fore.RESET)
    print()

    
@client.event
async def on_message(message):
    if "discord.gift/" in message.content:
        code = message.content.split('discord.gift/')[1].split(' ')[0]
        r = requests.post(f"https://discord.com/api/v8/entitlements/gift-codes/{code}/redeem", headers={"authorization": token, "content-type": "application/json"}, data={"channel_id": str(message.channel.id)})
        time = datetime.now().strftime("%H:%M:%S")
        if r.status_code == 200:
            print(unidecode.unidecode(f"{Fore.GREEN}[{Fore.RESET}{time}{Fore.GREEN}]{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}Sent by {message.author} - Server {message.guild} - Status Successfully Claimed{Fore.RESET}{Style.RESET_ALL}: {code}"))
        elif r.status_code == 400:
            print(unidecode.unidecode(f"{Fore.RED}[{Fore.RESET}{time}{Fore.RED}]{Fore.RESET}{Fore.RED}{Style.BRIGHT}Sent by {message.author} - Server {message.guild} - Status Already Claimed{Fore.RESET}{Style.RESET_ALL}: {code}"))
        else:
            print(unidecode.unidecode(f"{Fore.RED}[{Fore.RESET}{time}{Fore.RED}]{Fore.RESET}{Fore.RED}{Style.BRIGHT}Sent by {message.author} - Server {message.guild} - Status Unknow Gift{Fore.RESET}{Style.RESET_ALL}: {code}"))

            
client.run(token, bot = False)
