import discord
import time
import json
import io
#from discord import app_commands
import interactions
#from discord.ext import commands
#from discord_slash import commands, SlashCommand, SlashContext
import asyncio
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pyvirtualdisplay import Display 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from discord import ButtonStyle, ActionRow, Button
import os
from discord.ext import commands
from discord import Color 

with open('C:/Users/Samy Lamlih/Documents/py/ValHelper_Bot/config.json') as f:
   data = json.load(f)

# region variables 
#display = Display(visible=0, size=(800, 600))
#display.start()
TOKEN = data["TOKEN"]
intents = discord.Intents.all()
intents.message_content = True
scope = data["SCOPE"]
client = discord.Client(intents=intents)
#tree = app_commands.CommandTree(client)
PREFIX = ":"
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
LASTUPDATE = "EP_06 // ACT II"
options = Options()
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
#slash = SlashCommand(client, sync_commands = True)
#endregion 

def GetMap(args1, args2):
    with open('C:/Users/Samy Lamlih/Documents/py/ValHelper_Bot/Github/Files/Maps/'+ args2 + "/data.json") as x:
            descr2 = json.load(x)
    graph = descr2["GRAPH"]
    desc2 = descr2["DESC"]
    persp = descr2["PERSP"]
    mbd2 = discord.Embed(title=args2)
    mbd2.add_field(name = "Description", value = desc2)
    if args1 == "Graph" :
        mbd2.set_image(url= graph)
    if args1 == "Persp" :
        mbd2.set_image(url= persp)
    return mbd2

def GetStats(args) :
    CORRECTEDargs = str(args).replace('#', '%23')
    driver.get('https://tracker.gg/valorant/profile/riot/' + CORRECTEDargs + '/overview?playlist=competitive&season=all')
    time.sleep(1)
    try:
        if driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/span') :
            print('private sTATS')
            StatsError = True
            return StatsError

    except NoSuchElementException:
        StatsError = False
        try :
            rankImg = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/img')
            NoRanked = "rank"
        #components = [ActionRow(interactions.Button(url=('https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
        #                           label="This is an Link",
        #                           style=ButtonStyle.url,
        #                          emoji='🎬'))
        #]
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
            imgUrl = rankImg.get_attribute("src")
            mbd_stats.set_thumbnail(url= imgUrl)
            mbd_stats.add_field(name = 'HD Ratio :', value = KDRatio.text)
            #aces = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[5]/div[12]/div/div[1]/span[2]'))
            driver.get('https://tracker.gg/valorant/profile/riot/' + CORRECTEDargs + '/performance')
            playTime = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[2]'))
            mbd_stats.add_field(name = 'Playtime :', value = playTime.text)
            driver.get('https://tracker.gg/valorant/profile/riot/' + CORRECTEDargs + '/agents?playlist=unrated&season=all')
            mainAgent = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]'))
            mbd_stats.add_field(name = 'Main Agent :', value = mainAgent.text)
            #agent = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/img')
            #agentIMG = agent.get_attribute("src")
            driver.get('https://tracker.gg/valorant/profile/riot/' + CORRECTEDargs + '/overview?playlist=unrated&season=all')
            topMap = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[1]/div[3]/div/div[2]/div[1]'))
            mbd_stats.add_field(name = 'Top Map :', value = topMap.text)
            driver.get('https://tracker.gg/valorant/profile/riot/' + CORRECTEDargs + '/matches?playlist=unrated&season=all')
            #topFriend = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[1]/a/text()')) 
            #mbd_stats.add_field(name = 'Favorite Teamate :', value = topFriend.text)
            #mbd_stats.set_image(url= agentIMG)
            mbd_stats.set_author(name= args)
            mbd_stats.set_footer(text= "All informations are taken from https://tracker.gg/valorant")
            #driver.close()
            return mbd_stats

        except NoSuchElementException :
            NoRanked = "norank"
            return NoRanked
    #return components
    
    #mbd_stats.add_field(name = 'Aces :', value = aces.text)  

def GetHelp():
    mbdhelp = discord.Embed(title="Help")
    mbdhelp.add_field(name = "Prefix", value = "` : `")
    mbdhelp.add_field(name = "Informations About Agents :)", value = "Get any information / description / abilities, etc about an agent. Usage : `<Prefix> Agent <Agent Name>`")
    mbdhelp.add_field(name = "Informations About Maps :)", value = "Get infos about any map. Usage : `<Prefix> Graph \ Persp <Map>`")
    mbdhelp.add_field(name = "Help :)", value = "Get this page. Usage `<Prefix> Help`")
    mbdhelp.add_field(name = "Stats :)", value = "Get your ranked stats. Usage `<Prefix> Stats <yourfullname>`")
    return mbdhelp

