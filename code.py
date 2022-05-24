import discord
from discord.ext import commands
from discord.utils import get
import os


intents = discord.Intents.default()
intents.message_content = True
#go to discord developer portal and go to your bot and enable message content intent


bot = commands.Bot(command_prefix="#put your prefix here", intents=intents)

@bot.event
async def on_ready():
 print(f"{bot.user} is now online :)")

@bot.command()
async def say(ctx, *, arg):
 await ctx.send(arg)
#this command makes it so if someone does (prefix)say hello the bot will send hello to the message channel

bot.run(os.getenv("TOKEN")
