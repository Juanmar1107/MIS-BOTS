import discord

from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event

async def on_ready():

    print(f'We have logged in as {bot.user}')

@bot.command()

async def hello(ctx):

    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()

async def heh(ctx, count_heh = 5):

    await ctx.send("he" * count_heh)

@bot.event

async def on_message(message):

    if message.author == bot.user:

        return

    if message.content.startswith('$hello'):

        await message.channel.send("Hi!")

    elif message.content.startswith('$bye'):

        await message.channel.send("\U0001f642")

    else:

        await message.channel.send(message.content)

 

 

 

 

 

bot.run("MTM0NjY3MDgyNjIwNzk2OTMwMA.G8Wthn.d7NgFpi2-9j3B-fcJwAQ7C8HvkuwBl1DSCYgWI")
