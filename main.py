import discord
import os
import re
from discord.ext import commands
from pprint import pprint
from keep_alive import keep_alive
banned = ['pop', 'dö', 'auschwitz', 'fan', 'kaka', 'jesus', 'satan', 'aids', 'tjock', 'feting', 'tack', 'varsågod', 'neger', 'nibba', 'hoe',':hyperxd:', 'kalle', 'bög', 'Olouf ']

words_re = re.compile("|".join(banned))
client = discord.Client()
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
@client.event
async def on_message(message):
    print(message.author,": ", message.channel)
    print()
    if message.author != client.user:
      if words_re.search(message.content.lower()):
        await client.send_message(message.channel, "Det var ju inte  så bra, Sådär får man inte säga. Var snäll med andra")

      if "!bannade" in message.content.lower():
        await client.send_message(message.channel, "Dessa är de bannade orden:")
        str1 = "\n".join(banned)
        await client.send_message(message.channel, str1)

      if "!alive" in message.content.lower():
        await client.send_message(message.channel, "Tror du verkligen jag kunde svara om jag var död")

      if "!spel1" in message.content.lower():
        await client.send_message(message.channel, "Tror du verkligen jag kunde svara om jag var död")

      if "!spel" in message.content.lower():
        await client.change_presence(game=discord.game(name=message.content.strip('!spel')))
keep_alive()
token = "NTIxMjY0ODY4OTI2NTU0MTEy.DzRZHg.fUkZqsMZsIxq5-BiPbjdkGlH6Nw"
client.run(token)
