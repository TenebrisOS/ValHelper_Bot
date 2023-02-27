import discord
import time
import json
import io
import os

with open('C:/Users/modib/Documents/kali/py/ValHelper_Bot/config.json') as f:
   data = json.load(f)

# region variables 
TOKEN = data["TOKEN"]
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
PREFIX = "§"
#endregion