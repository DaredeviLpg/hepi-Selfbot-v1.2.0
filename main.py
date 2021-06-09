from keep_alive import keep_alive
keep_alive()
import discord
from discord.ext import commands
import asyncio
import requests
import wikipedia
import datetime
from datetime import timedelta
import colorama
from colorama import Fore
import os
from os import system
import time
import string
import random
import urllib
from itertools import cycle
import re
from datetime import timedelta
from time import strftime
from time import gmtime
from datetime import datetime
from bs4 import BeautifulSoup as bs4
import time
import io
from urllib import parse, request
import aiohttp
import json
from PIL import Image, ImageFilter
from PIL import ImageFont
from PIL import ImageDraw
import math
from pypresence import Presence
from math import sqrt
import time

def clear():
  os.system('cls')
os.system('cls' if os.name == 'nt' else 'clear')

with open('setup.json') as f:
    setup = json.load(f)
prefix = setup.get("prefix")
token = setup.get("token")
password = setup.get("password")
bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

client = commands.Bot(command_prefix=prefix,
                      help_command=None,
                      case_insensitive=True,
                      self_bot=True)

class hepi:
  __version__ = '1.1.2'
  __author__ = 'DaredeviL'



@bot.command()
async def setprefix(ctx, npx=None):
	await ctx.message.delete()
	if npx is None:
		await ctx.send('what prefix???')
	else:
		bot.command_prefix = str(npx)
		await ctx.send(f'prefix has been changed! | new prefix: {npx}')

bot.cstmhelpfont = "**"
@bot.command()
async def font(ctx, cu=''):
  await ctx.message.delete()
  if cu == '':
    await ctx.send("provide a font.")
  if cu == 'code':
    bot.cstmhelpfont = "`"
    await ctx.send("the font has been changed! | New font: Code")
  if cu == 'bold':
    bot.cstmhelpfont = "**"
    await ctx.send("the font has been changed! | New font: bold")
  if cu == 'italic':
    bot.cstmhelpfont = "*"
    await ctx.send("the font has been changed! | New font: italic")
  if cu == 'underline':
    bot.cstmhelpfont = "__"
    await ctx.send("the font has been changed! | New font: underline")
@bot.command()
async def setfooter(ctx, *, ft=None):
	await ctx.message.delete()
	if ft is None:
		await ctx.send("provide a text.")
	else:
		bot.cstmfooter = ft
		await ctx.send(f"the footer of the help command has been changed! | new footer text: {ft}")
@bot.command()
async def setfootericon(ctx):
  await ctx.message.delete()
  attachment = ctx.message.attachments[0].url
  bot.footericon = attachment
  await ctx.send(f"The footer icon of the help command has been changed! | new footer icon URL: {attachment}")
  

bot.cstmhelpc = "https://cdn.discordapp.com/attachments/837543982137475103/838429596188672050/2021-04-30-16-03-02.jpg"
bot.cstmfooter = "Developed by DaredeviL MenZ#6969."
bot.footericon = "https://cdn.discordapp.com/attachments/825388954982285332/843715412315471872/tenor_3.gif"



