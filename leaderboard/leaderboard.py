from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('leaderboard/leaderboard.kv')

class LeaderboardWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class LeaderboardApp(MDApp):
    def build(self):
        return LeaderboardWindow()

if __name__=="__main__":
    LeaderboardApp().run()