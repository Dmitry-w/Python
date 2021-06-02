import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot('1892115404:AAGTlWJtNnoyML9lyzMKH3lxArEueLpmoHs')

@bot.message_handler(commands=['start'])
def welcome_command(message):
          bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.first_name) + "\nВведите /help, чтобы узнать команды бота.")

@bot.message_handler(commands=['help'])
def help_command(message):
	bot.send_message(message.chat.id, '/start - запуск бота\n/help - команды бота\nС помощью этого бота можно узнать погоду в любом городе!\nВведите название города, в котором хотите узнать погоду.')

@bot.message_handler(content_types=['text'])
def test_command(message):
          try:
                 city = message.text

                 config_dict = get_default_config()
                 config_dict['language'] = 'ru'

                 owm = OWM('1b99a3783c0e6a8ac48024ee80aa8473', config_dict)
                 mgr = owm.weather_manager()
                 observation = mgr.weather_at_place(city)
                 w = observation.weather
                # Температура
                 t = w.temperature('celsius')
                 t1 = t['temp']
                 t2 = t['feels_like']
                 t3 = t['temp_max']
                 t4 = t['temp_min']
                # Скорость ветра
                 wi = w.wind()['speed']
                # Влажность
                 hum = w.humidity
                # Облачность
                 cloud = w.clouds
                # Давление
                 press = w.pressure['press']
                # Видимость
                 vd = w.visibility_distance

                 bot.send_message(message.chat.id, "В городе " + str(city) + " температура " + str(t1) + " °С" + "\n" +
                                "Максимальная температура " + str(t3) + " °С" + "\n" +
                                "Минимальная температура " + str(t4) + " °С" + "\n" +
                                "Ощущается как " + str(t2) + " °С" + "\n" +
                                "Скорость ветра " + str(wi) + " м/с" + "\n" +
                                "Влажность " + str(hum) + "%" + "\n" +
                                "Облачность " + str(cloud) + "%" + "\n" +
                                "Видимость " + str(vd) + " м" + "\n" +
                                "Давление " + str(press) + " мм.рт.ст.")

          except:
                    bot.send_message(message.chat.id, "Город не найден")
                    print(str(message.text),"- не найден")

bot.polling(none_stop=True, interval=0)

