import discord
import time
import json
import io
from discord import app_commands
import interactions
from discord.ext import commands
#from discord_slash import commands, SlashCommand, SlashContext
import asyncio
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
#from discord_slash.utils.manage_components import create_button, create_actionrow
#from discord_slash.model import ButtonStyle
import os
from discord import Color

with open('C:/Users/modib/Documents/kali/py/ValHelper_Bot/config.json') as f:
   data = json.load(f)

# region variables 
TOKEN = data["TOKEN"]
intents = discord.Intents.all()
intents.message_content = True
bot = interactions.Client(token = TOKEN)
client = discord.Client(intents=intents)
#tree = app_commands.CommandTree(client)
PREFIX = ":"
LASTUPDATE = "EP_06 // ACT II"
options = Options()
driver = webdriver.Chrome(options=options)
#slash = SlashCommand(client, sync_commands = True)
#endregion 

def GetStats(args) :
    CORRECTEDargs = str(args).replace('#', '%23')
    driver.get('https://tracker.gg/valorant/profile/riot/' + CORRECTEDargs + '/overview')
    #driver.execute_script("""
   #var l = document.getElementsByXPATH("//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/comment()[1]")[0];
   #l.parentNode.removeChild(l);
#""")
    #driver.execute_script("""
   #var l = document.getElementsByXPATH("//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/comment()[2];
   #l.parentNode.removeChild(l);
#""")
    #currentRank = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/text()'))
    mbd_stats = discord.Embed(title=" Ranked Stats :", color = Color.red())
    #mbd_stats.add_field(name = 'Current Rank :', value = currentRank.text)
    time.sleep(1)
    winRate = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[4]/div/div[2]/span[2]'))
    mbd_stats.add_field(name = 'Winrate :', value = winRate.text)
    hsPourc = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[3]/div/div[2]/span[2]')
    mbd_stats.add_field(name = 'HS / % :', value = hsPourc.text)
    KDRatio = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/span[2]')
    rankImg = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/img')
    imgUrl = rankImg.get_attribute("src")
    mbd_stats.set_thumbnail(url= imgUrl)
    mbd_stats.add_field(name = 'HD Ratio :', value = KDRatio.text)
    #aces = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[5]/div[12]/div/div[1]/span[2]'))
    driver.get('https://tracker.gg/valorant/profile/riot/' + CORRECTEDargs + '/performance')
    playTime = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[2]'))
    mbd_stats.add_field(name = 'Playtime :', value = playTime.text)
    driver.get('https://tracker.gg/valorant/profile/riot/' + CORRECTEDargs + '/agents?playlist=unrated')
    mainAgent = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]'))
    agent = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/img')
    #agentIMG = agent.get_attribute("src")
    mbd_stats.add_field(name = 'Main Agent :', value = mainAgent.text)
    #mbd_stats.set_image(url= agentIMG)
    mbd_stats.set_author(name= args)
    mbd_stats.set_footer(text= "All informations are from https://tracker.gg/valorant")
    
    #mbd_stats.add_field(name = 'Aces :', value = aces.text)
    return mbd_stats

mbdhelp = discord.Embed(title="Help")
mbdhelp.add_field(name = "Prefix", value = "` : `")
mbdhelp.add_field(name = "Informations About Agents :)", value = "Get any information / description / abilities, etc about an agent. Usage : `<Prefix> Agent <Agent Name>`")
mbdhelp.add_field(name = "\\ \\ Maps :)", value = "Get infos about any map. Usage : `<Prefix> Graph \ Persp <Map>`")
mbdhelp.add_field(name = "Help :)", value = "Get this page. Usage `<Prefix> Help`")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Riot Games Patches :)"))
    
@bot.command(name="help", description="Get Usage help for commands :D", scope=786255946535796759)
async def help(ctx: interactions.CommandContext):
    await interactions.channel.send(embed=mbdhelp)

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
        await message.channel.send(embed=mbdhelp)

    if args[0] == 'Stats' :
        await message.channel.send('Hang on while we searching for : ' + args[1])
        mbdstats = GetStats(args=args[1])
        await message.channel.send(embed=mbdstats)

#@tree.command(name = "help", description = "Get usage help :)", guild=discord.Object(id=1079717093689278514)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
#async def first_command(interaction):
#    await interaction.channel.send(embed=mbdhelp)

#@slash.slash(name="help", description= "Get usage help and other stuff", guild_ids="786255946535796759")
#async def help(message):
#    await message.channel.send(embed=mbdhelp)

client.run(TOKEN)