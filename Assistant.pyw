
import discord
from discord.ext import commands


with open("../Assistant-Configs/.bot.token", "r") as file:
    TOKEN = file.read()
    file.close()

with open("../Assistant-Configs/.user.ids", "r") as file:
    allowed_users = file.read()
    file.close()


class client(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if str(message.author.id) in allowed_users:
            if message.content.startswith("./say "):
                msg = message.content[6:]
                
                await message.delete()

                await message.channel.send(f"```{msg}```")

            if message.content.startswith("./mention "):
                id_mention = message.content[10:]

                await message.delete()

                await message.channel.send(id_mention)


client = client()
client.run(TOKEN)

