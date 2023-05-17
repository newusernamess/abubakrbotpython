import logging
import requests

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.filters import Text
from function import nimadur

API_TOKEN = "6050885032:AAHvIKfE3p6jvlwHKIGMqnb45ur1Dc0--ZU"
# Configure logging

logging.basicConfig(level=logging.INFO)

# async def instagramDownlaoder(instaUrl):
#     url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

#     querystring = {"url":f"{instaUrl.message.text}"}
#     headers = {
#         "X-RapidAPI-Key": "901af23752msh7c051f4139a8db7p13ac8djsn2345135172bb",
#         "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
#     }

#     response = await requests.get(url, headers=headers, params=querystring)
#     print(response.json())

# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

admins_id = [5466255061, 6299965585]


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        try:
            if update.message.photo:
                    print("Rasm ekan !")
                    for admin in admins_id:
                        await bot.send_photo(admin, caption=f"Sizga screenShot yubordi !\nTo'liq malumot 👇\nIsm: {update.message.from_user.first_name or 'Yoq'}\nFamiliya: {update.message.from_user.last_name}\nUsername: @{update.message.from_user.username or 'Yoq'}\nTelegram_id: {update.message.from_user.id}", photo=update.message.photo[1].file_id)
        except:
            pass
        try:
            if not update.message.entities[0].type == "url":
                await update.message.answer("Siz obuna bo'lmadingiz  <a href='https://www.instagram.com/abdukar1mov_08/'>obuna bo'ling</a>", parse_mode="HTML")
                raise CancelHandler()
        except:
            pass
        try:
            if not update.message.text == "/start" and not update.message.entities[0].type == "url":
                await update.message.answer("Siz obuna bo'lmadingiz  <a href='https://www.instagram.com/abdukar1mov_08/'>obuna bo'ling</a>", parse_mode="HTML")
                raise CancelHandler()
        except:
            pass
    
    
dp.middleware.setup(BigBrother())

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.answer(
        f"Assalomu alekom {message.from_user.first_name}\nBot instagramdan video yuklaydi foydalanish uchun\nAdminning instagram sahifasiga obuna bo'lib botga\nScreenShot yuborishingiz kerak, <a href='https://www.instagram.com/abdukar1mov_08/'>obuna bo'ling !</a>",
        parse_mode="HTML",
    )

@dp.message_handler(Text(startswith="https://www"))
async def echo_down(message: types.Message):
    await message.answer(text="Biroz kuting !")
    try:
        video = nimadur(message=message)
        await message.answer_video(video=video["media"], caption="@instasavedurlbot - <b>Shu botdan yuklab olindi !</b>", parse_mode="HTML")
    except:
        await message.answer(text="Bu videoni yuklab bo'lmadi")
    print(video)


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
