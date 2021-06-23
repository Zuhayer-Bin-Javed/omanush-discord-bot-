import discord
from discord.ext import commands
import datetime


class utility(commands.Cog):

  def __init__(self,client):
    self.client=client

  @commands.Cog.listener()
  async def on_ready(self):
    print(f"logged in as {self.client.user}")


  @commands.command()
  async def ping(self, ctx):
    embed=discord.Embed(color=0x0c660a, title=f"**PONG!** **{round(self.client.latency*1000)}ms**",description=f"{ctx.author.mention} দোস্ত এই রাখ তোর PING")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

    
  @commands.command()
  @commands.has_permissions()
  async def clear(self,ctx, amt=5):
    await ctx.channel.purge(limit=amt + 1)  
    embed=discord.Embed(color=0x0c660a, title=f"**lukiye lukiye message delete kora**",description=f"{amt} messages were deleted by {ctx.message.author}")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
      
  @clear.error
  async def clear_error(self,ctx, error):
    if isinstance(error, commands.CheckFailure):
      await ctx.send(f"TOR CLEAR KORAR KHOMOTA NAI")

  @commands.command(aliases=['avatar'])
  async def dp(self,ctx, *, member: discord.Member = None):
    if not member:
      member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

  @commands.command()
  async def quit(self,ctx):
    
    return await self.client.logout()
  async def shutdown(self,ctx):
    if ctx.message.author.id == 587529076286423041: #replace OWNERID with your user id
      try:
        await ctx.send("Shutting down the bot")
        await self.bot.logout()
      except:
        print("EnvironmentError")
        self.bot.clear()
    else:
      await ctx.send("Ostad! apne ki sob korben naki")


def setup(client):
  client.add_cog(utility(client))
