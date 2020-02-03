#1ccbot created by 99710
#based on TB 2.0.9

##Parameters##

#Version
bot_version = '1.0.1'

#owner id
owner_id = '166189271244472320'

#debug switch
debugmode = True

#Spicetools URL
spiceurl = "http://onlyone.cab/downloads/spicetools-latest.zip"

#Bemanitools URL
btoolURL = "http://tools.bemaniso.ws/bemanitools-v5.28.zip"

import discord
import requests
import aiohttp
import random
import asyncio
import os
import subprocess
import time

from discord.ext import commands
from random import randint

print('Please wait warmly...')

#initial_extensions = ['Modules.image', 'Modules.booru']
client = discord.Client()

if debugmode == True:
    bot = commands.Bot(command_prefix=("1c."), case_insensitive=True)
    print ("debug")
else:
    bot = commands.Bot(command_prefix=commands.when_mentioned, case_insensitive=True)
    
bot.remove_command("help")


st = time.time()

#if __name__ == '__main__':
#    for extension in initial_extensions:
#        bot.load_extension(extension)


#ready status display
@bot.event
async def on_ready():
    print(' ')
    print('Username - ' + bot.user.name)
    print('TenshiBot Ver - ' + bot_version)
    await bot.change_presence(activity=discord.Game(name="Startup complete"))
    await asyncio.sleep(7)
    await bot.change_presence(activity=discord.Streaming(name="/1CC/", url='https://twitch.tv/99710'))

    
#error event code
#print the error to the console and inform the user   
@bot.event
async def on_command_error(ctx, error):
    #command not found
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Error: Invalid command")        
        return
    #user failed check
    if isinstance(error, commands.CheckFailure):       
        await ctx.send("Error: Only the owner can use this command")
    else:
        await ctx.send(error)
        print(error)
        return

@bot.event
async def on_message(message):
    emoji = '\U0001F6AB'
    contents = message.content
    hdd = open("txt/hddtext.txt", "r")
    hddtext = hdd.read()
    if message.author == bot.user:
        return
    if message.author.bot:
        return	
    
#game hdd checks
    if "iidx hdd" in contents:  
        await message.channel.send(hddtext)
        return

    if "sdvx hdd" in contents: 
        await message.channel.send(hddtext)
        return

    if "ddr hdd" in contents:   
        await message.channel.send(hddtext)
        return	
    
    await bot.process_commands(message)

#command printing to console
@bot.event
async def on_command(ctx):
    print("[command] " + ctx.message.content[len("="):].strip() + " / " + str(ctx.guild))
    return

#owner check
def is_owner():
    async def predicate(ctx):
        return ctx.author.id == ownerid
    return commands.check(predicate)

#TenshiBot Hangout check
def is_hangout():
    async def predicate(ctx):
        return ctx.guild.id == 273086604866748426
    return commands.check(predicate)
    
#help command
@bot.command()
async def help(ctx):
    hlp = open("txt/help.txt", "r")
    help_cmd = hlp.read()
    await ctx.send(help_cmd)

#misc commands
    
@bot.command()
@is_owner()
async def kickme(ctx):
    await ctx.send('Say no more')
    await ctx.author.kick(reason='asked for it')

@bot.command()
async def blech(ctx):
    await ctx.send('<:cirblech:415143187762511872>')

#loader/server info commands

@bot.command()
async def gameloader(ctx):
    hlp = open("txt/gameloader_info.txt", "r")
    help_cmd = hlp.read()
    await ctx.send(help_cmd)

@bot.command()
async def teknoparrot(ctx):
    hlp = open("txt/tp_info.txt", "r")
    help_cmd = hlp.read()
    await ctx.send(help_cmd)

@bot.command()
async def spicetools(ctx):
    #foreign channel checks
    #id's aren't hardcoded as the channels may be deleted and remade which would break an id check

    #CN
    if str(ctx.channel) == '中文':
        await ctx.send('CN_spicestring')
    #JP
    if str(ctx.channel) == '日本語':
        await ctx.send('JP_spicestring')
    #KR
    if str(ctx.channel) == '한국어':
        await ctx.send('KR_spicestring')
    else:
        await ctx.send('Spicetools can be downloaded from ' + spiceURL)

@bot.command()
async def bemanitools(ctx):
    await ctx.send('Bemanitools can be downloaded from http://tools.bemaniso.ws/bemanitools-v5.28.zip')
    await ctx.send('(if this is out of date replace 5.28 with the correct number e.g 5.29)')     

@bot.command()
async def xrpcv(ctx):
    await ctx.send('Xrpcv can be downloaded from http://193.70.38.209/file/xrpcv_2202.7z')
    await ctx.send('Alternatively pen and paper can be used to write down scores')

@bot.command()
async def jconfig(ctx):
    await ctx.send('Jconfig can be downloaded from <#434222178922135553>. Be sure to read the readme')

#owner commands
@bot.command()
@is_owner()  
async def setstatus_stream(ctx, *, args):
    await bot.change_presence(activity=discord.Streaming(name= args, url='https://twitch.tv/99710'))

@bot.command()
@is_owner()  
async def setstatus(ctx, *, args):
    await bot.change_presence(activity=discord.Game(name= args))

@bot.command()
@is_owner()    
async def vpsreboot(ctx):
    #os.system("sudo reboot")
    os.system("shutdown -r -t 30")
    await ctx.send('Rebooting the VPS')

#console command
@bot.command()
@is_owner()
#freezes the bot!
async def console(ctx):
    cmd=ctx.message.content[len("<@571094749537239042> console"):].strip()
    result = subprocess.check_output([cmd], stderr=subprocess.STDOUT)
    #os.system(ctx.message.content)
    await ctx.send(result)    

#debug commands    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')    

@bot.command()
async def errortest(ctx):
    await()

#about
@bot.command()
async def about(ctx):
    second = time.time() - st
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)

    em = discord.Embed(title='Currently on ' + str(len(bot.guilds)) + ' servers', description='Uptime= %d weeks,' % (week) + ' %d days,' % (day) + ' %d hours,' % (hour) + ' %d minutes,' % (minute) + ' and %d seconds.' % (second) + '\n Created by Rumia', colour=0x00ffff)
    em.set_author(name='1CCBot ' + bot_version , icon_url=bot.user.avatar_url)
    await ctx.send(embed=em)

@bot.command()
async def rate(ctx):
    await ctx.send("I rate it " + str(randint(0,10)) + "/10")

@bot.command()
async def md(ctx, arg):
    await ctx.send("`" + arg + "`")

@bot.command()
async def emote(ctx, arg):
    await ctx.send("<" + arg + ">")

@bot.command()
@is_owner()
async def say(ctx, *, args):
    await ctx.send(args)

@bot.command()
@is_owner()
async def dsay(ctx, *, args):
    await ctx.send(args)
    await ctx.message.delete()

#tkn = open("Tokens/tenshi_debug.txt", "r")
tkn = open("Tokens/tenshi_production.txt", "r")
token = tkn.read()
tkn.close()    
bot.run(token, bot=True, reconnect=True)