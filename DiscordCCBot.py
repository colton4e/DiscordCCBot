import os
import discord
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

if __name__ == "__main__":
    client.run(TOKEN)

