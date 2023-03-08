import discord
import time
import json
import io
from discord import app_commands
import asyncio
import os

with open('C:/Users/modib/Documents/kali/py/ValHelper_Bot/config.json') as f:
   data = json.load(f)

# region variables 
TOKEN = data["TOKEN"]
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
PREFIX = ":"
LASTUPDATE = "EP_06 // ACT II"
#endregion 

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Riot Games Patches :)"))

@client.event
async def on_message(message:discord.Message):
    if message.author.bot or not(str(message.content).startswith(PREFIX)):
        return
    args = message.content.split(" ")
    args[0] = args[0][1::]
    print(args[0])
    if args[0] == "Agent" :
        with open('C:/Users/modib/Documents/kali/py/ValHelper_Bot/Github/Files/Agents/'+ args[1] + "/desc.json") as d:
            descr = json.load(d)
        img = descr["IMG"]
        desc = descr["DESC"]
        role = descr["ROLE"]
        with open('C:/Users/modib/Documents/kali/py/ValHelper_Bot/Github/Files/Roles/data.json') as c:
            rolesdata = json.load(c)
        thbm = rolesdata[role]
        with open('C:/Users/modib/Documents/kali/py/ValHelper_Bot/Github/Files/Agents/'+ args[1] + "/Abilities/abilities.json") as d:
            abl = json.load(d)
        abilitie1 = abl["ABILITIEONE"]
        ablt1_desc = abl[abilitie1]
        #abl1_img = 'C:/Users/modib/Documents/kali/py/ValHelper_Bot/Github/Files/Agents/'+ args[1] + "/Abilities/" + abilitie1 + ".png"
        abilitie2 = abl["ABILITIETWO"]
        ablt2_desc = abl[abilitie2]
        #abl2_img = 'C:/Users/modib/Documents/kali/py/ValHelper_Bot/Github/Files/Agents/'+ args[1] + "/Abilities/" + abilitie2 + ".png"
        abilitie3 = abl["ABILITIETHREE"]
        ablt3_desc = abl[abilitie3]
        #abl3_img = 'C:/Users/modib/Documents/kali/py/ValHelper_Bot/Github/Files/Agents/'+ args[1] + "/Abilities/" + abilitie3 + ".png"
        abilitie4 = abl["ABILITIEFOUR"]
        ablt4_desc = abl[abilitie4]
        #abl4_img = 'C:/Users/modib/Documents/kali/py/ValHelper_Bot/Github/Files/Agents/'+ args[1] + "/Abilities/" + abilitie4 + ".png"
        mbd = discord.Embed(title=args[1])
        mbd.set_thumbnail(url= thbm)
        mbd.set_image(url= img)
        mbd.add_field(name = "Role", value = role)
        mbd.add_field(name = "Description", value = desc)
        mbd.add_field(name = abilitie1, value = ablt1_desc)
        mbd.add_field(name = abilitie2, value = ablt2_desc)
        mbd.add_field(name = abilitie3, value = ablt3_desc)
        mbd.add_field(name = "ULT : " + abilitie4, value = ablt4_desc)
        await message.channel.send(embed=mbd) 
    
    if args[0] == "Map" :
        with open('C:/Users/modib/Documents/kali/py/ValHelper_Bot/Github/Files/Maps/'+ args[2] + "/data.json") as x:
            descr2 = json.load(x)
        graph = descr2["GRAPH"]
        desc2 = descr2["DESC"]
        persp = descr2["PERSP"]
        mbd2 = discord.Embed(title=args[1])
        mbd2.add_field(name = "Description", value = desc2)
        if args[1] == "Graph" :
            mbd2.set_image(url= graph)
        if args[1] == "Persp" :
            mbd2.set_image(url= persp)
        await message.channel.send(embed=mbd2) 
        
    if args[0] == "Last-Update" :
        await message.channel.send("Last Update : " + LASTUPDATE)
    
    if args[0] == "Help" :
        mbdhelp = discord.Embed(title="Help")
        mbdhelp.add_field(name = "Prefix", value = "` : `")
        mbdhelp.add_field(name = "Informations About Agents :)", value = "Get any information / description / abilities, etc about an agent. Usage : `<Prefix> Agent <Agent Name>`")
        mbdhelp.add_field(name = "\\ \\ Maps :)", value = "Get infos about any map. Usage : `<Prefix> Graph \ Persp <Map>`")
        mbdhelp.add_field(name = "Help :)", value = "Get this page. Usage `<Prefix> Help`")
        await message.channel.send(embed=mbdhelp)

client.run(TOKEN)