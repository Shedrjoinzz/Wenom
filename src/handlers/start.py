from aiogram import types
from aiogram.filters import CommandStart
from aiogram import Router

router = Router(name=__name__)

@router.message(CommandStart())
async def start_bot(message: types.Message):
    user_start = message.text.split(' ')
    print(user_start)
    
    if len(user_start) > 1:
        try:
            id_user = int(user_start[1])
            return print('ok')
        except:
            return print('False')
 
    await message.answer('Привет')
