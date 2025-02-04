import os 

from os import environ
from aiohttp import web
from plugins.koyeb import web_server

from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, FORCE_SUB

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.mention = me.mention
       self.username = me.username 
       self.force_channel = FORCE_SUB
       if FORCE_SUB:
         try:
            link = await self.export_chat_invite_link(FORCE_SUB)                  
            self.invitelink = link
         except Exception as e:
            print(f"{e}")
            print("Make Sure Bot admin in force sub channel")             
            self.force_channel = None
       print(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")
       app = web.AppRunner(await web_server())
       await app.setup()
       bind_address = "0.0.0.0"
       await web.TCPSite(app, bind_address, 8080).start()


    async def stop(self, *args):
      await super().stop()      
      print("Bot Stopped")
        
bot = Bot()
bot.run()
