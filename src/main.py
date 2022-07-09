import discord
from dotenv import dotenv_values

import requests
import json
import random

token = dotenv_values()['DISCORD_TOKEN']
client = discord.Client()

def get_quote():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    data = json.loads(response.text)
    return data['content']

def get_zen_quote():
    url =" https://zenquotes.io/api/random"
    response = requests.get(url)
    data = json.loads(response.text)
    return data[0]["q"] + " - " + data[0]["a"]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

COMMANDS = {
    '!quote': get_quote,
    '!zen': get_zen_quote,
}

SAD_WORDS = [ "sad",
                "depressed",
                "unhappy",
                "unamused",
                "unmotivated",
                "unfulfilled",
                "angry",
]

STARTER_ENCOURAGEMENT =["Cheer up",
                        "Be happy",
                        "Be positive",
                        "Be calm",
                        "Be patient",]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('/quote'):
        await message.channel.send(get_quote())

    if message.content.startswith('/zen_quote'):
        await message.channel.send(get_zen_quote())

    if any (word in message.content.lower() for word in SAD_WORDS):
        await message.channel.send(random.choice(STARTER_ENCOURAGEMENT))
        

client.run(token)
