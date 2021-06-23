import discord
from discord.ext import commands
import datetime
from PIL import Image,ImageFont,ImageDraw
import requests

#chanel ids
welcome_channel=843792330129670156
react1_channel=843792330619879425
react2_channel=843792330619879429
#role ids
oshadharon_role=848556720761602088


#time format
date_format="%d %b %Y %H:%M:%S"
timestamp = datetime.datetime.now()

class leave(commands.Cog):

  def __init__(self,client):
    self.client=client

  @commands.Cog.listener() 
  async def on_member_remove(self,member):
    #Display custom welcome message banner.
    # Open the input image, convert to RGB
    avatar_bytes = requests.get(member.avatar_url, stream=True).raw
    avatar = Image.open(avatar_bytes).convert("RGB")

    #Create same size alpha layer with circle, and apply to avatar
      
    alpha = Image.new("L", avatar.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.ellipse([(0, 0), avatar.size], fill=255)
    avatar.putalpha(alpha)
    font=ImageFont.truetype("./fonts/FontsFree-Net-Shorif-Bongobondhu-UNICODE.ttf",130)
    font_small=ImageFont.truetype("./fonts/FontsFree-Net-Shorif-Bongobondhu-UNICODE.ttf",70)
    avatar = avatar.resize((350, 350))
    # Open banner and alpha-composite avatar onto it
    banner = Image.open("./img/omanush bot leave template-001.png").convert("RGBA")
    overlay = Image.new("RGBA", banner.size)
    overlay.paste(avatar, (750, 415))
    draw=ImageDraw.Draw(overlay)
    name=member.name 
    W, H = (893, 868)
    draw.text((W,H),name,font=font, fill =(255, 250, 250),anchor="mm")
    time1=datetime.datetime.utcnow()
    draw.text(((903, 975)),f"({member.joined_at.strftime(date_format) } to {time1.strftime(date_format)})",font=font_small, fill =(255, 250, 250),anchor="mm")
    banner.alpha_composite(overlay)

    # Convert to RGB mode to save as JPG. Append user name, so that we
    # don't upload the wrong image if two users join at almost the same
    # time.

    left_file_path = "./img/left_banner.png"
    banner.convert("RGB").save(left_file_path)

    # Post the image.
    channel = self.client.get_channel(welcome_channel) 
    await channel.send(file=discord.File(left_file_path))
   # await member.send(file=discord.File(left_file_path))
      
      
#@commands.command() for command


def setup(client):
  client.add_cog(leave(client))
