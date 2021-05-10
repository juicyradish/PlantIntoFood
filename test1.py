import discord

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("hello"):
        await message.channel.send("hello, " + str(message.author) + "!")
    
    if message.content.startswith('$guess'):
        await message.channel.send('Guess a number between 1 and 10.')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = random.randint(1, 10)

        try:
            guess = await self.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send('Oops. It is actually {}.'.format(answer))


client.run('ODQwNDE3NzM2NTQ2ODQ0Njky.YJX6Ag.dH98CfOZJMCX6YtLcqsVo_s9uDc')