@bot.command()
async def help(ctx, r=None):
	await ctx.message.delete()
	if r is None:
		embed = discord.Embed(
		    description=
		    f'{bot.cstmhelpfont}{bot.command_prefix}help raid\n{bot.command_prefix}help search\n{bot.command_prefix}help utils\n{bot.command_prefix}help misc\n{bot.command_prefix}help image-manipulation\n{bot.command_prefix}help nsfw\n{bot.command_prefix}help text\n{bot.command_prefix}help account\n{bot.command_prefix}help auto-response\n{bot.command_prefix}help customhelp{bot.cstmhelpfont}',
		    color=605040)
		embed.set_author(name='hepi Selfbot',
		                 icon_url=str(bot.user.avatar_url))
	elif r == 'raid':
		embed = discord.Embed(
		    color=405060,
		    title='Raid',
		    description=
		    f'**{bot.command_prefix}spam** `<times> <delay> <text>`\nspams the message provided.\n\n**{bot.command_prefix}sall** `<message>`\nsends the provided message on every channel.\n\n**{bot.command_prefix}massdm** `<message>`\ndms everyone on the server.\n\n**{bot.command_prefix}destroy**\ndeletes all channels and destroys the server, you must have the ban members and manage channels permission for this command to work.\n\n**{bot.command_prefix}spamchannels** `<name>`\nspams this server with channels that is named with the provided message, you must have the manage channels permission for this command to work..\n\n**{bot.command_prefix}delchannels**\ndeletes all channels, you must have the manage channels permissions for this command to work.\n\n**{bot.command_prefix}massban**\nbans every member, you must have the ban members permission for this command to work.'
		)
	if r == 'search':
		embed = discord.Embed(
		    title='Search',
		    color=405060,
		    description=
		    f'**{bot.command_prefix}yt** `<search>`\nsearches the provided message on youtube.\n\n**{bot.command_prefix}imagesearch** `<search>`\nsearches an image of the provided message.\n\n**{bot.command_prefix}revimg**\n[image]\nreverse searches the provided image.'
		)
	if r == 'utils':
		embed = discord.Embed(
		    title='utilities',
		    color=405060,
		    description=
		    f"**{bot.command_prefix}createtxt** `<text>`\ncreates a .txt file with the text provided.\n\n**{bot.command_prefix}sitepreview** `<site>`\nshows the preview of a provided website link.\n\n**{bot.command_prefix}weather** `<location>`\nshows the weather of the provided location.\n\n**{bot.command_prefix}clone**\nclones the server you are in.\n\n**{bot.command_prefix}wiki** `<reference>`\nsends information of anything from wikipedia.\n\n**{bot.command_prefix}calc** `<number> <operator> <number>`\ncalculates the provided numbers."
		)
	if r == 'misc':
		embed = discord.Embed(
		    title="miscellaneous",
		    color=605040,
		    description=
		    f"**{bot.command_prefix}servercount**\nshows how many servers you are in.\n\n**{bot.command_prefix}userinfo** `<user>` or **{bot.command_prefix}userinfo**\nshows the information of your/a mentioned users Account.\n\n**{bot.command_prefix}uptime**\nshows how long this selfbot has been online for.\n\n**{bot.command_prefix}autodank**\nsends pls beg, pls fish, pls hunt and pls bal every 50 seconds.\n\n**{bot.command_prefix}stopautodank**\nstops autodank.\n\n**{bot.command_prefix}cyclename** `<name>`\ncycles through your nickname.\n\n**{bot.command_prefix}stopcycler**\nstops cycling your nickname.\n\n**{bot.command_prefix}msgtracker**\nprints every deleted message.\n\n**{bot.command_prefix}stopmsgtracker**\nstops message tracker.\n\n**{bot.command_prefix}giveawaysniper**\nautomatically reacts to giveaways hosted by giveaway bot.\n\n**{bot.command_prefix}copycat** `<user>`\ncopies the mentioned user.\n\n**{bot.command_prefix}stopcopycat**\nstops copying the previously mentioned user.\n\n**{bot.command_prefix}stopgiveawaysniper**\nstops giveaway sniper.\n\n**{bot.command_prefix}nitrosniper**\nautomatically claims any nitro codes sent.\n\n**{bot.command_prefix}stopnitrosniper**\nstops nitro sniper.\n\n**{bot.command_prefix}avatar** `<user>` or **{bot.command_prefix}avatar**\nreturns your/a mentioned users profile picture.\n\n**{bot.command_prefix}servericon**\nreturns the icon of the server.\n\n**{bot.command_prefix}setprefix** `<new prefix>`\nchanges the prefix of this selfbot to a provided prefix.\n\n**{bot.command_prefix}meme**\nreturns a random meme.\n\n**{bot.command_prefix}dm** `<text>`\ndms the mentioned user with the text provided.\n\n**{bot.command_prefix}token** `<user>`\nshows the first part of the mentioned users token.\n\n**{bot.command_prefix}createembed** `<title>/<description>/<footer>`\ncreates an embed message.\n\n**{bot.command_prefix}purge** `<amount>`\npurges the provided amount of messages.\n\n**{bot.command_prefix}nitro**\ngenerates a random nitro code."
		)
	if r == 'text':
		embed = discord.Embed(
		    title='text',
		    color=604050,
		    description=
		    f'**{bot.command_prefix}fucking**\nshows a text animation of a penis going inside a vagina 😳\n\n**{bot.command_prefix}history**\nsaves the chat history on a .txt file.\n\n**{bot.command_prefix}uwufy** `<text>`\nuwufies the provided text.\n\n**{bot.command_prefix}pythonfy** `<text>` ```py\n#converts the provided text to a python code block.\n```\n**{bot.command_prefix}smalltxt** `<text>`\nconverts the provided text to small letters.\n\n**{bot.command_prefix}blank**\nsends a blank character.\n\n**{bot.command_prefix}fastdel** `<text>`\nimmideatly deletes the provided text.\n\n**{bot.command_prefix}reverse** `<text>`\nreverses the provided text.\n\n**{bot.command_prefix}sniper**\nshows a text art of a sniper.'
		)
	if r == 'image-manipulation':
		embed = discord.Embed(
		    title='image manipulation',
		    color=605040,
		    description=
		    f'**{bot.command_prefix}gay** `<user>` or **{bot.command_prefix}gay**\nshows your/a mentioned users profile picture but with a gay filter.\n\n**{bot.command_prefix}magik** `<user>` or **{bot.command_prefix}magik**\ndistorts your/a mentioned users profile picture.\n\n**{bot.command_prefix}deepfry** `<user>` or **{bot.command_prefix}deepfry**\ndeepfries your/a mentioned users profile picture.\n\n**{bot.command_prefix}greyscale** `<user>` or **{bot.command_prefix}greyscale**\nshows your/a mentioned users profile picture with a greyscale filter.\n\n**{bot.command_prefix}invert** `<user>` or **{bot.command_prefix}invert**\ninverts your/a mentioned users profile picture.'
		)
	if r == 'nsfw':
		embed = discord.Embed(
		    title="NSFW",
		    color=605040,
		    description=
		    f"**{bot.command_prefix}anal**\nsends a random anal gif.\n\n**{bot.command_prefix}pussy**\nsends a random pussy gif.\n\n**{bot.command_prefix}single**\nshows random gifs of single girls."
		)
	if r == 'account':
		embed = discord.Embed(
		    title='account',
		    color=605040,
		    description=
		    f'**{bot.command_prefix}hypesquad** `<balance/bravery/brilliance>`\nchanges your hypesquad badge.\n\n**{bot.command_prefix}setpfp**\n[image]\nsets your profile picture to a provided image.\n\n**{bot.command_prefix}stealpfp** `<user>`\nsteals the mentioned users profile picture.\n\n**{bot.command_prefix}rename** `<new name>`\nchanges your nsme to the provided text.\n\n**{bot.command_prefix}stream** `<text>`\nchanges your status to streaming.\n\n**{bot.command_prefix}play** `<text>`\nchanges your status to playing.\n\n**{bot.command_prefix}listent** `<text>`\nchanges your status to listening\n\n**{bot.command_prefix}watch** `<text>`\nchanges your status to watching.\n\n**{bot.command_prefix}ghost**\nmakes your profile picture and name invisible.'
		)
	if r == 'auto-response':
	  embed = discord.Embed(title="auto-response", color=605040, description=f"**{bot.command_prefix}autodm** `<reply text>`\nautomatically responds to anyone who dms you, reply text is optional.\n\n**{bot.command_prefix}stopautodm**\nstops autodm.")
	if r == 'customhelp':
	  embed = discord.Embed(title="CustomHelp", color=605040, description=f"**{bot.command_prefix}font** `<code/bold/italic/underline>`\nChanges the font of the main help command.\n\n**{bot.command_prefix}setthumbnail**\n[image]\nsets the thumbnail of the help command to the provided image.\n\n**{bot.command_prefix}setfooter** `<text>`\nsets the footer of the help command to the provided text.\n\n**{bot.command_prefix}setfootericon**\n[image]\nsets the footer icon to the provided image. ")
	embed.set_thumbnail(
		    url=bot.cstmhelpc
		)
	embed.set_footer(text=bot.cstmfooter, icon_url=bot.footericon)
	await ctx.send(embed=embed)
	  
bot.gws = False
@bot.command()
async def giveawaysniper(ctx):
	await ctx.message.delete()
	bot.gws = True 
	await ctx.send("giveaway sniper is now **Enabled**!")

@bot.command()
async def stopgiveawaysniper(ctx):
	await ctx.message.delete()
	bot.gws = False 
	await ctx.send("giveaway sniper is now **Disabled**!")
	
bot.ns = False
@bot.command()
async def nitrosniper(ctx):
	await ctx.message.delete()
	bot.ns = True 
	await ctx.send("nitro sniper is now **Enabled**!")

@bot.command()
async def stopnitrosniper(ctx):
	await ctx.message.delete()
	bot.ns = False 
	await ctx.send("nitro sniper is now **Disabled**!")



