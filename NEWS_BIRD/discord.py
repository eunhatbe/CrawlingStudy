import asyncio

import discord
from discord.ext import commands

TOKEN = """please input your TOKEN"""


class NewsBot:
    def __init__(self):
        pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   intents=intents)


@bot.event
async def on_ready():
    print(f'Bot is ready')

    channel = bot.get_channel(763897112404295703)
    if channel is None:
        print('채널이 없어요 🦉')
        return
    await channel.send("🦉안녕하세요 뉴스를 물어오는 뻐꾸기입니다🦉")


@bot.command(name="run")
async def test(ctx):
    await ctx.send("run.")
    print("test")

async def main():
    async with bot:
        await bot.start(TOKEN)

asyncio.run(main())