def GetAgent(args1):
    with open('C:/Users/Samy Lamlih/Documents/py/ValHelper_Bot/Github/Files/Agents/'+ args1 + "/desc.json") as d:
            descr = json.load(d)
    img = descr["IMG"]
    desc = descr["DESC"]
    role = descr["ROLE"]
    with open('C:/Users/Samy Lamlih/Documents/py/ValHelper_Bot/Github/Files/Roles/data.json') as c:
        rolesdata = json.load(c)
    thbm = rolesdata[role]
    with open('C:/Users/Samy Lamlih/Documents/py/ValHelper_Bot/Github/Files/Agents/'+ args1 + "/Abilities/abilities.json") as d:
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
    mbd = discord.Embed(title=args1)
    mbd.set_thumbnail(url= thbm)
    mbd.set_image(url= img)
    mbd.add_field(name = "Role", value = role)
    mbd.add_field(name = "Description", value = desc)
    mbd.add_field(name = abilitie1, value = ablt1_desc)
    mbd.add_field(name = abilitie2, value = ablt2_desc)
    mbd.add_field(name = abilitie3, value = ablt3_desc)
    mbd.add_field(name = "ULT : " + abilitie4, value = ablt4_desc)
    return mbd

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Riot Games Patches :)"))
    
#@bot.command(name="gethelp", description="Get Usage help for commands :D", scope=scope)
#async def help(interaction: discord.Interaction):
#    await interactions.send(embed=mbdhelp)

@client.event
async def on_message(message:discord.Message):
    if message.author.bot or not(str(message.content).startswith(PREFIX)):
        return
    args = message.content.split(" ")
    args[0] = args[0][1::]
    print(args)
    if args[0] == "Agent" :
        mbdAgent = GetAgent(args1=args[1])
        await message.channel.send(embed=mbdAgent) 
    
    if args[0] == "Map" :
        mbdMap = GetMap(args1= args[1], args2= args[2])
        await message.channel.send(embed=mbdMap) 
        
    if args[0] == "Last-Update" :
        await message.channel.send("Last Update : " + LASTUPDATE)
    
    if args[0] == "Help" :
        mbdHelp = GetHelp()
        await message.channel.send(embed=mbdHelp)

    if args[0] == 'Stats' :
        await message.channel.send('Hang on while we searching for : ' + args[1])
        mbdstats = GetStats(args=args[1])
        argsCOR = str(args[1]).replace('#', '%23')
        if mbdstats == True :
            buttonUrl = Button(
                    style=ButtonStyle.url,
                    label="Sign in",
                    url='https://tracker.gg/valorant/profile/riot/' + argsCOR,
                    )
            action_row = ActionRow(buttonUrl)
            await message.channel.send('Your profile is private :(, or you have never logged in with tracker.gg, try :', components=[action_row])
            
        if mbdstats == "norank" :
            await message.channel.send('You have never played ranked before :(')
            #await message.channel.send('Sign in here to get your stats and use this bot : https://tracker.gg/valorant/profile/riot/' + argsCOR)
        else :
            buttonUrlG = Button(
                    style=ButtonStyle.url,
                    label="Check more Details :D",
                    url='https://tracker.gg/valorant/profile/riot/' + argsCOR,
                    )
            action_row2 = ActionRow(buttonUrlG)
            await message.channel.send(embed=mbdstats, components=[action_row2]) #components=mbdstats)

#@client.slash_command(name ="help", description="Get commands and usage help :D")
#async def help(message:discord.SlashCommand):
    mbd = GetHelp()
    await message.channel.send(embed=mbd)

#@client.slash_command(name ="last-update", description="Get last updated episode for this bot (VALORANT)")
#async def help(message:discord.SlashCommand):
#    await message.channel.send("Last Update : " + LASTUPDATE)
#
#@client.slash_command(name ="help", description="Get usage and commands help :D")
#async def help(message:discord.SlashCommand):
#    mbdhelp = GetHelp()
#    await message.channel.send(embed=mbdhelp)

#@client.slash_command(name ="help", description="Get your ranked stats :D", options = [
#        interactions.Option(
#            name="ID",
#            description="Your ID",
#            type=discord.OptionType.,
#            required=True,
#        ),
#    ],)
#async def help(message:discord.SlashCommand, name):
#    await message.channel.send('Hang on while we searching for : ' + name)
#    mbdstats = GetStats(args=name)
#    argsCOR = str(name).replace('#', '%23')
#    if mbdstats == True :
#        buttonUrl = Button(
#                style=ButtonStyle.url,
#                label="Sign in",
#                url='https://tracker.gg/valorant/profile/riot/' + argsCOR,
#                )
#        action_row = ActionRow(buttonUrl)
#        await message.channel.send('Your profile is private :(, or you have never logged in with tracker.gg, try :', components=[action_row])
#        
#    if mbdstats == "norank" :
#        await message.channel.send('You have never played ranked before :(')
#        #await message.channel.send('Sign in here to get your stats and use this bot : https://tracker.gg/valorant/profile/riot/' + argsCOR)
#    else :
#        buttonUrlG = Button(
#                style=ButtonStyle.url,
#                label="Check more Details :D",
#                url='https://tracker.gg/valorant/profile/riot/' + argsCOR,
#                )
#        action_row2 = ActionRow(buttonUrlG)
#        await message.channel.send(embed=mbdstats, components=[action_row2])

client.run(TOKEN)