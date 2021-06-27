from datetime import datetime
from discord.ext import commands
from colorama import Fore, init, Style
import requests, unidecode
init()

def PrintLogo():
    import os as o;o.system("cls" if o.name == "nt" else "clear")
    print(f"""{Fore.LIGHTMAGENTA_EX}
\t\t\t    ╔╦╗╦╔═╗╔═╗╔═╗╦═╗╔╦╗  ═╗ ╦  ╔═╗╔╗╔╦╔═╗╔═╗╦═╗
\t\t\t     ║║║╚═╗║  ║ ║╠╦╝ ║║  ╔╩╦╝  ╚═╗║║║║╠═╝║╣ ╠╦╝
\t\t\t    ═╩╝╩╚═╝╚═╝╚═╝╩╚══╩╝  ╩ ╚═  ╚═╝╝╚╝╩╩  ╚═╝╩╚═ by XinOnGithub
        
        """)

PrintLogo()
token = input("\t[+]Token :")

client = commands.Bot(command_prefix = "!", self_bot = True)

@client.event
async def on_ready():
    PrintLogo()
    print(f"""
        {Fore.LIGHTMAGENTA_EX}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
        {Fore.LIGHTMAGENTA_EX}║                                                                                                     ║\n
        {Fore.LIGHTCYAN_EX}\t\t\tSniping Discord Nitro on {Fore.RESET}{str(len(client.guilds))}{Fore.LIGHTCYAN_EX} Servers For {Fore.RESET}{client.user.name}#{client.user.discriminator}{Fore.RESET}                                {Fore.LIGHTMAGENTA_EX}
                          ___________________________________________________________                                                \n""")

    
@client.event
async def on_message(message):
    if "discord.gift/" in message.content:
        code = message.content.split('discord.gift/')[1].split(' ')[0]
        r = requests.post(f"https://discord.com/api/v8/entitlements/gift-codes/{code}/redeem", headers={"authorization": token, "content-type": "application/json"}, data={"channel_id": str(message.channel.id)})
        time = datetime.now().strftime("%H:%M:%S")
        if r.status_code == 200:
            print(unidecode.unidecode(f"         {Fore.GREEN}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.GREEN}]{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}Sent by {message.author} - Server {message.guild} - Status Successfully Claimed{Fore.RESET}{Style.RESET_ALL}: {code}"))
        else:
            print(unidecode.unidecode(f"             {Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET}{Fore.RED}{Style.BRIGHT}Sent by {message.author} - Server {message.guild} - Status Invalid Gift{Fore.RESET}{Style.RESET_ALL}: {code}"))

            
client.run(token, bot = False)
