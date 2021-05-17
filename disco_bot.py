import os
import discord
from discord.ext import commands
import locale
from dotenv import load_dotenv
import json

import asyncio


base_path = os.path.dirname(__file__)
locale.setlocale(locale.LC_ALL, "pl_PL.UTF-8")
intents = discord.Intents.all()
intents.typing = False
load_dotenv()
bot = commands.Bot(command_prefix=os.environ.get("COMMAND_PREFIX"), intents=intents)


# with open('json_config.json') as file:
#     config = json.load(file)


for filename in os.listdir(os.path.join(base_path, './cogs')):
    if filename.endswith('.py') and filename != 'db.py':
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
    print('Bot is ready')


bot.run(os.environ.get("BOT_TOKEN"))
