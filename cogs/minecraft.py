import discord
from discord.ext import commands
from discord import app_commands
from mcstatus import JavaServer
from aiomcrcon import Client as RCONClient
import os

class Minecraft(commands.Cog, name="minecraft"):
    def __init__(self, bot):
        self.bot = bot
        # Internal connection (LAN)
        self.mc_host = os.getenv("MC_HOST")
        self.mc_port = int(os.getenv("MC_PORT", "25565"))
        self.rcon_port = int(os.getenv("RCON_PORT", "25575"))
        self.rcon_password = os.getenv("RCON_PASSWORD")
        
        # Public display (Playit.gg)
        self.public_addr = os.getenv("MC_PUBLIC_ADDRESS", "Unknown Address")

    @commands.hybrid_command(
        name="status",
        description="Check the status of the Minecraft server."
    )
    async def status(self, context: commands.Context) -> None:
        """
        Check the status of the Minecraft server.
        """
        await context.defer()

        try:
            # Bot connects locally (Fast & Stable)
            server = JavaServer.lookup(f"{self.mc_host}:{self.mc_port}")
            status = server.status()

            embed = discord.Embed(
                title="⛏️ Minecraft Server Status",
                color=0x57F287  # Green
            )
            
            # Show the Public Playit Address to users
            embed.add_field(name="Server Address", value=f"```{self.public_addr}```", inline=False)
            
            embed.add_field(name="Status", value="🟢 Online", inline=True)
            embed.add_field(name="Latency", value=f"{round(status.latency)}ms", inline=True)
            embed.add_field(name="Players", value=f"{status.players.online}/{status.players.max}", inline=True)
            
            if status.players.sample:
                player_names = [p.name for p.sample]
                # Discord fields have a 1024 char limit; truncate if necessary
                players_str = "\n".join(player_names)
                if len(players_str) > 1000:
                    players_str = players_str[:1000] + "..."
                embed.add_field(name="Online Players", value=players_str, inline=False)
            
            embed.set_footer(text=f"Version: {status.version.name}")
            await context.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(
                title="⛏️ Minecraft Server Status",
                description="🔴 The server appears to be offline.",
                color=0xE02B2B  # Red
            )
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="mc",
        description="Send a command to the Minecraft server console (Admin only)."
    )
    @commands.has_permissions(administrator=True) 
    @app_commands.describe(command="The command to run (without /)")
    async def mccmd(self, context: commands.Context, *, command: str) -> None:
        """
        Send a command to the Minecraft server console.
        """
        await context.defer()

        try:
            # Bot uses internal IP for RCON (Secure)
            async with RCONClient(self.mc_host, self.rcon_port, self.rcon_password) as client:
                response = await client.send_cmd(command)
                
                if len(response) > 1900:
                    response = response[:1900] + "..."
                
                if not response:
                    response = "Command executed (No output)."

                embed = discord.Embed(
                    title="Console Command Executed",
                    description=f"```{response}```",
                    color=0xBEBEFE
                )
                await context.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(
                title="RCON Error",
                description=f"Failed to send command: {e}",
                color=0xE02B2B
            )
            await context.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Minecraft(bot))
