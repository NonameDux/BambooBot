import asyncio
import logging
import sys
from os import getenv
from datetime import datetime
import random
import html

from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message,InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery
from aiogram.types import FSInputFile


from database import initilize_db,upsert_info,check_info,get_all_usernames,get_db_screen,get_all_info 
from settings import GetTypeBamboo 
# Bot token can be obtained via https://t.me/BotFather
TOKEN = "" #Your bot token

bot_start_timestamp = int(datetime.now().timestamp())

photo_file = FSInputFile("wake_up.jpg")

Is_Tracing = True
Logs = []

totalmessages = 0
button = InlineKeyboardButton(text="Grab +1 cm!🎋", callback_data="grab_bonus")
keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])

sync_finished = asyncio.Event()
router = Router()
dp = Dispatcher()
initilize_db()
dp.include_router(router)

#GETTING DATA FROM LAST ENABLING
async def wait_for_sync_end(bot):
    old_users_id,old_usernames,old_user_amount,old_timestamp = get_db_screen()
    await sync_finished.wait() 

    CHAT_ID = 0 #Your chat ID
   

    users_id,usernames,user_amount,timestamp = get_db_screen()

    print("History update finished! Sending report to chat...")
    user_logs = {}

    for log in Logs:
        username = log[0]
        action = log[1]
        action_time = log[2]
        
        if username not in user_logs:
            user_logs[username] = []
        
        user_logs[username].append([action, action_time])

    report_blocks = []

    for username, logs_list in user_logs.items():
        clean_username = username.replace("@", "").lower()
        
        old_usernames_clean = [name.replace("@", "").lower() for name in old_usernames]
        usernames_clean = [name.replace("@", "").lower() for name in usernames]
        
        try:
            old_idx = old_usernames_clean.index(clean_username)
            old_amt = old_user_amount[old_idx]
        except ValueError:
            old_amt = 0
            
        try:
            new_idx = usernames_clean.index(clean_username)
            new_amt = user_amount[new_idx]
        except ValueError:
            new_amt = old_amt

        user_block = (
            f"@{username.replace('@', '')} ({int(old_amt)} -> {int(new_amt)}):\n"
            f"<blockquote>"
            f"{'\n'.join([f'{item[0]} ({item[1]})' for item in logs_list])}"
            f"</blockquote>"
        )
        report_blocks.append(user_block)

    report_text = (
        f"📊 <b>History update finished!</b>\n"
        f"While the bot was sleeping, you did...\n\n"
        f"{'\n\n'.join(report_blocks)}"
    )

    await bot.send_photo(
        chat_id=CHAT_ID,
        photo=photo_file,
        caption=report_text,
        parse_mode="HTML"  
    )
    



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {message.from_user.full_name}!")

@dp.message(Command("bamboo", ignore_mention=True)) 
async def command_bamboo_handler(message: Message) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    global Is_Tracing
    print(user_id, username)
    if username:
        username_text = f"@{username}"
    else:
        username_text = "none"

    result = check_info(user_id)
    timestamp = int(message.date.timestamp())
    if result:
        amount, last_timestamp = result
        delay = timestamp - last_timestamp
    else:
        amount, last_timestamp = 0, timestamp
        delay = 4000
    
    if Is_Tracing:
        if timestamp > bot_start_timestamp:
            Is_Tracing = False
            sync_finished.set()

    num = random.choices([0.1,0.5, 1.0, 1.5,5], weights=[2,62, 25, 10,1])[0]
    print(f"[INFO] ID:{user_id}, USERNAME:{username_text}, BAMBOO_SIZE:{amount}, LAST:{last_timestamp}, NOW:{timestamp}, DELAY:{delay}")

    new_amount = amount + num

    TypeB, AchivementMessage = GetTypeBamboo(amount,new_amount)

    if Is_Tracing:
        if delay < 3600:
            Logs.append((username,f"You need to wait <b>{int((3600-delay)/60)}</b> more minutes!",message.date.strftime("%H:%M")))
        elif delay >= 3600:
            upsert_info(user_id,username,new_amount,timestamp)
            Logs.append((username,f"Your bamboo grew, +{num} cm!",message.date.strftime("%H:%M")))
            if num == 5:
                Logs.append((username,f"🔥👑 CRITICAL LUCK, BOW TO THE KING! {username_text} 👑🔥",message.date.strftime("%H:%M")))
            if AchivementMessage:
                    await message.answer(AchivementMessage)
        else: 
            await message.answer(f"An error happened!")

    else:
        if delay < 3600:
            await message.answer(f"""{username_text}, You need to wait <b>{int((3600-delay)/60)}</b> more minutes!
Your bamboo height now: <b>{amount}</b> cm.
Type: <b>{TypeB}</b>""")
        elif delay >= 3600:
            if num == 5:
                await message.answer(f"🔥👑 CRITICAL LUCK, BOW TO THE KING! {username_text} 👑🔥")
            upsert_info(user_id,username_text,new_amount,timestamp)
            await message.answer(f"""{username_text}, Your bamboo grew, +{num} cm!
Your bamboo height now: <b>{amount}</b> cm.
Type: {TypeB}""")
            if AchivementMessage:
                await message.answer(AchivementMessage)
        else: 
            await message.answer(f"An error happened!")

@dp.message(Command("top"))
async def command_top_handler(message: Message) -> None:
    raw_info = get_all_info() 
    
    #SORTING
    sorted_info = tuple(sorted(raw_info, key=lambda x: x[2], reverse=True))

    report_blocks = []
    i = 0
    for row in sorted_info:
        i+=1
        if i==1:user_block = (f"{i}. 👑 @{row[1].replace('@', '')} — <b>{int(row[2])} cm.</b> 👑\n")
        elif i==2:user_block = (f"{i}. 🔥 @{row[1].replace('@', '')} — <b>{int(row[2])} cm.</b> 🔥\n")
        elif i<=10:user_block = (f"{i}. @{row[1].replace('@', '')} — <b>{int(row[2])} cm.</b>\n")

        report_blocks.append(user_block)

    report_text = (
        f"👑 <b>Owners of the tallest bamboo</b> 👑\n\n"
        f"{''.join(report_blocks)}"
    )
    await message.answer(report_text)



@dp.message()
async def echo_handler(message: Message) -> None:
    global totalmessages
    totalmessages+=1
    if totalmessages >= 50:
        totalmessages = 0
        await message.answer(
            text="Click to grab a bonus!", 
            reply_markup=keyboard
        )

@router.callback_query(F.data == "grab_bonus")
async def process_grab_bonus(callback: CallbackQuery):

    user_id = callback.from_user.id
    username = callback.from_user.username
    print(user_id, username)
    if username:
        username_text = f"@{username}"
    else:
        username_text = "none"

    result = check_info(user_id)
    timestamp = int(datetime.now().timestamp())
    if result:
        amount, last_timestamp = result
    else:
        amount, last_timestamp = 0, timestamp
    
    new_amount = amount + 1

    upsert_info(user_id,username_text,new_amount,last_timestamp)

    TypeB, AchivementMessage = GetTypeBamboo(amount,new_amount)

    await callback.message.edit_text(
        text=f"""🎁 Bonus claimed by {username_text}!
Their bamboo height now: <b>{new_amount}</b> cm
Type: <b>{TypeB}</b>
{AchivementMessage}""",
        reply_markup=None 
    )

    await callback.answer(text="You were fast! +1 cm added.", show_alert=False)


@dp.message(Command("top", ignore_mention=True))
async def command_bamboo_handler(message: Message) -> None:
    usernames = get_all_usernames()

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    asyncio.create_task(wait_for_sync_end(bot))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())