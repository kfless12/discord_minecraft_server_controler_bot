# bot.py
from decouple import config

import discord
from discord.ext import commands
from droplet_control import DropletController

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)
TOKEN = config("DISCORD_TOKEN")

droplet_controller = DropletController()


@bot.command(name="hard_reset")
async def test(ctx):
    await ctx.send("Restarting the server...")
    droplet_controller.power_cycle_droplet()


bot.run(TOKEN)
