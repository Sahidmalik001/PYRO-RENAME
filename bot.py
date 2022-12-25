import os 

from os import getenv, environ

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
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
       
    async def stop(self, *args):
      await super().stop()      
      print("Bot Stopped")
        
bot = Bot()
bot.run()
