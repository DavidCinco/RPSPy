import kivy, kivymd
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy import Config

#Screen PY files
from menu.menu import MenuWindow
from game.game import GameWindow
from leaderboard.leaderboard import LeaderboardWindow
from sqlqueries import SqlQueries

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()

class MainWindow(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #con = SqlQueries.create_connection('database/rpsdb.db')
        #query = "CREATE TABLE "
        #SqlQueries.create_table(con, )
        
class MainApp(MDApp):
    def build(self):
        return MainWindow()

if __name__=="__main__":
    MainApp().run()