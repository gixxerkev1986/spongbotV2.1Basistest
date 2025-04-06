import discord
from discord.ext import commands
import asyncio
import os

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = 1356894863454376105  # <-- Vervang indien nodig

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"[INFO] Bot is online als {bot.user}")
    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await bot.tree.sync(guild=guild)
        print(f"[SYNC] Slash commands gesynchroniseerd naar guild {GUILD_ID}: {len(synced)} command(s)")
        for cmd in synced:
            print(f"[SYNC] -> /{cmd.name} | {cmd.description}")
    except Exception as e:
        print(f"[ERROR] Fout bij slash sync: {e}")

async def main():
    async with bot:
        try:
            await bot.load_extension("commands.ping")
            print("[LOAD] ping.py succesvol geladen")
        except Exception as e:
            print(f"[ERROR] ping.py niet geladen: {e}")
        await bot.start(TOKEN)

# Start de bot
asyncio.run(main())
