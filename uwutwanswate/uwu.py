import discord
token = open('token.txt', 'r').read()
client = discord.Client()
@client.event
async def on_connect():
    print('{} has been connected'.format(client.user))
@client.event
async def on_ready():
    print('{} is now ready to use!'.format(client.user))
@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        if not message.mention_everyone:
            if not message.author.bot:
                text = message.content.replace('<@654106402058534953> ', f'<@{message.author.id}> ').replace('l', 'w').replace('r', 'w').replace('L', 'W').replace('R', 'W').replace('you ', 'uwu ')
                text = text + ' uwu'
                await message.channel.send(text)
client.run(token)