import discord


class Frame:

    def __init__(self):
        self.frame = discord.Embed()

    def user_info(self, context, member: discord.Member) -> discord.Embed:

        role_names = {role.name for role in member.roles if role.name!='@everyone'}

        self.frame.colour = member.colour
        self.frame.timestamp = context.message.created_at
        self.frame.set_author(name=member.mention)
        self.frame.set_thumbnail(url=member.avatar_url)
        self.frame.add_field(name='UserID', value=member.id, inline=False)
        self.frame.add_field(
            name='Server nickname:',
            value=member.display_name,
            inline=False
        )
        self.frame.add_field(
            name='Joined Discord at:',
            value=member.created_at.strftime('%A, %d.%m.%Y o %H:%M'),
            inline=False
        )
        self.frame.add_field(
            name=f'Joined {context.guild.name} at:',
            value=member.joined_at.strftime('%A, %d.%m.%Y o %H:%M'),
            inline=False
        )
        self.frame.add_field(
            name=f'Roles on server ({len(member.roles)})',
            value=', '.join(role for role in role_names),
            inline=False)

        return self.frame

    def warning(self, member: discord.Member, reason):
        self.frame.set_author(name=str(member))
        self.frame.set_thumbnail(url=member.avatar_url)
        self.frame.add_field(name='Reason', value=reason, inline=False)

        return self.frame
