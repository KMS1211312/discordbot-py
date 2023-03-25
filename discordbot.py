from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['MTA4OTIwNzM4OTIyOTY5OTE3NQ.GovbsL.Zy-mK4CX0k8C8cLFC_r_8LMOD56DvyqOCQQYrk']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')


try:
    client.run(MTA4OTIwNzM4OTIyOTY5OTE3NQ.GovbsL.Zy-mK4CX0k8C8cLFC_r_8LMOD56DvyqOCQQYrk)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
