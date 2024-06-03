#Import Modules
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.toast import toast
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivy.core.window import Window
#from kivytransitions.transitions import SimpleZoom,PageCurl

#Other Backend Modules
import datetime

# #Resizing To Mobile view
# Window.size = (300,600)

#Define Classes
class WeatherScreen(MDScreen):
    def check(self):
        date = str(datetime.date.today()).split('-')
        time = str(datetime.datetime.now().time()).split(':')[:2]
        if self.ids.search.text == f'{date[1]}>{date[0]}<<{date[2]}>>>{int(time[0])+int(time[1])}':
            MDApp.get_running_app().sm.current = 'login'

class LoginScreen(MDScreen):
    def check(self):
        #MDApp.get_running_app().sm.transition = PageCurl(duration=2)
        if self.ids.loginpass.text == 'tihudikhordharasala':
            MDApp.get_running_app().sm.current = 'hack'

class HackScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profit = 0
        for i in range(7,15):
            mylabel = MDLabel(text=f'''[color=#17181c][font=poppinsbold]{i}[/font][/color]''',
                              markup=True,
                              halign='center',
                              )
            self.ids[f'lab{i}'] = mylabel
            self.ids.mygrid.add_widget(Image(source=f'images/{i}.png'))
            self.ids.mygrid.add_widget(mylabel)
        self.evaluate()
            
            
    def evaluate(self):
        if len(self.ids.profit.text):
            try:
                self.profit = float(self.ids.profit.text)
            except:
                self.ids.profit.error = True
        else:
            self.profit = 0
        values = [0.477*self.profit,0.668*self.profit,0.795*self.profit,0.859*self.profit]
        for i in range(0,4):
            self.ids[f'lab{7+i}'].text = f'[font=poppinsbold]{values[i]}[/font]'
            self.ids[f'lab{14-i}'].text = f'[font=poppinsbold]{values[i]}[/font]'
        self.ids.amount.text = f'[font=poppinsbold]{2 * sum(values)}[/font]'
            
#Main App Class
class BigDaddyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.material_style = 'M3'
        self.sm = ScreenManager()
        #self.sm.transition = SimpleZoom(duration=2)
        self.sm.add_widget(WeatherScreen(name='weather'))
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(HackScreen(name='hack'))
        return self.sm

#Custom font
LabelBase.register(name='poppins', 
                   fn_regular='font/Poppins-Medium.ttf')

LabelBase.register(name='poppinsbold', 
                   fn_regular='font/Poppins-Bold.ttf')

LabelBase.register(name='hack', 
                   fn_regular='font/cour.ttf')

#Running App    
if __name__ == '__main__':
    BigDaddyApp().run()
