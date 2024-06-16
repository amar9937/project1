from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.metrics import dp

import cal
import random
import datetime

#Window.size = (300,600)

class Data_Content(BoxLayout):
    pass

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initial_value = 0
        self.profit_margin = 0
        self.end_margin = 0
        self.turn_over = 0
        self.assign()
        self.ids.banner1.text = '* * '*100 + 'Normal Mode' + ' * *'*100
        self.ids.banner2.text = '* * '*100 + 'Round Mode' + ' * *'*100
        self.ids.banner3.text = '* * '*100 + 'Slow Mode' + ' * *'*100
        self.ids.banner4.text = '* * '*100 + 'Fast Mode' + ' * *'*100
        content = Data_Content()
        self.data_popup = Popup(title='hack',
                                content=content,
                                auto_dismiss=True,
                                size_hint=(.8,.5),
                                height=content.height)
        self.data_popup.title_font = 'hack-italic'
        self.data_popup.title_size = '17sp'
        
    def abort(self,widget):
        for i in range(1,5):
            widget.ids[f'text{i}'].text = ''
            
    def hack(self,widget):
        try:
            self.initial_value = float(widget.ids.text1.text)
            self.profit_margin = float(widget.ids.text2.text)
            self.end_margin = float(widget.ids.text3.text)
            self.turn_over = int(widget.ids.text4.text)
            App.get_running_app().anim_popup.auto_dismiss = False
            App.get_running_app().anim_popup.title = 'executing...'
            App.get_running_app().anim_popup.open()
            self.event = Clock.schedule_interval(App.get_running_app().generate,random.randrange(300,500)/10**4)
            self.data_popup.dismiss()
        except Exception:
            App.get_running_app().error_popup.open()
            
    def assign(self):
        self.ids.lab1.text = cal.cal(self.initial_value,self.profit_margin,self.end_margin,self.turn_over,'normal')
        self.ids.lab2.text = cal.cal(self.initial_value,self.profit_margin,self.end_margin,self.turn_over,'round')
        self.ids.lab3.text = cal.cal(self.initial_value,self.profit_margin,self.end_margin,self.turn_over,'slow')
        self.ids.lab4.text = cal.cal(self.initial_value,self.profit_margin,self.end_margin,self.turn_over,'fast')
        
class ScrollableLabel(ScrollView):
    text = StringProperty('')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bar_color = 0,0,0,0
        self.bar_inactive_color = 0,0,0,0
        
class ImageButton(ButtonBehavior, Image):  
    def on_press(self):  
        App.get_running_app().sm.data_popup.open()
        
class Anim_Content(BoxLayout):
    def on_size(self,*args):
        try:
            App.get_running_app().anim_popup.height = self.height + dp(60)
        except:
            pass

class CalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ecode = ''
        self.colors = ['6fffe9','02c39a','00b4d8','fcfffd','ff8360','2b2c28','ffc43d','ef476f','f2b5d4']
        new_color = ['6fffe9','02c39a','00b4d8','fcfffd','ff8360','2b2c28','ffc43d','ef476f','f2b5d4']
        random.shuffle(new_color)
        for color in new_color:
            my_button = Button(text=color,
                               background_normal='',
                               background_down='',
                               color=(0,0,0,0),
                               background_color=get_color_from_hex(color),
                               on_press=self.check)
            self.ids.grid.add_widget(my_button)
            
        date = str(datetime.date.today()).split('-')
        time = str(datetime.datetime.now().time()).split(':')[:2]
        self.code = str((int(date[0])-int(date[1])+int(date[2]))+int(time[0]+time[1])).replace('0','9')
        
    def check(self,*args):
        self.ecode += str(self.colors.index(args[0].text)+1)
        if int(self.ecode) == int(self.code):
            App.get_running_app().manager.current = 'second'
        
class ActivityApp(App):
    
    def generate(self,dt):
        with open('anim.txt', 'r') as jabber:
            lines = jabber.readlines()
        lines = [line.strip() for line in lines]
        self.anim_popup.content.ids.lab.text = lines[self.counter]
        self.counter += 1
        if self.counter == len(lines):
            self.sm.assign()
            self.sm.ids.scroll.scroll_y = 1
            self.counter = 0
            App.get_running_app().anim_popup.auto_dismiss = True
            self.anim_popup.title = 'completed'
            self.sm.event.cancel()

    def build(self):
        self.counter = 0
        self.hack_color = 'ff0000'
        self.error_popup = Popup(title='Alert',
                                content=Label(text='Error!',
                                              font_name='hack-italic'),
                                auto_dismiss=True,
                                size_hint=(.8,.5))
        self.anim_popup = Popup(title='executing...',
                                content=Anim_Content(),
                                auto_dismiss=False,
                                size_hint=(.8,None))
        self.anim_popup.title_font = 'hack-italic'
        self.anim_popup.title_size = '17sp'
        self.sm = MainScreen(name='second')
        self.manager = ScreenManager()
        self.manager.transition.direction = 'up'
        self.manager.transition.duration = 1
        self.manager.add_widget(CalScreen(name='first'))
        self.manager.add_widget(self.sm)
        return self.manager

LabelBase.register(name='hack', 
                   fn_regular='courbd.ttf')

LabelBase.register(name='hack-italic', 
                   fn_regular='couri.ttf')

if __name__ == '__main__':
    ActivityApp().run()