from aiogram import executor

from init_bot import dp


if __name__ == '__main__':
    print('Start')
    executor.start_polling(dp, skip_updates=True)
    print('End')