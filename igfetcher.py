import telebot
import time


bot_token='1432521465:AAGWES7yjP0bqgKhStoKmWas2ALgTDrJjs8'

  
bot=telebot.TeleBot(token=bot_token)
def find_at(msg):
  for text in msg:
    if '@' in text:
      return text

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message,"Hi There😃 Welcome!🤗.......I can send you the link of Instagram profile by any desired username just start the username after '@'😉")
 
 
@bot.message_handler(commands=['help'])
def send_welcome(message):
  bot.reply_to(message,'Contact my piro owner❤️😂... @DebNationXD for any support that you need...........Thank You 🙏')


@bot.message_handler(func=lambda msg: msg.text is not None and '@'in msg.text)
def at_answer(message):
  texts = message.text.split()
  at_text = find_at(texts)
  
  bot.reply_to(message, 'https://instagram.com/{}'.format(at_text[1:]))

 

while True : 
  send_welcome is not None 
   
  try:
    bot.polling()
  except Expectation:
    time.sleep(15)
   
     
     
    
 
       
     
 
