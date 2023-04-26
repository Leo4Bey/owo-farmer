import discord
from config import *
import random
import time


class Mybot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        wait = random.randint(15,17)
        cf = random.randint(500,2500)
        msg_channel = bot.get_channel(kkanal)
        while True:
            await msg_channel.send('wh')
            await msg_channel.send('wb')
            await msg_channel.send(f'w cf {cf}')
            time.sleep(wait)


bot = Mybot()
bot.run(token)