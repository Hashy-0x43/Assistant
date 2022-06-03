
import discord
from discord.ext import commands


with open("../../.Assistant.token", "r") as file:
    TOKEN = file.read()
    file.close()

hashy_id = 693358577376559115


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author.id == hashy_id:
            if message.content.startswith("./say "):
                msg = message.content[6:]
                print(msg, "X")
                
                await message.delete()

                await message.channel.send(f"```{msg}```")

            if message.content.startswith("./mention "):
                id_mention = message.content[10:]
                print(id_mention, "X")

                await message.delete()

                await message.channel.send(id_mention)
                


client = MyClient()
client.run(TOKEN)

