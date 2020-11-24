import discord
import random
from discord.ext import commands
from config import settings


bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event

async def on_ready():
    print('BOT connected')

@bot.command()

async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'{author.mention} Привет!')


#Connect
bot.run(settings['token'])
