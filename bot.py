import telebot
import os
from random import choice
from settings import TG_API_TOKEN

#from settings import TG_API_TOKEN
from bot_logic import gen_pass

#bot = telebot.TeleBot(TG_API_TOKEN)
bot = telebot.TeleBot(TG_API_TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
#    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! Команды : /bye ends the bot, /tips")
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! Команды : /bye ends the bot, /tips, /mem sends a meme')

@bot.message_handler(commands=['bye'])
def send_goodbye(message):
    bot.reply_to(message, "Пока! До скорой встречи!")

@bot.message_handler(commands=['tips'])
def send_help(message):
    bot.reply_to(message, "С какой игрой тебе помочь? Steal a brainrot, Grow a garden, Plants vs brainrots, 99 nights in the forest, Doors. Пожалуйста напищи игру также как здесь указано.")

@bot.message_handler(func=lambda message: 'Steal a brainrot' in message.text)
def handle_sab_text(message):
    bot.reply_to(message, 'Супер, здесь вещи, которые тебе могут помочь! 1. Купи приватный сервер, у тебя ничего не будут красть и всех брейнротов будешь покупать только ты, и никто с тобой за брейнротов не будет бороться. 2.Создай второй аккаунт, когда ты будешь делать перерождение ты сможешь взять вещи через второй аккаунт чтобы их не потерять, и также если у тебя будут все вещи на втором аккаунте то ты сможешь пробовать красть на публичных серверах. 3.Играй в субботу на обновлениях, Семми раздает там очень много секретных брейнротов, и включает очень много ивентов.')

@bot.message_handler(func=lambda message: 'Grow a garden' in message.text)
def handle_gag_text(message):
    bot.reply_to(message, 'Супер, здесь вещи, которые тебе могут помочь! 1.Создай приватный сервер, это безплатно и донатеры у тебя не будут красть за робаксы. 2. Контролируй магазин семян, он меняется каждых 5 минут. 3.Играй в субботу на обновлениях, Джандел раздает много петов и растений и также включает ивенты.')

@bot.message_handler(func=lambda message: 'Plants vs brainrots' in message.text)
def handle_pvb_text(message):
    bot.reply_to(message, 'Супер, здесь вещи, которые тебе могут помочь! 1.Контролируй магазин с растениями, он меняется каждых 5 минут. 2.Выполняй ивент квесты, это тебе даст много денег, растений и брейнротов. 3.Играй в субботу на обновлениях, Армин раздает много растений и брейнротов.')

@bot.message_handler(func=lambda message: '99 nights in the forest' in message.text)
def handle_99nitf_text(message):
    bot.reply_to(message, 'Супер, здесь вещи, которые тебе могут помочь! 1.Играй в команде, так веселее и вы друг другу можете роли разделить. 2.Копи алмазы, ты можешь их копить исканием их на карте, побежданием замка культистов, игранием в субботу на обновления там раздают безплатно 20 алмазов и через ежедневные задания. 3.Покупай за алмазы класы, класы тебе помогут в игре.')

@bot.message_handler(func=lambda message: 'Doors' in message.text)
def handle_doors_text(message):
    bot.reply_to(message, 'Супер, здесь вещи, которые тебе могут помочь 1.Собирай монеты,когда пойдешь в следущий раунд ты сможешь себе купить вещи как фонарь итд. ')

@bot.message_handler(commands=['mem'])
def send_mem(message):
    random_mem = choice(os.listdir('images')) #'mem2.jpeg'
    with open(f'images/{random_mem }', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    #bot.send_message(message.chat_id, f'Привет , {message.from_user.first_name}!\nЯ бот который отпровляет мемы')
    
#@bot.message_handler(func=lambda message: 'Dead rails' in message.text)
#def handle_dr_text(message):
    #bot.reply_to(message, 'Супер, здесь вещи, которые тебе могут помочь!')

#@bot.message_handler(func=lambda message: 'Dump' in message.text)
#def handle_dump_text(message):
    #bot.reply_to(message, 'Супер, здесь вещи, которые тебе могут помочь!')


#content_types=['audio', 'photo', 'voice', 'video', 'document',
    # 'text', 'location', 'contact', 'sticker']

#@bot.message_handler(content_types=['sticker'])
#def handle_sticker(message):
    #bot.reply_to(message, 'Крутой стикер!')

#@bot.message_handler(func=lambda message: 'банан' in message.text)
#def handle_banana_text(message):
    #bot.reply_to(message, 'Бананы это круто!')

gen_pass(10)

bot.polling()