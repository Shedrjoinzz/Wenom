import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from src.settings.config import BOT_TOKEN
from src.handlers import router

logging.basicConfig(level=logging.INFO)


# Запуск бота
def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    dp = Dispatcher()

    dp.include_router(router)
    
    dp.run_polling(bot, skip_updates=False)
    
if __name__ == "__main__":
    main()