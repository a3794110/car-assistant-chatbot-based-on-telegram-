import sys
from io import BytesIO
from nltk.chat.eliza import eliza_chatbot
import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '374976246:AAFRcnKaSnW2cBI6q7UUe1yeZyj3gCjdAwE'
WEBHOOK_URL = 'https://1b137c23.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
	'state3',
	'state4',
	'state5',
	'state6',
	'state7'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'reset_the_car'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'motion_control'
        },
	{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'functional_analysis'
        },
	{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': 'move_forward'
        },
	{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': 'turn_left'
        },
	{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': 'turn_right'
        },
	{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': 'move_backward'
        },
	{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state5',
            'conditions': 'stop_to_back'
        },
	{
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state7',
            'conditions': 'stop_back'
        },
	{
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state2',
            'conditions': 'motion_again'
        },

	{
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': 'turn_right'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state6',
            'conditions': 'all_of_it'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state7',
                'state5',
		'state1',
		'state6'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)
x='1'

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
    if machine.advance(update):
	machine.advance(update)
    else :
	text = update.message.text
    	update.message.reply_text(eliza_chatbot.respond(text))
    x=update.message.text
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')

@app.route('/motion',methods=['GET'])
def motion():
    return x

if __name__ == "__main__":
    _set_webhook()
    app.run()
