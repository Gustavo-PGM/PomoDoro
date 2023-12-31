from itertools import cycle
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.clock import Clock

class Ciclo:
    def __init__(self):
        self.cycle = cycle([tempor(25), tempor(5), tempor(25), tempor(5), tempor(30)])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.cycle)

class tempor:
    def __init__(self, tempo):
        self.tempo = tempo * 60

    def diminuir(self):
        self.tempo -= 1
        return self.tempo

    def __str__(self):
        return '{:02d}:{:02d}'.format(*divmod(self.tempo, 60))

class Pomodoro(MDFloatLayout):
    tempo = StringProperty('25:00')
    botao = StringProperty('Começar')
    rodando = BooleanProperty(False)
    cycle = Ciclo()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ttempo = next(self.cycle)
        self.tempo = str(self.ttempo)

    def start(self):
        self.botao = 'Acabar'
        if not self.rodando:
            self.rodando = True
            Clock.schedule_interval(self.update, 1)

    def stop(self):
        self.botao = 'Recomeçar'
        if self.rodando:
            self.rodando = False

    def clique(self):
        if self.rodando:
            self.stop()
        else:
            self.start()

    def update(self, *args):
        tempo = self.ttempo.diminuir()
        if tempo == 0:
            self.stop()
            self.ttempo = next(self.cycle)

        self.tempo = str(self.ttempo)

class PomoGus(MDApp):
    def change_color(self):
        theme = self.theme_cls.theme_style
        if theme == 'Dark':
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'

    def build(self):
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.primary_hue = '400'
        return Builder.load_file('doro.kv')
    

PomoGus().run()