# Car-Assistant-Chatbot-Based-On-Telegram-
Car assistant chatbot
### ability
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
This chatbot has the ability of natural language processing . Therefore,if the input text does not in the transition of finite state machine,it will respond you with 'perfunctory' words by package 'nltk'.

On the other hand, if the input text exist in the transition of finite state machine,it will act as follows.
The initial state is set to `user`. 
* user
	* Input: "reset the car"
		* reset complete"
	* Input: "functional analysis"
		* Which parts?"
			* state3
				* Input: "all of it"
					* car is functional"
	* Input: "motion control"
		* what to do next?"
			* state2
				* Input "move forward" or "turn left" or "turn right" or "move backward"
					* then?"
						* state4
							* Input:"again"
								* what to do next?"
									* back to state2
							* Input:"stop"
								* back to home"
									* back to user
				* Input "stop"
					* back to home"
						* back to user
## Author
[a3794110](https://github.com/a3794110)
