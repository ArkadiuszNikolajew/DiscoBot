import datetime
import re
import discord
import unicodedata
import asyncio
from frames import Frame
from discord.ext import commands
from utils import bad_words


class AutoMod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        async def bad_language():
            for word in message.content.split():
                if word.lower() in bad_words:
                    await message.delete()

        async def all_caps():
            if len(message.content) > 4 and message.content.isupper():
                await message.delete()

        async def invite():
            base_pattern = r'(https:)|(w{3}\.+)'
            if re.search(base_pattern + r'discord\.gg', message.content):
                await message.channel.send(embed=Frame().warning(message.author, 'Posted an invite'))
            elif re.search(r'(https:)|(w{3}\.+)', message.content):
                await message.channel.send(embed=Frame().warning(message.author, 'Posted a link'))
            await message.delete()

        async def zalgo():
            zalgo_categories = {'Mn', 'Me'}
            for char in list(message.content):
                if unicodedata.category(char) in zalgo_categories:
                    await message.delete()

        try:
            await asyncio.gather(bad_language(), all_caps(), invite(), zalgo())
        except discord.NotFound:
            print('This message was already deleted')

        await self.bot.process_commands(message)


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        await message.channel.send(f'Message from {message.author.mention} was deleted')


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f'Nie ma takiej komendy. Wpisz !help, aby zobaczyć dostępne komendy.')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Nie masz wystarczającej mocy by wykonać to zadanie')
        if isinstance(error, commands.CommandOnCooldown):
            cooldown = str(datetime.timedelta(seconds=error.retry_after)).split('.')[0].split(':')
            await ctx.send(f"Możesz użyć tej komendy ponownie za {cooldown[0]}h {cooldown[1]}m {cooldown[2]}s")

def setup(bot):
    bot.add_cog(AutoMod(bot))