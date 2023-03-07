from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup

Builder.load_file('menu/menu.kv')


class ExitPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MenuWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start_game(self):
        MDApp.get_running_app().root.ids.scrn_game.choose()

        self.parent.transition.direction = 'left'
        self.parent.current='scrn_game'

    def leaderboard(self):
        self.parent.transition.direction = 'left'
        self.parent.current='scrn_leaderboard'

    def exit(self):
        popup = ExitPopup()
        popup.open()

class MenuApp(MDApp):
    def build(self):
        return MenuWindow()

if __name__=="__main__":
    MenuApp().run()