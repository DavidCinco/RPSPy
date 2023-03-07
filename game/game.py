from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.clock import Clock
import random

Builder.load_file('game/game.kv')

class ChoosePopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def choice_value(self, value):
        MDApp.get_running_app().root.ids.scrn_game.user_choice = value
        MDApp.get_running_app().root.ids.scrn_game.cpu_choice = random.choice(MDApp.get_running_app().root.ids.scrn_game.cpu_choices_list)
        MDApp.get_running_app().root.ids.scrn_game.display_choices()
        self.dismiss()

class GameOverPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def close(self):
        MDApp.get_running_app().root.ids.scrn_game.return_to_menu()
        self.dismiss()

class GameWindow(Screen):

    game_round = 1 #default round
    user_lifes = 3 #default lifes (3 hearts) 
    user_score = 0 #default score
    user_choice = "" #default - no choice yet
    
    cpu_choices_list = ['rock', 'paper', 'scissors'] 
    cpu_choice = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def choose(self, *args):
        self.ids.player_choice_image.source = "icons/faq.png"
        self.ids.cpu_choice_image.source = "icons/faq.png"
        
        popup = ChoosePopup()
        popup.open()

    def display_choices(self):

        both_values = [self.user_choice, self.cpu_choice]
        counter = 0

        for value in both_values:
            if counter == 0:
                if value == "rock":
                    self.ids.player_choice_image.source = "icons/stone.png"
                elif value == "paper":
                    self.ids.player_choice_image.source = "icons/paper.png"
                else:
                    self.ids.player_choice_image.source = "icons/scissors.png"
                counter = counter + 1
            
            else:
                if value == "rock":
                    self.ids.cpu_choice_image.source = "icons/stone.png"
                    
                elif value== "paper":
                    self.ids.cpu_choice_image.source = "icons/paper.png"
                    
                else:
                    self.ids.cpu_choice_image.source = "icons/scissors.png"

        self.compare_results()
                    
    def compare_results(self):
        
        if self.user_choice == "rock" and self.cpu_choice == "scissors":
            self.user_score = self.user_score + 50
        elif self.user_choice == "paper" and self.cpu_choice == "rock":
            self.user_score = self.user_score + 50
        elif self.user_choice == "scissors" and self.cpu_choice == "paper":
            self.user_score = self.user_score + 50
            
        elif self.cpu_choice == "rock" and self.user_choice == "scissors":
            self.user_lifes = self.user_lifes - 1
        elif self.cpu_choice == "paper" and self.user_choice == "rock":
            self.user_lifes = self.user_lifes - 1
        elif self.cpu_choice == "scissors" and self.user_choice == "paper":
            self.user_lifes = self.user_lifes - 1

        elif self.cpu_choice == self.user_choice:
            pass

        if self.user_lifes <= 0:
            self.ids.lifes_label.text = f"Lifes: {str(self.user_lifes)}"
            popup = GameOverPopup()
            popup.open()
        else:
            self.game_round = self.game_round + 1
            self.ids.round_label.text = f"Round #{str(self.game_round)}"
            self.ids.lifes_label.text = f"Lifes: {str(self.user_lifes)}"
            self.ids.score_label.text = f"Score: {str(self.user_score)}"
            Clock.schedule_once(self.choose, 2)

    def reset_status(self):
        self.game_round = 1
        self.user_lifes = 3
        self.user_score = 0
        self.ids.round_label.text = f"Round #{str(self.game_round)}"

    def return_to_menu(self):
        self.reset_status()
        self.parent.transition.direction = 'right'
        self.parent.current='scrn_menu'

class GameApp(MDApp):
    def build(self):
        return GameWindow()

if __name__=="__main__":
    GameApp().run()