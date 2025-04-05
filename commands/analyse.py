import discord
from discord.ext import commands
from discord import app_commands

class Analyse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="analyse", description="Geef een mock analyse van een coin")
    @app_commands.describe(coin="De coin om te analyseren")
    async def analyse(self, interaction: discord.Interaction, coin: str):
        await interaction.response.send_message(
            f"Mock analyse voor {coin.upper()}:\nRSI: 47.8\nTrend: neutraal\nPrijs: $0.123"
        )

async def setup(bot):
    await bot.add_cog(Analyse(bot))