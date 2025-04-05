import discord
from discord.ext import commands
import os
import asyncio

TOKEN = os.environ["DISCORD_TOKEN"]
GUILD_ID = 1356894863454376105  # jouw server ID

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Ingelogd als {bot.user}")
    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await bot.tree.sync(guild=guild)
        print(f"✅ Slash commands gesynchroniseerd met GUILD {guild.id} ({len(synced)} commando's)")
    except Exception as e:
        print(f"❌ Sync error: {e}")
    await load_cogs()

async def load_cogs():
    try:
        await bot.load_extension("commands.ping")
        await bot.load_extension("commands.analyse")
        print("✅ Alle commando's geladen")
    except Exception as e:
        print(f"❌ Fout bij laden commando's: {e}")

async def main():
    async with bot:
        await main_startup()
        await bot.start(TOKEN)

async def main_startup():
    pass

asyncio.run(main())