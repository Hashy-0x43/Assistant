import discord
from discord.ext import commands
import binascii
import hashlib
import os
import re
import base65536
import json
import urllib.request
from pytube import YouTube
import base64


TOKEN = ''


client = commands.Bot(command_prefix='./')


@client.event
async def on_ready():
    print("Status: Ready!")


def yes_encoding(arguement):
    return arguement.encode()


def no_encoding(arguement):
    return arguement


error_idk = "```I don't know```"
error_too_long = "```Too Long!```"


@client.command()
async def goals(ctx):
    file = open("goals.txt", "r")
    goals = "```" + file.read() + "```"
    file.close()
    await ctx.send(goals)


@client.command()
async def str2hex(ctx, *, content: yes_encoding):
    """encode hexadecimal"""
    if len(content) < 1500:
        await ctx.send("```" + binascii.hexlify(content).decode('utf-8') + "```")
    if len(content) > 1500:
        await ctx.send(error_too_long)


@client.command()
async def hex2str(ctx, *, content: yes_encoding):
    """decode hexadecimal"""
    if len(content) < 1500:
        await ctx.send("```" + binascii.unhexlify(content).decode('utf-8') + "```")
    if len(content) > 1500:
        await ctx.send(error_too_long)


@client.command()
async def md5(ctx, *, content: no_encoding):
    """converts string to md5 hash"""
    if len(content) > 1500:
        await ctx.send(error_too_long)
    if len(content) < 1500:
        content = hashlib.md5(content.encode())
        await ctx.send("```" + content.hexdigest() + "```")


@client.command()
async def sha1(ctx, *, content: no_encoding):
    """converts string to sha1 hash"""
    if len(content) > 1500:
        await ctx.send(error_too_long)
    if len(content) < 1500:
        content = hashlib.sha1(content.encode())
        await ctx.send("```" + content.hexdigest() + "```")


@client.command()
async def sha224(ctx, *, content: no_encoding):
    """converts string to sha224 hash"""
    if len(content) > 1500:
        await ctx.send(error_too_long)
    if len(content) < 1500:
        content = hashlib.sha224(content.encode())
        await ctx.send("```" + content.hexdigest() + "```")


@client.command()
async def sha256(ctx, *, content: no_encoding):
    """converts string to sha256 hash"""
    if len(content) > 1500:
        await ctx.send(error_too_long)
    if len(content) < 1500:
        content = hashlib.sha256(content.encode())
        await ctx.send("```" + content.hexdigest() + "```")


@client.command()
async def sha384(ctx, *, content: no_encoding):
    """converts string to sha384 hash"""
    if len(content) > 1500:
        await ctx.send(error_too_long)
    if len(content) < 1500:
        content = hashlib.sha384(content.encode())
        await ctx.send("```" + content.hexdigest() + "```")


@client.command()
async def sha512(ctx, *, content: no_encoding):
    """converts string to sha512 hash"""
    if len(content) > 1500:
        await ctx.send(error_too_long)
    if len(content) < 1500:
        content = hashlib.sha512(content.encode())
        await ctx.send("```" + content.hexdigest() + "```")

"""
@client.command(hidden = True)
async def nmap(ctx, *, content: no_encoding):
    <IPv4> : full nmap scan
    if re.search("^192", content) == False:
        result = os.popen("nmap -p 22 -Pn " + content).read()
        await ctx.send("```" + result + "```")
    if re.search("^192", content) == True:
        await ctx.send("```No```")
"""
# use the nmap3 module
@client.command()
async def ebase65536(ctx, *, content: yes_encoding):
    """encode base65536"""
    if len(content) > 1500:
        await ctx.send(error_too_long)
    if len(content) < 1500:
        content = base65536.encode(content)
        await ctx.send("```" + content + "```")

@client.command()
async def dbase65536(ctx, *, content: no_encoding):
    """decode base65536"""
    if len(content) > 1500:
        await ctx.send(error_too_long)
    if len(content) < 1500:
        content = base65536.decode(content)
        await ctx.send("```" + content.decode() + "```")

@client.command()
async def C19(ctx):
    """Current total of COVID-19 deaths in the US"""
    data = urllib.request.urlopen("https://api.covid19api.com/summary").read()
    info = json.loads(data)
    await ctx.send("```" + "Total Deaths in the United States: " + str(info["Countries"][181]["TotalDeaths"]) + "```")

"""
@client.command()
async def YouTube(ctx, *, content: no_encoding):
    """"WORK IN PROGRESS""""
    # <url> : downloads YouTube videos and outputs as base64 string
    yt = YouTube(content)
    stream = yt.streams.first()
    stream.download("C:\\Users\\" + username + "\\Videos\\YouTube_Downloads\\")
    video = open("C:\\Users\\" + username + "\\Videos\\YouTube_Downloads\\" + yt.title + ".mp4","rb")
    data = video.read()
    video.close()
    data = base64.b64encode(data.encode("ascii"))

    await ctx.send(data)
"""

import webbrowser

@client.command()
async def TEST(ctx):
    """Nothing"""
    file = open("Worked","w")
    file.write("X")
    file.close()
    await ctx.send("Done")

client.run(TOKEN)
