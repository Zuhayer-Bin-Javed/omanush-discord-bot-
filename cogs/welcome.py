import discord
from discord.ext import commands
import datetime
import requests
import DiscordUtils
from PIL import Image,ImageFont,ImageDraw

#chanel ids
welcome_channel=843792330129670156
react1_channel=843792330619879425
react2_channel=843792330619879429
#role ids
oshadharon_role=848556720761602088


#time format
date_format="%d %b %Y %H:%M:%S %z"
timestamp = datetime.datetime.now()

class welcome(commands.Cog):

  def __init__(self,client):
    self.client=client
    self.tracker = DiscordUtils.InviteTracker(self.client)

  @commands.Cog.listener()
  async def on_member_join(self, member):
    #"""Display custom welcome message banner."""
    # Open the input image, convert to RGB
    avatar_bytes = requests.get(member.avatar_url, stream=True).raw
    avatar = Image.open(avatar_bytes).convert("RGB")	 
    #Create same size alpha layer with circle, and apply to avatar
    alpha = Image.new("L", avatar.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.ellipse([(0, 0), avatar.size], fill=255)
    avatar.putalpha(alpha)
    font=ImageFont.truetype("./fonts/FontsFree-Net-Shorif-Bongobondhu-UNICODE.ttf",150)
    avatar = avatar.resize((350, 350))
    # Open banner and alpha-composite avatar onto it
    banner = Image.open("./img/omanush bot welcome template-003.png").convert("RGBA")
    overlay = Image.new("RGBA", banner.size)
    overlay.paste(avatar, (500, 680))
    draw=ImageDraw.Draw(overlay)
    name=str(member)
    W, H = (635, 382)
    draw.text((W,H),name,font=font, fill =(231, 117, 93),anchor="mm")
    banner.alpha_composite(overlay)

    # Convert to RGB mode to save as JPG. Append user name, so that we don't upload the wrong image if two users join at almost the same time.

    welcome_file_path = "./img/welcome_banner.png"
    banner.convert("RGB").save(welcome_file_path)
    # inviter is the member who invited
    inviter = await self.tracker.fetch_inviter(member) 
    # inviter is the member who invited
    #embed code for joining server
    embed=discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!")
    #embed.set_thumbnail(url=member.avatar_url)
    file = discord.File("./img/welcome_banner.png", filename="welcome_banner.png")
    embed.set_image(url="attachment://welcome_banner.png")
    embed.add_field(name=f"{member.name} check this channels to get introduced to this server",value=f"Joined at {member.joined_at.strftime(date_format)}",inline=False)
    embed.set_footer(text=f"Invited by:{inviter}",icon_url=inviter.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    #get the channel
    channel=self.client.get_channel(welcome_channel)
    await member.add_roles(member.guild.get_role(oshadharon_role))
    try:
      await channel.send(embed=embed,file=file) 
      await member.send(embed=embed)
    
    except Exception: 
      await channel.send(file=file,embed=embed)
      await self.guil.owner.send(f)
    

def setup(client):
  client.add_cog(welcome(client))

  #@commands.command() for command


