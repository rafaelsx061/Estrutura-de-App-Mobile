from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home import HomeScreen
from screens.tela1 import Tela1Screen
from screens.tela2 import Tela2Screen
from screens.tela3 import Tela3Screen
from screens.tela4 import Tela4Screen
from screens.tela5 import Tela5Screen


class GerenciadorTelas(ScreenManager):
    pass


class MeuApp(App):
    def build(self):
        sm = GerenciadorTelas()

        # Adicionando todas as telas ao gerenciador
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(Tela1Screen(name="tela1"))
        sm.add_widget(Tela2Screen(name="tela2"))
        sm.add_widget(Tela3Screen(name="tela3"))
        sm.add_widget(Tela4Screen(name="tela4"))
        sm.add_widget(Tela5Screen(name="tela5"))

        return sm


if __name__ == "__main__":
    MeuApp().run()