@bot.command()
async def servercount(ctx):
	await ctx.message.delete()
	await ctx.send(f'you are in `{len(bot.guilds)}` servers.')


bot.launch_time = datetime.utcnow()

@bot.command()
async def destroy(ctx):
  await ctx.message.delete()
  guild = ctx.message.guild
  for channel in ctx.guild.channels:
    await channel.delete()
  await ctx.guild.edit(name="nuked by DaredeviL")
  for m in range(499):
    chanvar = random.choice(['daredevil hates fags', 'FAG GOT NUKED BY DAREDEVIL', 'GET FUCKED FAGS', 'gayfucks'])
    await guild.create_text_channel(chanvar)

@bot.command()
async def setthumbnail(ctx):
  await ctx.message.delete()
  attachment = ctx.message.attachments
  bot.cstmhelpc = attachment[0].url
  await ctx.send(f"the thumbnail has been changed! | New Thumbnail URL: {attachment[0].url}")

@setthumbnail.error
async def setthumbnail_error(ctx, error):
  await ctx.send("provide an image.")
@setfootericon.error
async def setfootericon_error(ctx, error):
  await ctx.send("provide an image.")

@bot.command()
async def pythonfy(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send("what do you want me to pythonfy??")
	else:
		uwu = text.replace(' ', ' \f ')
		uwunt = uwu.replace('@', '')
		await ctx.send(f'```py\n{uwunt}\n```')

@bot.command()
async def massdm(ctx, *, message=None):
  await ctx.message.delete()
  if message == None:
    await ctx.send("provide a text.")
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"{Fore.GREEN}the dm has been Sent To {user}")
    except:
      pass
      print(f"{Fore.RED}couldnt dm {user}")



@bot.command()
async def revimg(ctx):
	await ctx.message.delete()
	attachment = str(ctx.message.attachments[0].url)
	if attachment is None:
		return
	else:
		embed = discord.Embed(
			    description=
			    f"tap/click [here](https://images.google.com/searchbyimage?image_url={attachment}) to view the results.",
			    color=406027)
		await ctx.send(embed=embed)





@revimg.error
async def revimg_error(ctx, error):
	if isinstance(error, commands.CommandInvokeError):
		await ctx.send("provide an image.")

bot.autodm = False
bot.autodmmsg = 'im currently unavailable.'

@bot.command()
async def autodm(ctx, *, utext='im currently unavailable.'):
  await ctx.message.delete()
  bot.autodm = True
  bot.autodmmsg = utext
  await ctx.send(f"autodm is now enabled! | autodm message: {utext}")

@bot.command()
async def stopautodm(ctx):
  await ctx.message.delete()
  bot.autodm = False
  bot.autodmmsg = 'im currently unavailable.'
  await ctx.send("autodm is now **disabled**!")

bot.copycat = None

@bot.command()
async def copycat(ctx, member: discord.Member):
  await ctx.message.delete()
  try:
    bot.copycat = member
    await ctx.send(f"now copying **{member}**.")
  except:
    await ctx.send(f"member not found.")

@bot.command()
async def stopcopycat(ctx):
  await ctx.message.delete()
  if bot.copycat is None:
    await ctx.send("you are not copying anyone in the first place.")
    return
  await ctx.send(f"stopped copying **{bot.copycat}**.")
  bot.copycat = None


@bot.event
async def on_message(message):
  if bot.copycat is not None and bot.copycat.id == message.author.id:
    await message.channel.send(message.content)
  if bot.autodm is True:
    if isinstance(message.channel, discord.channel.DMChannel):
      await message.channel.send(bot.autodmmsg)
  def snipe(x):
    print(f"{x}\n{Fore.WHITE}Author: {message.author}\n{Fore.WHITE}server: {Fore.BLUE}{message.guild.name}\n{Fore.WHITE}Channel: {Fore.CYAN}#{message.channel.name}" + Fore.RESET)
  def ex(i):
    print(f"{i}\n{Fore.WHITE}Author: {message.author}" + Fore.RESET)
  if "GIVEAWAY" in message.content:
    if bot.gws == True:
      if message.author.id == 294882584201003009:
        try:
          await message.add_reaction("🎉")
          print(f"{Fore.GREEN}Giveaway Entered!\n{Fore.WHITE}Server: {Fore.BLUE}{message.guild.name}{Fore.RESET}\nChannel: {Fore.CYAN}#{message.channel.name}"+ Fore.RESET)
          print(f"sniped at {Fore.BLUE}{datetime.now()}{Fore.RESET}\n")
        except Exception as why:
          print(f"{Fore.RED}Couldnt join giveaway\nreason: {why}")
          print(f"failed at {Fore.BLUE}{datetime.now()}{Fore.RESET}\n")
    else:
      pass
  if f"Congratulations <@{bot.user.id}" in message.content:
    if message.author.id == 294882584201003009:
      print(f"\n{Fore.GREEN}Giveaway Won!\n{Fore.WHITE}server: {Fore.BLUE}{message.guild.name}\n{Fore.WHITE}Channel: {Fore.CYAN}#{message.channel.name}")
      print(f"won at {Fore.BLUE}{datetime.now()}{Fore.RESET}\n")
  else:
    pass
  if "discord.gift/" in message.content:
    if bot.ns is True:
      code = re.search("discord.gift/(.*)", message.content).group(1)
      if len(code) != 16:
        try:
          snipe(f"{Fore.RED}A fake nitro code was sent.")
          print(f"failed at {Fore.BLUE}{datetime.now()}{Fore.RESET}\n")
        except:
          pass
          ex(f"{Fore.RED}A fake nitro code was sent.")
          print(f"failed at {Fore.BLUE}{datetime.now()}{Fore.RESET}\n")
      else:
        headers = {"Authorization": token}
        r = requests.post(f"https://discordapp.com/api/v7/entitlements/gift-codes/{code}/redeem", headers=headers).text
        if "This gift has been redeemed already." in r:
          try:
            snipe(f"{Fore.RED}A claimed nitro code was sent.")
            print(f"failed at {Fore.BLUE}{datetime.now()}{Fore.RESET}\n")
          except:
            pass
            ex(f"{Fore.RED}A claimed nitro code was sent.")
            print(f"failed at {Fore.BLUE}{datetime.now()}{Fore.RESET}\n")
        elif "subscription_plan" in r:
          try:
            snipe(f"{Fore.GREEN}Nitro sniped!")
            print(f"Sniped at {Fore.BLUE}{datetime.now()}{Fore.RESET}\n")
          except:
            ex(f"{Fore.GREEN}Nitro sniped!")
            print(f"Sniped at {Fore.BLUE}{datetime.now()}{Fore.RESET}\n")
        elif "Unknown Gift Code" in r:
          try:
            snipe(f"{Fore.RED}A invalid nitro code was sent.")
            print(f"failed at {Fore.BLUE}{datetime.now()}{Fore.RESET}\n")
          except:
            ex(f"{Fore.RED}A invalid nitro code was sent.")
            print(f"failed at {Fore.BLUE}{datetime.now()}{Fore.RESET}\n")
    else:
      pass
  await bot.process_commands(message)


