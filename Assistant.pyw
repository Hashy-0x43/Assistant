
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
async def calc(ctx, operator, x, y):
    possible_operator_arguments = ["--multiply", "--divide", "--add", "--subtract"]
    x = int(x)
    y = int(y)
    
    if operator == "--multiply":
        z = x * y
    
    if operator == "--divide":
        z = x / y
    
    if operator == "--add":
        z = x + y
    
    if operator == "--subtract":
        z = x - y

    if operator not in possible_operator_arguments:
        z = "Operator not implemented."

    z = str(z)

    await ctx.send(z)


client.run(TOKEN)
