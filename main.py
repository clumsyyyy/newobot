from stay import keep_alive
from replit import db
from datetime import datetime
from pytz import timezone
from discord.ext import commands
import discord
import os
import requests
import json
import random

sadge_words = ["i live in spain but the s is silent", "sometimes we forget to tandai hadir and thats okay", "sometimes we have bad days and thats okay, better days are upon us", "hey sometimes you just gotta take a nap and forget it all", "it's fine to not be fine", "hey at least you're not mentally deranged or actually mentally retarded, man. thats an advantage.", "thirafi had secc with amar at room 219", "mending nonton boku no pico :v - benis", "if u ever feel like shit remember that thirafi got denied by an AI. A FUCKIN AI.", "pls go to horny jail. pls.", "KONPEKO KONPEKO KONPEKO HOLOLIVE SAN-KISEI NO USADA PEKORA PEKO DO A~ MO DO A~ MO DO A~ WAAAAAAAAAAAAAAAAAAA AH↓HA↑HA↑HA↑"]

rps = ["rock", "paper", "scissors", "M4A1-S", "a gun", "Hitler", "a frog", "a plate", "an unit of RT-2PM2 Topol-M Cold-Launched Three-Stage Solid-Propellant Silo-Based Intercontinental Ballistic Missile", "a main battle tank"]

yes_or_no = ["yes", "no", "prolly", "idk man im only a bot pepehands", "let's just agree to disagree, man", "let's just disagree to agree", "I would like to agree, but for the sake of papa Stalin, I won't", "y e s", "n o", "wait what?", "uhhhhhhhhhhhhhhhhhhhhhhhhh yes", "uhhhhhhhhhhhhhhhh no?", "I would like to agree, but agreeing will be based"]

date = datetime.now()
client = discord.Client()
channel = client.get_channel(758682366264082487)

def quoting():
  res = requests.get("https://zenquotes.io/api/random")
  jsondata = json.loads(res.text)
  quote = jsondata[0]['q'] + " -" + jsondata[0]['a']
  return quote

def addwisdom(mssg):
  if "sadge_words" in db.keys():
    wisdom = db["sadge_words"]
    wisdom.append(mssg)
    db["sadge_words"] = wisdom
  else:
    db["sadge_words"] = [mssg]
  
def addsuit(mssg):
  if "rps" in db.keys():
    suit_ops = db["rps"]
    suit_ops.append(mssg)
    db["rps"] = suit_ops
  else:
    db["rps"] = [mssg]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):

    options = sadge_words
    if "sadge_words" in db.keys():
      options = options + db["sadge_words"]

    suit = rps
    if "rps" in db.keys():
      suit = suit + db["rps"]

    if message.author == client.user:
        return
    if message.content.startswith('hello newo'):
        await message.channel.send('hello i am newo')
    if message.content.startswith('newo wisdom'):
        await message.channel.send(random.choice(options))
    if message.content.startswith('newo kerang ajaib'):
        await message.channel.send(random.choice(yes_or_no))
    if message.content.startswith('newo suit'):
        await message.channel.send("I choose {}".format(random.choice(suit)))
    if message.content.startswith('newo date'):
        await message.channel.send(date)
    if message.content.startswith('newo motivate'):
        await message.channel.send(quoting())
    if message.content.startswith("newo add wisdom"):
        wisdom1 = message.content.split("newo add wisdom ", 1)[1]
        addwisdom(wisdom1)
        options = options + db["sadge_words"]
        await message.channel.send("wisdom added ezclap")
    if message.content.startswith("newo add suit"):
        suit1 = message.content.split("newo add suit ", 1)[1]
        print(suit1)
        addsuit(suit1)
        suit = suit + db["rps"]
        await message.channel.send("suit option added ezclap")
    if message.content.startswith('newo help'):
        await message.channel.send("```NewoBot by Newo \n\n TBH I don't know yet what this bot does so right now it's a meme \n\n \n -hello newo = it'll reply \n -newo wisdom = say something weird  \n -newo kerang ajaib = ask a question with this as the beginning and it'll reply \n -newo suit <insert option> = a simple suit game I guess. Let's just see how good you are vs a bot \n -newo add wisdom <insert wisdom> = add a wisdom to the database \n -newo add suit <insert option> = add a suit option to the database ```")

keep_alive()
client.run(os.getenv('TOKEN'))
