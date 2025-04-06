import discord
from discord.ext import commands
import asyncio
import os

# Environment variable voor je bot-token (Render)
TOKEN = os.getenv("DISCORD_TOKEN")

# Hardcoded Guild ID (vervang dit door jouw echte Discord server ID)
GUILD_ID = 1356894863454376105

# Bot setup
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
        await bot.load_extension("commands.ping")  # Laad ping commando
        await bot.start(TOKEN)

# Start bot
asyncio.run(main())