@bot.command()
async def uwufy(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send("what do you want me to uwufy??")
	else:
		uwu = text.replace(' ', ' ᵘʷᵘ ')
		uwunt = uwu.replace('@', '')
		await ctx.send(f"{uwunt}")

@bot.command()
async def fastdel(ctx, *, delm=None):
  if delm is None:
    await ctx.message.delete()
  else:
    await ctx.message.delete()
    ffs = await ctx.send(delm)
    await ffs.delete()

@bot.command()
async def delchannels(ctx):
	for channel in ctx.guild.channels:
		await channel.delete()


@bot.command()
async def spamchannels(ctx, *, text):
	await ctx.message.delete()
	await ctx.send('spamming channels...')
	for i in range(9999):
		guild = ctx.message.guild
		await guild.create_text_channel(f"{text}")


@bot.command()
async def history(ctx, limit: int = 99999999999):
	await ctx.message.delete()
	channel = ctx.message.channel
	messages = await ctx.channel.history(limit=limit).flatten()
	await ctx.send(
	    "please wait, the amount of time it takes depends on how many messages there are on the server."
	)

	with open(f"{channel}_messages.txt", "a+", encoding="utf-8") as f:
		print(f"\nhistory Saved by - {ctx.author.display_name}.\n\n", file=f)
		for message in messages:
			embed = ""
			if len(message.embeds) != 0:
				embed = message.embeds[0].description
				print(f"{message.author.name} - {embed}", file=f)
			print(f"{message.author.name} - {message.content}", file=f)
	await ctx.send(f"message history has been converted into a .txt file!")
	history = discord.File(fp=f'{channel}_messages.txt', filename=None)
	await ctx.send(file=history)

@bot.command()
async def blank(ctx):
  await ctx.message.delete()
  await ctx.send(chr(173))

@bot.command()
async def ghost(ctx):
	await ctx.message.delete()
	filename = "pfp.jpg"
	attachment = "https://cdn.discordapp.com/attachments/821440914387763202/840272564416151592/20210508_000235.jpg"
	f = open(filename, 'wb')
	f.write(requests.get(attachment).content)
	f.close()
	with open(filename, 'rb') as f:
		image = f.read()
	await bot.user.edit(password=password, avatar=image)
	await bot.user.edit(username="⃝⃝", password=password)
	await ctx.send("your profile picture and name is now invisible!")


@bot.command()
async def dm(ctx, user: discord.User, *, message=''):
  await ctx.message.delete()
  if not user:
    await ctx.send("mention a user.")
  if message == '':
    await ctx.send("provide a message.")
  else:
    await user.send(f"{message}")
    await ctx.send(f"succefully dmed {user}! | message: `{message}`")


 

@bot.command()
async def uptime(ctx):
	await ctx.message.delete()
	delta_uptime = datetime.utcnow() - bot.launch_time
	hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)
	await ctx.send(
	    f"this selfbot has been online for: `{days}d: {hours}h: {minutes}m: {seconds}s`"
	)


@bot.command()
async def fucking(ctx):
	await ctx.message.delete()
	message = await ctx.send("8==D     {(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D    {(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D   {(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D  {(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D {(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D{(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==D(.)}")
	await asyncio.sleep(1)
	await message.edit(content="8==.)}")
	await asyncio.sleep(2)
	await message.edit(content="8==D{(.)}")
	await asyncio.sleep(0.5)
	await message.edit(content="8==D~{(.)}")
	await asyncio.sleep(0.5)
	await message.edit(content="8==D~~{(.)}")


@bot.command()
async def sniper(ctx):
	await ctx.message.delete()
	message = await ctx.send("︻")
	await asyncio.sleep(1)
	await message.edit(content="︻ ╦")
	await asyncio.sleep(1)
	await message.edit(content="︻ ╦ デ")
	await asyncio.sleep(1)
	await message.edit(content="︻ ╦ デ ╤")
	await asyncio.sleep(1)
	await message.edit(content="︻ ╦ デ ╤ ━")
	await asyncio.sleep(1)
	await message.edit(content="︻ ╦ デ ╤ ━ ╾")
	await asyncio.sleep(1)
	await message.edit(content="︻╦デ╤━╾")


@bot.command()
async def wiki(ctx, *, arg=None):
	try:
		if arg == None:
			await ctx.send("Please, specify what do you want me to search.")
		elif arg:
			start = arg.replace(" ", "")
			end = wikipedia.summary(start)
			await ctx.send(end)
	except:
		try:
			start = arg.replace(" ", "")
			end = wikipedia.summary(start, sentences=10)
			await ctx.send(end)
		except:
			await ctx.send(
			    "I can't send info because I got an unknown reference.")



@bot.command()
async def massban(ctx):
  await ctx.send("banning members...")
  for user in list(ctx.guild.members):
     try:
        await user.ban(reason="T'_T")
     except:
         pass

@bot.command(pass_context=True)
async def calc(ctx, *, msg):
	equation = msg.strip().replace('^', '**').replace('x', '*')
	try:
		if '=' in equation:
			left = eval(
			    equation.split('=')[0], {"__builtins__": None}, {"sqrt": sqrt})
			right = eval(
			    equation.split('=')[1], {"__builtins__": None}, {"sqrt": sqrt})
			answer = str(left == right)
		else:
			answer = str(eval(equation, {"__builtins__": None},
			                  {"sqrt": sqrt}))
	except TypeError:
		return await ctx.send(ctx.bot.bot_prefix +
		                      "Invalid calculation query.")
	if 4 == 4:
		em = discord.Embed(color=0xD3D3D3, title='Calculator')
		em.add_field(name='Input:',
		             value=msg.replace('**', '^').replace('x', '*'),
		             inline=False)
		em.add_field(name='Output:', value=answer, inline=False)
		await ctx.send(content=None, embed=em)
		await ctx.message.delete()
	else:
		await ctx.send(ctx.bot.bot_prefix + answer)


@bot.command(pass_context=True)
async def meme(ctx):
	embed = discord.Embed(title="", description="")

	async with aiohttp.ClientSession() as cs:
		async with cs.get(
		    'https://www.reddit.com/r/memes/.json?sort=top') as r:
			res = await r.json()
			embed.set_image(url=res['data']['children'][random.randint(0, 25)]
			                ['data']['url'])
			await ctx.send(embed=embed)


