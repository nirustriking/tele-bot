x = "niruyg7" # ADAFRUIT_IO_USERNAME
y = "aio_KhaX36hU7tSx28XnF2s2lbiJgSKP" # ADAFRUIT_IO_KEY 
from Adafruit_IO import Client, Feed
aio = Client(x,y)

feed=Feed(name='bot')
result=aio.create_feed(feed)

from Adafruit_IO import Data
value=Data(value=1)
value_send=aio.create_data('bot',value)


from telegram.ext import Updater,CommandHandler
import requests
def grt_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def dog(bot,update):
    url=grt_url()
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo=url)

u = Updater('1305318094:AAFUjgQYIj4PFOlPjqNnWT_TZSUQ6R5BiP4')
dp = u.dispatcher
dp.add_handler(CommandHandler('dog',dog))
u.start_polling()
u.idle()
