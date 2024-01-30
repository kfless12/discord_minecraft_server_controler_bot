# bot.py
from decouple import config

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)
TOKEN = config("DISCORD_TOKEN")


@bot.command(name="test")
async def test(ctx):
    print("got message")
    await ctx.send("Fuck yo bitch!")


bot.run(TOKEN)