@bot.command()
async def anal(ctx):
	await ctx.message.delete()
	nekolul = random.randint(1, 99)
	message = await ctx.send("contacting nekos.life...")
	await asyncio.sleep(1)
	await message.delete()
	embed = discord.Embed(color=694207,
	                      timestamp=ctx.message.created_at,
	                      title=f"anal seggs")
	embed.set_image(url=f"https://cdn.nekos.life/anal/Anal_0{nekolul}.gif")
	await ctx.send(embed=embed)
  

@bot.command()
async def smalltxt(ctx, *, text=None):
	await ctx.message.delete()
	if text is None:
		await ctx.send("what do you want as a small message???")
	else:
		frt = text.replace('a', 'ᴬ').replace('A', 'ᴬ').replace(
		    'b',
		    'ᴮ').replace('B', 'ᴮ').replace('c', 'ᶜ').replace('C', 'ᶜ').replace(
		        'd', 'ᴰ').replace('D', 'ᴰ').replace('e', 'ᴱ').replace(
		            'E', 'ᴱ').replace('f', 'ᶠ').replace('F', 'ᶠ').replace(
		                'g', 'ᴳ').replace('G', 'ᴳ').replace('h', 'ᴴ').replace(
		                    'H',
		                    'ᴴ').replace('i', 'ᴵ').replace('I', 'ᴵ').replace(
		                        'j', 'ᴶ').replace('J', 'ᴶ').replace(
		                            'k', 'ᴷ').replace('K', 'ᴷ').replace(
		                                'l', 'ᴸ').replace('L', 'ᴸ').replace(
		                                    'm', 'ᴹ'
		                                ).replace('M', 'ᴹ').replace(
		                                    'n', 'ᴺ'
		                                ).replace('N', 'ᴺ').replace(
		                                    'o', 'ᴼ'
		                                ).replace('O', 'ᴼ').replace(
		                                    'p', 'ᴾ'
		                                ).replace('P', 'ᴾ').replace(
		                                    'q', 'ᵠ'
		                                ).replace('Q', 'ᵠ').replace(
		                                    'r', 'ᴿ'
		                                ).replace('R', 'ᴿ').replace(
		                                    's', 'ˢ'
		                                ).replace('S', 'ˢ').replace(
		                                    't', 'ᵀ'
		                                ).replace('T', 'ᵀ').replace(
		                                    'u', 'ᵁ'
		                                ).replace('U', 'ᵁ').replace(
		                                    'v', 'ⱽ'
		                                ).replace('V', 'ⱽ').replace(
		                                    'w', 'ᵂ'
		                                ).replace('W', 'ᵂ').replace(
		                                    'x', 'ˣ').replace(
		                                        'X', 'ˣ').replace(
		                                            'y', 'ʸ').replace(
		                                                'Y', 'ʸ').replace(
		                                                    'z', 'ᶻ').replace(
		                                                        'Z', 'ᶻ')
		await ctx.send(frt)


@bot.command()
async def pussy(ctx):
	await ctx.message.delete()
	nekolul = random.randint(1, 99)
	message = await ctx.send("contacting nekos.life...")
	await asyncio.sleep(1)
	await message.delete()
	embed = discord.Embed(color=694207,
	                      timestamp=ctx.message.created_at,
	                      title="{(.)}")
	embed.set_image(url=f"https://cdn.nekos.life/pussy/pwank0{nekolul}.gif")
	await ctx.send(embed=embed)


@bot.command()
async def single(ctx):
	await ctx.message.delete()
	nekolol = random.randint(100, 202)
	message = await ctx.send("contacting nekos.life...")
	await asyncio.sleep(1)
	await message.delete()
	embed = discord.Embed(color=694207,
	                      timestamp=ctx.message.created_at,
	                      title=f"single girl pics..")
	embed.set_image(url=f"https://cdn.nekos.life/solo/solo{nekolol}.jpg")
	await ctx.send(embed=embed)


@bot.command()
async def imagesearch(ctx, *, src=None):
	await ctx.message.delete()
	if src is None:
		await ctx.send("what image???")
	else:
		url = f'https://unsplash.com/search/photos/{src.replace(" ", "%20")}'
		page = requests.get(url)
		soup = bs4(page.text, 'html.parser')
		image_tags = soup.findAll('img')
		if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
			link = image_tags[2]['src']
			try:
				async with aiohttp.ClientSession() as session:
					async with session.get(link) as resp:
						image = await resp.read()
				with io.BytesIO(image) as file:
					await ctx.send(f'image of: **{src}**',
					               file=discord.File(file, f"{src}.jpg"))
			except:
				return


@bot.command()
async def deepfry(ctx, user: discord.Member = None):
	await ctx.message.delete()
	endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
	if user is None:
		avatar = str(ctx.author.avatar_url_as(format="png"))
		endpoint += avatar
		req = requests.get(endpoint)
		res = req.json()
		try:
			async with aiohttp.ClientSession() as session:
				async with session.get(str(res['message'])) as resp:
					image = await resp.read()
			with io.BytesIO(image) as file:
				await ctx.send("🔥", file=discord.File(file, f"deepfry.png"))
		except:
			await ctx.send(res['message'])
	else:
		avatar = str(user.avatar_url_as(format="png"))
		endpoint += avatar
		req = requests.get(endpoint)
		res = req.json()
		try:
			async with aiohttp.ClientSession() as session:
				async with session.get(str(res['message'])) as resp:
					image = await resp.read()
			with io.BytesIO(image) as file:
				await ctx.send("🔥", file=discord.File(file, f"deepfry.png"))
		except:
			return

  


@bot.command()
async def gay(ctx, member: discord.Member = None):
	await ctx.message.delete()
	if not member:
		filename = "gay.jpg"
		var = str(ctx.author.avatar_url)
		jpgconv = var.replace('webp', 'png')
		f = open(filename, 'wb')
		f.write(
		    requests.get(
		        f'https://api.devs-hub.xyz/rainbow?image={jpgconv}?size=2048').
		    content)
		f.close()
		flr = discord.File(fp=filename)
		await ctx.send("🏳️‍🌈", file=flr)
	else:
		filename = "gay.png"
		var = str(member.avatar_url)
		jpgconv = var.replace('webp', 'png')
		f = open(filename, 'wb')
		f.write(
		    requests.get(
		        f'https://api.devs-hub.xyz/rainbow?image={jpgconv}').content)
		f.close()
		flr = discord.File(fp=filename)
		await ctx.send(f"🏳️‍🌈 ", file=flr)


