import discord
from discord.ext import commands
from frames import Frame


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands

    @commands.command()
    async def ping(self, ctx):
        """Ping Server"""
        await ctx.send(f':ping_pong: Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def user_info(self, ctx, member: discord.Member = None):
        """
        Shows info about user, e.g {command_prefix}user_info @testuser.
        If member argument is not passed show info about user invoking the command
        """
        member = ctx.author if not member else member
        await ctx.send(embed=Frame().user_info(ctx, member))


def setup(bot):
    bot.add_cog(Info(bot))

