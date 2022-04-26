import config
import discord

#Take api token and permission link from config file
TOKEN = config.TOKEN
PERMISSIONLINK = config.permissionLink

client = discord.Client()

@client.event 
async def on_ready():
    print('Logged in as {0.user}'.format(client))

client.run(TOKEN)

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} on {channel}')
    
