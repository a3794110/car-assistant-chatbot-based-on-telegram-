# car-assistant-chatbot-based-on-telegram-
car assistant chatbot
###ability
* command the vehicles based on finite state machine
* simple Natural Language processing
 
## Setup
### Prerequisite
* Python 2.7
#### Install Dependency
```sh
pip install -r requirements.txt
```
### Secret Data
`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.
### Run Locally
You can either setup https server or using `ngrok` as a proxy.
**`ngrok` would be used in the following instruction**
```sh
ngrok http 5000
```
After that, `ngrok` would generate a https URL.
You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.
#### Run the sever
```sh
python app.py
```
## Finite State Machine
![fsm](./show-fsm.png)
## Usage
The initial state is set to `user`.
a month ago @Lee-W Fix README typo 	
Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.
a month ago @Lee-W Update README for basic FSM design 	
* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"
	* Input: "go to state2"
		* Reply: "I'm entering state2"
## Author
[a3794110](https://github.com/a3794110)
