from pydoc import resolve
import config
import discord

#get api token and permission link from config file 
TOKEN = config.TOKEN
PERMISSIONLINK = config.permissionLink
        
client = discord.Client()
        
@client.event 
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} on ({channel})')

    if message.author == client.user:
        return
    
    if user_message.lower() == '1488':
        response = 'фошист!'
        await message.channel.send(response)
    
    if user_message.lower() == 'ты пидор' or 'ты пидор!':
        response = 'А может ты пидор?!'
        await message.channel.send(response)

client.run(TOKEN)
