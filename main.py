import discord
import logging 
from discord.ext import commands
from dotenv import load_dotenv
import os
import datetime
import requests
import json 


activity = discord.Activity(type=discord.ActivityType.watching, name=" for দামে কম মানে ভাল discord ব্যবহারকারীগণ")

intents = discord.Intents.default()
intents.members = True

#time format
date_format="%d %b %Y %H:%M:%S"
timestamp = datetime.datetime.now()

#chanel ids
welcome_channel=843792330129670156
react1_channel=843792330619879425
react2_channel=843792330619879429
#role ids
oshadharon_role=848556720761602088

joining_time=discord.Member.joined_at

client = commands.Bot(command_prefix=['.','omanush '], activity=activity, status=discord.Status.do_not_disturb, intents=intents)


def get_quote():
  respose=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(respose.text)  
  quote= json_data[0]["q"]+" -"+json_data[0]["a"]
  return(quote)
quote=get_quote()  

@client.command()
async def load(ctx,extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
  client.unload_extension(f'cogs.{extension}')

async def on_ready():
  print(f"logged in as {client.user}")

  
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f"cogs.{filename[:-3]}")
  
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



load_dotenv('.env')

client.run(os.getenv('bot_token'))