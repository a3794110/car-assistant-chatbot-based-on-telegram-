import sys
from io import BytesIO
from nltk.chat.eliza import eliza_chatbot
import telegram
import os
from flask import Flask, request, send_file
 


API_TOKEN = '374976246:AAFRcnKaSnW2cBI6q7UUe1yeZyj3gCjdAwE'
WEBHOOK_URL = 'https://6aa21fc0.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
x=' '
current_dir_path = os.path.dirname(os.path.realpath(__file__))
print(current_dir_path)

def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    global x
    if update.message.text:
        text = update.message.text
        update.message.reply_text(eliza_chatbot.respond(text))
    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        newFile=bot.get_file(file_id)  
        newFile.download('cropped_panda.jpg')
        os.system('1.bat')
        f = open('test.txt', 'r', encoding='UTF-8')
        for line in f.readlines():
            x=x+line
        update.message.reply_text(x)
        x=' '
        f.close()
    if update.message.voice:
        file_id = update.message.voice.file_id
        newFile=bot.get_file(file_id)  
        newFile.download('voice.ogg')
    #x=update.message.text
    return 'ok'


@app.route('/motion',methods=['GET'])
def motion():
    return x

if __name__ == "__main__":
    _set_webhook()
    app.run()