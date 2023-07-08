from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instr import *

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        introduce = Label(text=txt_instruction)

        name_lbl = Label(text="Введіть своє ім'я", halign='center')
        self.name_input = TextInput(multiline=False)
        age_lbl = Label(text="Введіть свій вік", halign='center')
        self.age_input = TextInput(text='7',multiline=False)


        self.btn = Button(text='Почати', size_hint=(0.3, 0.2), pos_hint={'center': 0.5})
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(name_lbl)
        line1.add_widget(self.name_input)
        line2.add_widget(age_lbl)
        line2.add_widget(self.age_input)

        line3 = BoxLayout(orientation='vertical', padding=15)
        line3.add_widget(introduce)
        line3.add_widget(line1)
        line3.add_widget(line2)
        line3.add_widget(self.btn)

        self.add_widget(line3)

    def next(self):
        pass
        

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass

class ResultScreen(Screen):
    pass

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        sm.add_widget(ResultScreen(name='result'))

app = HeartCheck()
app.run()