import discord
from discord.ext import commands

class ping(commands.Cog):

  def __init__(self,client):
    self.client=client

  @commands.Cog.listener()
  async def on_guild_join(self,guild):
    guild1=guild.id
    channel =self.client.get_guild(guild1).system_channel
    if channel is not None:
      embed=discord.Embed(title=f"Working with {len(self.client.guilds)} servers",
      description=f"Happy to work with {guild.name}")
      embed.add_field(name=f"Big shoutout to {guild.owner.name} for adding me up",value="You guys are awsome!!!")
      embed.set_image(url=self.client.user.avatar_url)
      await channel.send(embed=embed) 

  #@commands.command() for command


def setup(client):
  client.add_cog(ping(client))
