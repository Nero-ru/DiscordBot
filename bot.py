import discord
from discord.ext import  commands

client = commands.Bot(command_prefix = '!')

@client.event

async def on_ready():
    print('BOT connected')

@client.command( pass_context = True)

async def hello(ctx):
    await ctx.send('Привет!')

#Connect

token = open ('token.txt', 'r').readline()

client.run(token)