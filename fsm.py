
from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def all_of_it(self, update):
        text = update.message.text
        return text.lower() == 'all of it'

    def motion_again(self, update):
        text = update.message.text
        return text.lower() == 'again'

    def reset_the_car(self, update):
        text = update.message.text
        return text.lower() == 'reset the car'

    def motion_control(self, update):
        text = update.message.text
        return text.lower() == 'motion control'

    def functional_analysis(self, update):
        text = update.message.text
        return text.lower() == 'functional analysis'

    def move_forward(self, update):
        text = update.message.text
        return text.lower() == 'move forward'
   
    def turn_left(self, update):
        text = update.message.text
        return text.lower() == 'turn left'
    
    def turn_right(self, update):
        text = update.message.text
        return text.lower() == 'turn right'

    def move_backward(self, update):
        text = update.message.text
        return text.lower() == 'move backward'

    def stop_to_back(self, update):
        text = update.message.text
        return text.lower() == 'stop'

    def stop_back(self, update):
        text = update.message.text
        return text.lower() == 'stop'

    def on_enter_state1(self, update):     
        update.message.reply_text("Reset is complete...")
	self.go_back(update)

    def on_enter_state2(self, update):
        update.message.reply_text("What to do next?")
  
    def on_enter_state3(self, update):
        update.message.reply_text("Which parts?")      

    def on_enter_state6(self, update):
        update.message.reply_text("Car is functional")
        self.go_back(update)
   
    def on_enter_state4(self, update):
        update.message.reply_text("Then?")
    
    def on_enter_state5(self, update):
        update.message.reply_text("Back to home")
        self.go_back(update)

    def on_enter_state7(self, update):
        update.message.reply_text("Back to home")
        self.go_back(update)









