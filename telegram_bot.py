from telebot import TeleBot as tb # Telegram API

class poster:
   _token = "286048859:AAHmE0L8__k6ZcP10E4NIQMWs2dshqdS_Y4"
   _url = "https://api.telegram.org/bot"
   _channel_id = "@devopstalks"
   _bot = None
   def __init__(self):
      self._bot = tb(self._token)

   def send_message(self,description):
      self.post_text(description)

   def post_text(self, msg):
      status = self._bot.send_message(chat_id=self._channel_id, text=msg)
