# Name

import discord

from colorama import init, Style
from colors import color # setup the colors in colors.py [ ]


client = discord.Client()
init(autoreset=True)
TOKEN = open('token.txt', 'r').read() # input token [ ]
welcome = open('welcome.txt', 'r') # input welcome message [ ]
prefix = ' ' # input prefix [ ]


for line in welcome: print(color[0] + Style.BRIGHT + line, end="")
print()


@client.event
async def on_ready():
    print(f"{color[1] + Style.BRIGHT}bot is ready ~")

@client.event
async def on_connect():
    print(f"{color[1] + Style.BRIGHT}bot is connected to discord ~")
    activity = discord.Activity(name=f'{prefix}help', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

@client.event
async def on_disconnect():
    print(f"{color[2] + Style.BRIGHT}bot has disconnected from discord ~")

@client.event
async def on_message(message):
    if message.content.lower() == (f'{prefix}ping'):
        print(f"{color[0] + Style.BRIGHT + message.author.name + Style.NORMAL + color[0]} pinged the bot.")
        await message.channel.send("pong")
    elif message.content.lower() == (f'{prefix}help'):
        print(f"{color[0] + Style.BRIGHT + message.author.name + Style.NORMAL + color[0]} asked for help.")
        await message.channel.send("HELP!")

client.run(TOKEN)
TOKEN.close()
welcome.close()