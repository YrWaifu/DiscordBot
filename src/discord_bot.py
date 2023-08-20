import discord
from discord.ext import commands
from token.py import token

config = {
    "token" : token,
    "prefix" : "prefix"
}

bot =  commands.Bot(command_prefix=config["prefix"])

@bot.event
async def onMessage(ctx):
    if ctx.author != bot.user:
        await ctx.reply(ctx.content)

bot.run[config("token")]