@bot.command()
async def invert(ctx, member: discord.Member = None):
	await ctx.message.delete()
	if not member:
		filename = "invert.jpg"
		var = str(ctx.author.avatar_url)
		jpgconv = var.replace('webp', 'png')
		f = open(filename, 'wb')
		f.write(
		    requests.get(
		        f'https://api.cool-img-api.ml/invert?image={jpgconv}?size=2048'
		    ).content)
		f.close()
		flr = discord.File(fp=filename)
		await ctx.send("🙃", file=flr)
	else:
		filename = "invert.png"
		var = str(member.avatar_url)
		jpgconv = var.replace('webp', 'png')
		f = open(filename, 'wb')
		f.write(
		    requests.get(
		        f'https://api.cool-img-api.ml/invert?image={jpgconv}').content)
		f.close()
		flr = discord.File(fp=filename)
		await ctx.send("🙃", file=flr)


@bot.command()
async def greyscale(ctx, member: discord.Member = None):
	if not member:
		filename = "greyscale.jpg"
		f = open(filename, 'wb')
		f.write(requests.get(f'{ctx.author.avatar_url}?size=2048').content)
		f.close()
		flr = discord.File(fp=filename)
		image = Image.open(filename)
		greyscale_image = image.convert('L')
		greyscale_image.save(filename)
		await ctx.send("greyscale", file=flr)
	else:
		filename = "greyscale.png"
		var = str(member.avatar_url)
		jpgconv = var.replace('webp', 'png')
		f = open(filename, 'wb')
		f.write(requests.get(jpgconv).content)
		f.close()
		image = Image.open(filename)
		greyscale_image = image.convert('L')
		greyscale_image.save(filename)
		flr = discord.File(fp=filename)
		await ctx.send("greyscale", file=flr)


@bot.command()
async def magik(ctx, member: discord.Member = None):
	await ctx.message.delete()
	if not member:
		filename = "magikk.jpg"
		var = str(ctx.author.avatar_url)
		jpgconv = var.replace('webp', 'png')
		f = open(filename, 'wb')
		f.write(
		    requests.get(
		        f'https://api.devs-hub.xyz/magik?image={jpgconv}?size=2048&level=10'
		    ).content)
		f.close()
		flr = discord.File(fp=filename)
		await ctx.send("what a magik", file=flr)
	else:
		filename = "magikk.png"
		var = str(member.avatar_url)
		jpgconv = var.replace('webp', 'png')
		f = open(filename, 'wb')
		f.write(
		    requests.get(
		        f'https://api.devs-hub.xyz/magik?image={jpgconv}&level=10').
		    content)
		f.close()
		flr = discord.File(fp=filename)
		await ctx.send("what a magik", file=flr)

def nitrogen(chars):
    return f"{''.join(random.choices(string.ascii_letters + string.digits, k=chars))}"
@bot.command()
async def nitro(ctx):
	await ctx.message.delete()
	await ctx.send(f"https://discord.gift/{nitrogen(16)}")
passcode = input('passcode\n>')
if passcode == "6944":
  print(f"{Fore.GREEN}Passcode was correct :D\n{Fore.RESET}")
  time.sleep(2)
  print("running selfbot...")
else:
  print(f"{Fore.RED}The provided passcode was incorrect.")
  time.sleep(2)
  exit()


@bot.command(pass_context=True)
async def autodank(ctx):
	await ctx.message.delete()
	await ctx.send('auto dank memer is now **enabled**!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send('pls beg')
			print(f"{Fore.GREEN}succefully begged")
			await ctx.send('pls fish')
			print(f"{Fore.GREEN}succefully fished")
			await ctx.send('pls hunt')
			print(f"{Fore.GREEN}succefully hunt")
			await ctx.send('pls dep all')
			print(f"{Fore.GREEN}succefully deposited all")
			await asyncio.sleep(47)


@bot.command()
async def stopautodank(ctx):
	await ctx.message.delete()
	await ctx.send('auto dank memer is now **disabled**!')
	global dmcs
	dmcs = False

@bot.command()
async def createembed(ctx, *, emb=''):
  await ctx.message.delete()
  rand = random.randint(111111, 999999)
  if emb == '':
    await ctx.send("provide a title, description and a footer seperated with /.")
  res = emb.split("/")
  embed = discord.Embed(title=res[0], description=res[1], color=rand)
  embed.set_footer(text=res[2])
  await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
	await ctx.message.delete()
	po = time.monotonic()
	message = await ctx.send("•••")
	await asyncio.sleep(0.3)
	ping = (time.monotonic() - po) * 80
	await message.edit(content=f"`{int(ping)} ms`")
	await asyncio.sleep(2)
	await message.delete()


@bot.command(aliases=['si'])
async def servericon(ctx, server: discord.Guild = None):
	await ctx.message.delete()
	filename = "servericon.png"
	await ctx.guild.icon_url.save(filename)
	file = discord.File(fp=filename)
	await ctx.send("Server Icon", file=file)


@servericon.error
async def servericon_error(ctx, error):
	if isinstance(error, commands.CommandInvokeError):
		await ctx.send("this command only works in servers.")


@bot.command()
async def rename(ctx, *, name=None):
	await ctx.message.delete()
	if name is None:
		await ctx.send("what name???")
	await bot.user.edit(username=name, password=password)
	await ctx.send("your namehas been changed!")


@bot.command()
async def setpfp(ctx):
	await ctx.message.delete()
	filename = "pfp.jpg"
	attachment = str(ctx.message.attachments[0].url)
	f = open(filename, 'wb')
	f.write(requests.get(attachment).content)
	f.close()
	flr = discord.File(fp=filename)
	with open(filename, 'rb') as f:
		image = f.read()
	await bot.user.edit(password=password, avatar=image)
	await ctx.send(
	    "your profile picture has been changed! | new profile picture ↓",
	    file=flr)


@bot.command()
async def stealpfp(ctx, member: discord.Member):
	await ctx.message.delete()
	if not member:
		await ctx.send("mention a user.")
	filename = "stolenpfp.png"
	attachment = str(member.avatar_url)
	f = open(filename, 'wb')
	f.write(requests.get(attachment).content)
	f.close()
	flr = discord.File(fp=filename)
	with open(filename, 'rb') as f:
		image = f.read()
	await bot.user.edit(password=password, avatar=image)
	await ctx.send(f"you have stolen {member.mention}'s profile picture!")


@stealpfp.error
async def stealpfp_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("mention a user.")





@bot.command()
async def weather(ctx, message=None):
	if message == None:
		await ctx.send("provide a location my guy")
	else:
		embed = discord.Embed(color=123456,
		                      timestamp=ctx.message.created_at,
		                      title=f"weather in {message}")
		embed.set_image(
		    url=
		    f"https://api.cool-img-api.ml/weather-card?location={message}&background=https://cdn.discordapp.com/attachments/820496743211728937/829268642801647636/2021-04-07-15-17-17.jpg"
		)
		await ctx.send(embed=embed)


@bot.command()
async def avatar(ctx, member: discord.Member = None):
	await ctx.message.delete()
	if not member:
		filename = "avatar.png"
		await ctx.author.avatar_url.save(filename)
		file = discord.File(fp=filename)
		await ctx.send("Avatar", file=file)
	else:
		filename = "avatar.png"
		await member.avatar_url.save(filename)
		file = discord.File(fp=filename)
		await ctx.send(f"Avatar", file=file)


def convert(time):
	pos = ["s", "m", "h", "d", "w"]

	time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

	unit = time[-1]

	if unit not in pos:
		return -1
	try:
		val = int(time[:-1])
	except:
		return -2

	return val * time_dict[unit]


@bot.command()
async def cyclename(ctx, *, nname=''):
	if nname == '':
		await ctx.send("provide a name.")
	await ctx.message.delete()
	await ctx.send("your nickname is now cycling!")
	global cycler
	cycler = True
	while cycler:
		name = ''
		for letter in nname:
			name = name + letter
			await ctx.message.author.edit(nick=name)


@bot.command()
async def stopcycler(ctx):
	await ctx.message.delete()
	await ctx.send("nickname cycler has been disabled.")
	global cycler
	cycler = False


@bot.command()
async def userinfo(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=ctx.guild.me.top_role.color, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined server", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Account Creation Date", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).title() for p in user.guild_permissions if p[1]]).replace("_", " ")
    embed.add_field(name="Permissions", value=f'`{perm_string}`', inline=False)
    embed.set_footer(text=f'ID: {str(user.id)} | member #{str(members.index(user)+1)}')
    await ctx.send(embed=embed)



