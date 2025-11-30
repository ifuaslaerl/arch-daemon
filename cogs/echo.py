"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.4.0
"""

from discord.ext import commands
from discord.ext.commands import Context

class Echo(commands.Cog, name="echo"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_command(
        name="echo",
        description="This command makes the bot repeat whateaver you texted.",
    )
    async def testcommand(self, context: Context, message: str) -> None:
        """
        This command makes the bot repeat whateaver you texted.

        :param context: The application command context.
        :param message: The message the bot repeat.
        """
        
        await context.send(message)

async def setup(bot) -> None:
    await bot.add_cog(Echo(bot))
