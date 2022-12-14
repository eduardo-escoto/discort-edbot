# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        await message.channel.send('Fuck you bro')

client.run('MTA1MjQ5ODM3MTg5MTQ0MTcwNA.GAhKW9.igb2jAzSxYpkYl268WLB5JpIniltJBJgM4iFqo')
