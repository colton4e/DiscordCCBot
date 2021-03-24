import os
import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

@client.event
async def on_message(message):
    if message.author == client.user: return # Don't make the bot reply to itself

    if message.content.startswith("!join"):
        if message.author.voice:
            vc = await message.author.voice.channel.connect()
        else:
            await message.channel.send("You're not in a voice channel idiot")

if __name__ == "__main__":
    client.run(TOKEN)

