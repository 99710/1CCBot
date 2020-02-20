#1ccbot created by 99710
#based on TB 2.0.9

##Parameters##

#Version
bot_version = '1.1 R2'

#owner id
ownerid = 166189271244472320

#debug switch
debugmode = False

#Spicetools URL
spiceURL = "http://onlyone.cab/downloads/spicetools-latest.zip"

#Bemanitools URL
btoolURL = "http://tools.bemaniso.ws/bemanitools-v5.29.zip"

#segatools URL
stoolURL = "http://example.com"

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

Roles = [
"green",     
"light green",    
"dark green",
]

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
secure_random = random.SystemRandom()

user_blacklist = open("txt/badactors.txt", "r")
badactors = user_blacklist.read()

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
    
    if str(message.author.id) in badactors and "hdd" in contents.lower():
        print("user triggered HDD check but id is whitelisted")
        #await message.channel.send('id ignored')
        return
    
#game hdd checks
    if "iidx hdd" in contents.lower():  
        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "sdvx hdd" in contents.lower(): 
        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "ddr hdd" in contents.lower():   
        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "popn hdd" in contents.lower():   
        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "jubeat hdd" in contents.lower():   
        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

#    if "generic hdd" in contents.lower():   
#        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
#        return
    
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
async def kickme(ctx):
    await ctx.send('You will be kicked in 10 seconds')
    await asyncio.sleep(10)
    await ctx.author.kick(reason='asked for it')

@bot.command()
async def blech(ctx):
    await ctx.send('<:cirblech:415143187762511872>')

@bot.command()
@is_owner()
async def getrole(ctx):
    print ('[Debug] Giving user role')
    user=ctx.message.author
    role=discord.utils.get(ctx.guild.roles, name=secure_random.choice(Roles))
    await user.add_roles(role, reason='User introduced themselves')

#loader/server info commands

@bot.command()
@is_owner()
async def gameloader(ctx):
    hlp = open("txt/gameloader_info.txt", "r")
    help_cmd = hlp.read()
    await ctx.send(help_cmd)

@bot.command()
@is_owner()
async def teknoparrot2(ctx):
    hlp = open("txt/tp_info.txt", "r")
    help_cmd = hlp.read()
    await ctx.send(help_cmd)

@bot.command()
@is_owner()
async def teknoparrot(ctx):
    await ctx.send('Teknoparrot can be downloaded from https://teknoparrot.com/')
    await ctx.send('(Check <#434222178922135553> to see if your game is supported by jconfig first)')

@bot.command()
@commands.cooldown(1, 90, commands.BucketType.default)
async def spicetools(ctx):
    #foreign channel checks
    #id's aren't hardcoded as the channels may be deleted and remade which would break an id check

    #CN
    if str(ctx.channel) == '中文':
        #await ctx.send('您可以从下载 ' + spiceURL)
        #await ctx.send('您可以从 ' + spiceURL + ' 下载')
        await ctx.send('请稍等片刻...')
        r = requests.get(spiceURL)
        with open('Spicetools.zip', 'wb') as f:
            f.write(r.content)
        await ctx.send(file=discord.File('Spicetools.zip'))
        return
    #JP
    if str(ctx.channel) == '日本語':
        #await ctx.send(spiceURL + ' からダウンロードできます')
        await ctx.send('お待ちください...')
        r = requests.get(spiceURL)
        with open('Spicetools.zip', 'wb') as f:
            f.write(r.content)
        await ctx.send(file=discord.File('Spicetools.zip'))
        return
    #KR
    if str(ctx.channel) == '한국어':
#        await ctx.send(spiceURL +' 에서 얻을 수 있습니다')
        await ctx.send('기다려주세요 ...')
        r = requests.get(spiceURL)
        with open('Spicetools.zip', 'wb') as f:
            f.write(r.content)
        await ctx.send(file=discord.File('Spicetools.zip'))
        return
    else:
        await ctx.send('Spicetools can be downloaded from ' + spiceURL)
        return

@bot.command()
async def bemanitools(ctx):
    #foreign channel checks
    #id's aren't hardcoded as the channels may be deleted and remade which would break an id check

    #CN
    if str(ctx.channel) == '中文':
        #await ctx.send('您可以从下载 ' + spiceURL)
        await ctx.send('您可以从 ' + btoolURL + ' 下载')
        return
    #JP
    if str(ctx.channel) == '日本語':
        await ctx.send(btoolURL + ' からダウンロードできます')
        return
    #KR
    if str(ctx.channel) == '한국어':
        await ctx.send(btoolURL +' 에서 얻을 수 있습니다')
        return
    else:
        await ctx.send('Bemanitools can be downloaded from ' + btoolURL)
        return     

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

    em = discord.Embed(title='Currently on ' + str(len(bot.guilds)) + ' servers', description='Uptime= %d weeks,' % (week) + ' %d days,' % (day) + ' %d hours,' % (hour) + ' %d minutes,' % (minute) + ' and %d seconds.' % (second) + '\n Created by 99710', colour=0x00ffff)
    em.set_author(name='1CCBot V' + bot_version , icon_url=bot.user.avatar_url)
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
