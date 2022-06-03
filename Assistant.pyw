import discord
from discord.ext import commands


with open("../../.Assistant.token", "r") as file:
    TOKEN = file.read()
    file.close()


client = commands.Bot(command_prefix='./')


@client.event
async def on_ready():
    print("Status: Ready!")


@client.command()
async def goals(ctx):
    file = open("goals.txt", "r")
    goals = "```" + file.read() + "```"
    file.close()
    await ctx.send(goals)


@client.command()
async def action(ctx, content):
    await ctx.send(content)


client.run(TOKEN)
