from aiogram import Bot, Dispatcher, executor, types
import config 
import time
import random

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'go'])
async def start(message : types.Message):
    with open('users.txt', 'r', encoding='utf-8') as read_user:
        res = read_user.readlines()
        users = []
        if res != []:
            for i in res:
                username = i.split()[0]
                if username not in users:
                    users.append(username)
                    if username in users:
                        with open('users.txt', 'a+', encoding='utf-8') as user:
                            user.write(f'{message.from_user.username} {message.from_user.id} {time.ctime()}\n')
        else:
            with open('users.txt', 'a+', encoding='utf-8') as users:
                users.write(f"{message.from_user.username} {message.from_user.id} {time.ctime()}\n")
    await message.answer(f"Здраствуйте, {message.from_user.full_name} {message.from_user.id}")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Помощь")

@dp.message_handler(text = "Привет")
async def hello(message: types.Message):
    await message.answer("Привет")

@dp.message_handler()
async def not_found(message: types.Message):
    await message.reply("Я вас не понял введите /help")

@dp.message_handler(commands=['game'])
async def not_found (game: types.Message):
    await game.answer('я загадал число между 1 и 3 ')
    random = random.randint(1,3)



executor.start_polling(dp)






# import random
# number = random.randint(1,3)
# choices = 0
# while choices < 1 :
#     print('Угадай число между 1 и 3')
#     guess =  input ()
#     guess = int(guess)
# if guess == number:
#     break
# if guess == number:
#     print('Молодец ты угадал число')
# else:
#     print('К сожелению ты не угадал число.Я')