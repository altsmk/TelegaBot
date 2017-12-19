import telebot# Подключаем библиотеку для работы с телеграмом
#Подключаем библиотеки
import requests
from bs4 import BeautifulSoup
#Токен телеграм бота, который мы получили от Godfatherbot
token = "475943736:AAFne2LFTJvSANCPVgCSs9rcivfIOFsTKTk"
#Активация бота
bot = telebot.TeleBot(token)
 
#Обработчик команды /btc
@bot.message_handler(commands=['btc'])
def handle_command(mesage):
    #Отсюда парсим информацию
    r = requests.get("https://coinmarketcap.com/currencies/bitcoin/#markets")
    #Обрезаем строки, чтобы получить исключительно число.
    data = r.text
    SiteInfo = BeautifulSoup(data)
    SiteInfo = SiteInfo.find_all("span",id="quote_price")
    TempText = str(SiteInfo)
    TempText = TempText[:TempText.find('id')]
    TempText = TempText[TempText.find('"'):TempText.find(".")]
    TempText = TempText[TempText.find('='):]
    TempText = TempText[TempText.find('"')+1:]
    #Отправляем пользователю ответ
    bot.send_message(mesage.chat.id, TempText)
#Делаем так, чтоб мы постоянно обрабатывали информацию, делаем без цикла ибо Telegram API позволяет это сделать вот такой строкой.
bot.polling(none_stop=True,interval=0,)
