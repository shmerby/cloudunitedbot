import discord
from discord.ext import commands

bot = commands.Bot(";")

@bot.event
async def on_ready():
    print("cloud bot on")
    
"""Cloud Commands"""

@bot.command(pass_context=True)
async def cuddle(ctx):
    await bot.say("***cuddles*** :3")

@bot.command(pass_context=True)
async def cloud(ctx):
    await bot.say("clouds are cute x3")
    
@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say("hi :wave:")

@bot.command(pass_context=True)
async def hug(ctx):
    await bot.say("***hugs super tight*** :hugging: :blush:")

@bot.command(pass_context=True)
async def feed(ctx):
    await bot.say("cuddles and feeds yummy cloud snacks :blush:")  
 
@bot.command(pass_context=True)
async def sad(ctx):
    await bot.say("***picks you up, hugs super tight and cuddles till ur happy :3***")

@bot.command(pass_context=True)
async def revolution(ctx):
    await bot.say("GLORY GLORY GLORY TO THE CLOUDS! GLORY GLORY GLORY! CLOUD REVOLUTION NOW!")
    





bot.run("NDEzNDM1NTE5MTI5NzQ3NDU2.DWYxXA.ZdYatPUt-IafiCwiD5YDLqPdkJ0")
