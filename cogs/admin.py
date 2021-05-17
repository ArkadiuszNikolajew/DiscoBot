from discord.ext import commands, tasks
import sys


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def check(self, ctx):
        a = self.bot.get_all_members()
        for b in a:
            await ctx.send(b)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Wyłącznie bota"""
        await ctx.send('Do zobaczenia wkrótce!')
        await self.bot.logout()
        sys.exit(0)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def restart(self, ctx):
        """Restart bota"""
        await ctx.send('BRB')
        await self.bot.logout
        sys.exit(6)

    # Manage Extensions

    @commands.command(hidden=True)
    @commands.is_owner()
    async def load_ext(self, extension):
        self.bot.load_extension(f'cogs.{extension}')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload_ext(self, extension):
        self.bot.reload_extension(f'cogs.{extension}')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload_ext(self, extension):
        self.bot.unload_extension(f'cogs.{extension}')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def new_role(self, ctx, name, colour, hoist=False, reason=None):
        await ctx.guild.create_role(name=name, hoist=hoist, colour=colour, reason=reason)


def setup(bot):
    bot.add_cog(Admin(bot))

