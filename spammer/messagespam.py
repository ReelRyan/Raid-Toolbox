import discord
import asyncio
import time
import sys
import os
import random
import aiohttp

useproxies = sys.argv[7]
if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()

token = sys.argv[1]
SERVER = sys.argv[2]
tokenno = sys.argv[3]
msgtxt = sys.argv[4]
textchan = sys.argv[5]
allchan = sys.argv[6]

@client.event
async def on_ready():
    txtchan = client.get_channel(textchan)
    if allchan == 'true':
        while not client.is_closed:
           for c in client.get_server(SERVER).channels:
                if c.type != discord.ChannelType.text:
                   continue
                myperms = c.permissions_for(client.get_server(SERVER).get_member(client.user.id))
                if not myperms.send_messages:
                    continue
                try:
                    await client.send_message(c, msgtxt)
                except:
                    return ''
    else:
        while not client.is_closed:
            await client.send_message(txtchan, msgtxt)

try:
    client.run(token, bot=False)
except Exception as c:
    print (c)


