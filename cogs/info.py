import discord
from discord.ext import commands


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
        """Info o użytkowniku. Przykład: !user_info @testuser"""
        member = ctx.author if not member else member
        role_names = [role.name for role in member.roles]

        u_info = discord.Embed(colour=member.colour,
                               timestamp=ctx.message.created_at)
        u_info.set_author(name=f'Informacje o {member}')
        u_info.set_thumbnail(url=member.avatar_url)
        u_info.set_footer(text=f'Wywołane przez {ctx.author}',
                          icon_url=ctx.author.avatar_url)
        u_info.add_field(name='ID', value=member.id, inline=False)
        u_info.add_field(name='Nazwa na serwerze:',
                         value=member.display_name, inline=False)
        u_info.add_field(name='Status:', value=member.status, inline=False)
        u_info.add_field(name='Dołączył do Discord:',
                         value=member.created_at.strftime('%A, %d.%m.%Y o %H:%M'),
                         inline=False)
        u_info.add_field(name=f'Dołączył do {ctx.guild.name}a:',
                         value=member.joined_at.strftime('%A, %d.%m.%Y o %H:%M'),
                         inline=False)
        u_info.add_field(name=f'Role ({len(member.roles)})',
                         value=', '.join(role for role in role_names),
                         inline=False)
        u_info.add_field(name='Bot?', value='Nie' if not member.bot else 'Tak',
                         inline=False)

        await ctx.send(embed=u_info)


def setup(bot):
    bot.add_cog(Info(bot))

