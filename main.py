import asyncio
import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import model

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot_client = commands.Bot(command_prefix='-',
                          intents=discord.Intents.all(),
                          help_command=None,
                          strip_after_prefix=True)
# setup logging since im not doing client.run()
logging.basicConfig(level=logging.INFO)

@bot_client.event
async def on_ready():
    print("Bot ready!")
    print(f'Logged in as {bot_client.user.name}')

async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error

@bot_client.event
async def setup_hook():
    # Sync commands to discord

    await bot_client.tree.sync(guild=None)


    print("Commands synced!")

# Startup method
async def main():
    async with bot_client:
        print("Preparing database...")
        # Create database and its models if it doesn't exist already
        model.create_tables()
        print("Database prepared.")
        print("Syncing commands...\n-----")
        for file in os.listdir("./commands"):  # lists all the cog files inside the command folder.
            if file.endswith(".py"):  # It gets all the cogs that ends with a ".py".
                await bot_client.load_extension(
                    f"commands.{file[:-3]}")  # It gets the name of the file removing the ".py" and loads the command.
        print("-----")

        # load stuff from .env
        load_dotenv()

        await bot_client.start(os.environ["BOT_TOKEN"])

if __name__ == '__main__':
    asyncio.run(main())