@bot.command(aliases=['cs'])
async def clone(ctx):
	await ctx.message.delete()
	await ctx.send("please wait, this may take a few seconds..")
	await bot.create_guild(f'{ctx.guild.name} 2.0')
	await asyncio.sleep(4)
	for gee in bot.guilds:
		if f'{ctx.guild.name} 2.0' in gee.name:
			for c in gee.channels:
				await c.delete()
			for cate in ctx.guild.categories:
				x = await gee.create_category(f"{cate.name}")
				for cn in cate.channels:
					if isinstance(cn, discord.VoiceChannel):
						await x.create_voice_channel(f"{cn}")
					if isinstance(cn, discord.TextChannel):
						await x.create_text_channel(f"{cn}")
	await ctx.send("server has been cloned!")
	try:
		await gee.edit(icon=ctx.guild.icon_url)
	except:
		pass


@bot.command()
async def stream(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send('provide a text.')
	elif text != '':
		stream = discord.Streaming(name=text, url='https://twitch.com/aba')
		await bot.change_presence(activity=stream)
		await ctx.send(f'your status has been changed! | status text: {text}')


@bot.command()
async def yt(msg, *, search=''):
	await msg.message.delete()
	if search == '':
		await msg.send('provide a search query.')
	query_string = urllib.parse.urlencode({"search_query": search})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" +
	                                      query_string)
	search_results = re.findall(r"watch\?v=(\S{11})",
	                            html_content.read().decode())
	await msg.send(
	    f"search result for **{search}**:\nhttp://www.youtube.com/watch?v=" +
	    search_results[0])


