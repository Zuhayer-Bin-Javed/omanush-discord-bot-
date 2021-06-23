import discord
from discord.ext import commands
import datetime

#time format
date_format="%d %b %Y %H:%M:%S"
timestamp = datetime.datetime.now()
#chanel ids
welcome_channel=843792330129670156
react1_channel=843792330619879425
react2_channel=843792330619879429
#role ids
oshadharon_role=848556720761602088

class add_react(commands.Cog):

  def __init__(self,client):
    self.client=client

  @commands.Cog.listener()
  
  async def on_message(self,message):
    if message.channel.id == react1_channel or message.channel.id == react2_channel :
      await message.add_reaction('\N{Sparkling Heart}')
      await message.add_reaction('\N{Revolving Hearts}')
      await message.add_reaction('\N{Beating Heart}')
      await message.add_reaction('\N{Heart with Arrow}')
      await message.add_reaction('\N{Heart with Ribbon}')
      print(f"added reaction on {message.channel} and message by {message.author} on {timestamp.strftime(date_format)} ")
    

def setup(client):
  client.add_cog(add_react(client))
