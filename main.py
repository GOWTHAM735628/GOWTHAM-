from pyrogram import Cilent, filters
from pyrogram. types import inilnekeyboardMarkup.InilnKeyboardButton

API_ID = "24619371"
API_HASH = "4418d775c222fa4f61c4c50e56bb5fef"
BOT_TOKEN = "7600157728:AAFoVEVXlOs4IPxj104i_Aj-OHoNM2el_EE"

Tamilnetworkcom = Cilent(
      name="codebot
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN,
) 

START_BUTTONS = [[
  InilnKeyboardButton("JOIN NOW ", url="https://t.me/tamilnetworkcom")
]]

@tamilnetworkcom.on_message(filters.command("start"))
async def start_com(cilent, message):
  await message.reply_text(
  text= "You have to join channel to used me",
reply_markup=InilnKeyboardButton(START_BUTTONS)
  )    

        
print("Bot was Started")

Tamilnetworkcom.run()                           
