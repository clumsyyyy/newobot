import discord
import os
import random
from datetime import datetime
from discord.ext import commands
date = datetime.now()
client = discord.Client()
channel = client.get_channel(758682366264082487)

sadge_words = ["i live in spain but the s is silent", "sometimes we forget to tandai hadir and thats okay", "spain is spainus", "PEKOPEKOPEKOPEKOPEKO", "sometimes we have bad days and thats okay, better days are upon us", "hey sometimes you just gotta take a nap and forget it all", "it's fine to not be fine", "hey at least you're not mentally deranged or actually mentally retarded, man. thats an advantage."]
yes_or_no = ["yes", "no", "prolly"]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello newo'):
        await message.channel.send('hello i am newo')
    if message.content.startswith('newo wisdom'):
        await message.channel.send(random.choice(sadge_words))
    if message.content.startswith('newo kerang ajaib'):
        await message.channel.send(random.choice(yes_or_no))
    if message.content.startswith('newo help'):
        await message.channel.send("```TBH I don't know yet what this bot does \n\n newo wisdom = say something weird \n hello newo = it'll reply \n\n newo kerang ajaib = ask a question with this as the beginning and it'll reply```")



client.run(os.getenv('TOKEN'))