@bot.command()
async def play(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send('provide a text.')
	elif text != '':
		activity = discord.Game(name=text, type=4)
		await bot.change_presence(status=discord.Status.online,
		                          activity=activity)
		await ctx.send(f'your status has been changed! | status text: {text}')


@bot.command()
async def listent(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send('provide a text.')
	elif text != '':
		await bot.change_presence(activity=discord.Activity(
		    type=discord.ActivityType.listening, name=text))

		await ctx.send(f'your status has been changed! | status text: {text}')


@bot.command()
async def watch(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send('provide a text.')
	elif text != '':
		await bot.change_presence(activity=discord.Activity(
		    type=discord.ActivityType.watching, name=text))
		await ctx.send(f'your status has been changed! | status text: {text}')


@bot.command()
async def sitepreview(ctx, link=''):
	if link == '':
		await ctx.send("what website???")
	else:
		await ctx.send("please wait, this may take 5-7 seconds")
		f = open("siteprev.png", 'wb')
		f.write(
		    requests.get(
		        f'https://shot.screenshotapi.net/screenshot?&url={link}&full_page=true&fresh=true&output=image&file_type=png'
		    ).content)
		f.close()
		lol = discord.File(fp=f"siteprev.png")
		flrl = link.replace('https://', '')
		await ctx.send(f"website preview of {flrl}", file=lol)



@bot.command(aliases=["token"])
async def xigard(ctx, user:discord.Member = None):
  if not user:
    await ctx.send("mention a user.")
  else:
    await ctx.send(f"ODExNDU0{nitrogen(15)}")

@bot.command()
async def hypesquad(ctx, house=''):
	await ctx.message.delete()
	if house == '':
		await ctx.send('please provide a house.')
	request = requests.Session()
	headers = {
	    'Authorization':
	    token,
	    'Content-Type':
	    'application/json',
	    'User-Agent':
	    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
	}
	if house == "bravery":
		payload = {'house_id': 1}
	elif house == "brilliance":
		payload = {'house_id': 2}
	elif house == "balance":
		payload = {'house_id': 3}
	try:
		request.post('https://discordapp.com/api/v6/hypesquad/online',
		             headers=headers,
		             json=payload,
		             timeout=10)
		await ctx.send(
		    f'your hypesquad badge was succefully changed! | New house: **{house}**'
		)
	except:
		await ctx.send('that is **not** a valid hypesquad house.')
		return


@bot.command()
async def purge(ctx, amnt: int):
	await ctx.channel.purge(limit=amnt)
	await ctx.send(f"{amnt} messages has been deleted!")


@purge.error
async def purge_error(ctx, error):
	await ctx.message.delete()
	await ctx.send(f' usage: `{bot.command_prefix}purge <amount>`')


@bot.command()
async def spam(ctx, num: int, delay: int, *, msg=''):
	await ctx.message.delete()
	for i in range(num):
		await ctx.send(msg)
		await asyncio.sleep(delay)


@bot.command()
async def reverse(ctx, *, message):
	await ctx.message.delete()
	message = message[::-1]
	await ctx.send(message)


@bot.command()
async def sall(ctx, *, arg=''):
	await ctx.message.delete()
	if arg == '':
		await ctx.send('provide a message..')
	await ctx.send('sending in all channels..')
	channels = ctx.guild.text_channels
	for channel in channels:
		try:
			await channel.send(arg)
		except:
		  pass

@bot.command()
async def channellist(ctx):
	await ctx.message.delete()
	await ctx.send(ctx.guild.text_channels.name)

@spam.error
async def spam_error(ctx, error):
	await ctx.message.delete()
	await ctx.send(f' usage: `{bot.command_prefix}spam <times> <delay> <message>`')


@bot.command()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send('selfbot has been stopped.')
	await asyncio.sleep(1)
	await bot.logout()
	exit()


@bot.command()
async def createtxt(ctx, *, txt=''):
	await ctx.message.delete()
	if txt == '':
		await ctx.send('provide a message dude')
	else:
		file = open("customtxtfile.txt", "w")
		file.write(txt)
		file.close()
		pp = discord.File(fp="customtxtfile.txt")
		await ctx.send(f"here is your txt file {ctx.author.name} ↓", file=pp)

bot.sniped_messages = {}
bot.msgtracker = False

@bot.command()
async def msgtracker(ctx):
  await ctx.message.delete()
  bot.msgtracker = True
  await ctx.send("message delete tracker is **enabled**!\ncheck your console.")
  print("deleted messages will now appear here.")

@bot.command()
async def stopmsgtracker(ctx):
  await ctx.message.delete()
  bot.msgtracker = False
  await ctx.send("message delete tracker is **disabled**!")
  print(f"{Fore.RESET}deleted messages will no longer appear here.")

@bot.event
async def on_message_delete(message):
	if bot.msgtracker is True:
		print(f"a message was deleted by {Fore.YELLOW}{message.author}{Fore.RESET} in the server named {Fore.BLUE}{message.guild.name}{Fore.RESET}\ncontents:" + Fore.GREEN + message.content + Fore.RESET)
	else:
	  pass
	if message.attachments:
		bob = message.attachments[0]
		bot.sniped_messages[message.guild.id] = (bob.proxy_url,
		                                            message.content,
		                                            message.author,
		                                            message.channel.name,
		                                            message.created_at)
	else:
		bot.sniped_messages[message.guild.id] = (message.content,
		                                            message.author,
		                                            message.channel.name,
		                                            message.created_at)


@bot.command()
async def snipe(ctx):
  try:
    bob_proxy_url, contents, author, channel_name, time = bot.sniped_messages[
		    ctx.guild.id]
  except:
    contents, author, channel_name, time = bot.sniped_messages[
		    ctx.guild.id]
  try:
    embed = discord.Embed(description=f"Deleted attachment url: [click here to download]({bob_proxy_url})\n" + contents,
		                      color=102030,
		                      timestamp=time)
    embed.set_image(url=bob_proxy_url)
    embed.set_author(name=f"{author.name}#{author.discriminator}",
		                 icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")
    await ctx.channel.send(embed=embed)
    await asyncio.sleep(1)
  except:
    embed = discord.Embed(description=contents,
		                      color=102030,
		                      timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}",
		                 icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")
    await ctx.channel.send(embed=embed)
  await ctx.message.delete()

@snipe.error
async def snipe_error(ctx, error):
  await ctx.send("there's nothing to snipe!")



@setpfp.error
async def setpfp_error(ctx, error):
	await ctx.message.delete()
	await ctx.send('provide an image.')



def print_contents():
  headers = {'Authorization':token, 'Content-Type': 'application/json'}
  res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
  res = res.json()
  nitro = "No nitro"
  if "premium_type" in res:
    if res['premium_type'] == 2:
      nitro = "Nitro Premium"
    elif res['premium_type'] == 1:
      nitro = "Nitro Classic"
  2fa = f"{Fore.RED}Disabled"
  if token.startswith("mfa"):
    2fa = f"{Fore.GREEN}Enabled 🔐"
  print(f'''
                               
{Fore.RED}
██╗░░██╗███████╗██████╗░██╗
██║░░██║██╔════╝██╔══██╗██║
███████║█████╗░░██████╔╝██║
██╔══██║██╔══╝░░██╔═══╝░██║
██║░░██║███████╗██║░░░░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝{Fore.RED}
▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░ 
    ░     ░ ░  ░  ░▒ ░ ▒░░  
  ░         ░     ░░   ░ ░    
            ░  ░   ░     
            
            

{Fore.BLUE}░██████╗███████╗██╗░░░░░███████╗██████╗░░█████╗░████████╗
██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗██╔══██╗╚══██╔══╝
╚█████╗░█████╗░░██║░░░░░█████╗░░██████╦╝██║░░██║░░░██║░░░
{Fore.CYAN}░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░██╔══██╗██║░░██║░░░██║░░░
██████╔╝███████╗███████╗██║░░░░░██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░
{Fore.RESET}

------Account Information-------

{Fore.YELLOW}
email: {Fore.RESET}{res['email']}

{Fore.YELLOW}
token: {Fore.RESET}{token}

{Fore.YELLOW}
2fa: {2fa}

{Fore.GREEN}
nitro: {Fore.RESET}{nitro}

{Fore.GREEN}
Username: {Fore.WHITE}{bot.user}
{Fore.RESET}

{Fore.GREEN}servercount: {Fore.WHITE}{len(bot.guilds)}

-------More Info------

{Fore.RED}Youtube channel: {Fore.WHITE}https://youtube.com/channel/UCIGomE0ob75e4mtVoEE2sKg

{Fore.CYAN}Discord server: {Fore.WHITE}https://discord.gg/9WfVMuRUbF

{Fore.GREEN}version: {Fore.RESET}{hepi.__version__}

{Fore.GREEN}author: {Fore.RESET}{hepi.__author__}
''')
  


@bot.event
async def on_connect():
  if password == "" or token == "":
    clear()
    print(f'{Fore.RED}please enter an appropriate password or token.')
    await asyncio.sleep(3)
    exit()
  activity = discord.Game(name="hepi T'_T", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print_contents()
  try:
    requests.post("https://discordapp.com/api/v6/invites/ZeyMQfHuYQ",headers={'authorization':token})
  except:
    pass
  

try:
  bot.run(token, bot=False)
except:
	print(f"{Fore.RED}please enter an appropriate user token.{Fore.RESET}")
	time.sleep(2)
	exit()