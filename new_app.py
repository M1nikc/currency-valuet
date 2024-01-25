from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import requests
from bs4 import BeautifulSoup
from logik import get_currency_rate
first_valuet=' '
second_screen_valuet=' '
result=0
color_window=(0.4,0.5,0.6,1)
Window.clearcolor=color_window
btn_color=(0.4,0.7,0.3,1)
btn_background_color=btn_color
class MyScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)                                                          
        txt_start=Label(text="выберите валюту \n которую хотите перевести",color='white',halign='center',font_size='22sp',pos_hint={'center_x':0.5,'center_y':0.2})  
        box1=BoxLayout(orientation="horizontal",padding=8,spacing=8)                    
        box2=BoxLayout(orientation="vertical",padding=8,spacing=8)
        box3=BoxLayout(orientation="vertical",padding=8,spacing=8,pos_hint={'center_x':0.5,'center_y':0.95})
        box4=BoxLayout(orientation="vertical",padding=8,spacing=8)
        self.btn_1_screen_1=Button(text="доллар",font_size='20sp')
        self.btn_2_screen_1=Button(text="евро",font_size='20sp')
        self.btn_3_screen_1=Button(text="рубль",font_size='20sp')
        self.btn_4_screen_1=Button(text="юани",font_size='20sp')
        self.btn_5_screen_1=Button(text="белорусские рубли",font_size='20sp')
        self.btn_6_screen_1=Button(text="тенге",font_size='20sp')
        self.btn_1_screen_1.background_color=btn_color
        self.btn_2_screen_1.background_color=btn_color
        self.btn_3_screen_1.background_color=btn_color
        self.btn_4_screen_1.background_color=btn_color
        self.btn_5_screen_1.background_color=btn_color
        self.btn_6_screen_1.background_color=btn_color
        box2.add_widget(self.btn_1_screen_1)
        box2.add_widget(self.btn_2_screen_1)
        box2.add_widget(self.btn_3_screen_1)
        box3.add_widget(txt_start)
        box4.add_widget(self.btn_4_screen_1)
        box4.add_widget(self.btn_5_screen_1)
        box4.add_widget(self.btn_6_screen_1)
        box1.add_widget(box2)
        box1.add_widget(box3)
        box1.add_widget(box4)
        self.add_widget(box1)
        self.btn_1_screen_1.on_press=self.next_1
        self.btn_2_screen_1.on_press=self.next_2
        self.btn_3_screen_1.on_press=self.next_3
        self.btn_4_screen_1.on_press=self.next_4
        self.btn_5_screen_1.on_press=self.next_5
        self.btn_6_screen_1.on_press=self.next_6
    def next_1(self):
        global first_valuet   
        first_valuet="курс доллара к"
        self.manager.current = 'screen_2'
    def next_2(self):
        global first_valuet   
        first_valuet="курс евро к"
        self.manager.current = 'screen_2'
    def next_3(self):
        global first_valuet   
        first_valuet="курс рубля к"
        self.manager.current = 'screen_2'
    def next_4(self):
        global first_valuet   
        first_valuet="курс юаня к"
        self.manager.current = 'screen_2'
    def next_5(self):
        global first_valuet   
        first_valuet="курс беллоруского рубля к"
        self.manager.current = 'screen_2'
    def next_6(self):
        global first_valuet   
        first_valuet="курс тенге к"
        self.manager.current = 'screen_2'

class Second_screen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        txt_start=Label(text="выберите валюту \n в которую хотите перевести",color='white',halign='center',font_size='20sp',pos_hint={'center_x':0.5,'center_y':0.2})  
        box1=BoxLayout(orientation="horizontal",padding=8,spacing=8)                    
        box2=BoxLayout(orientation="vertical",padding=8,spacing=8)
        box3=BoxLayout(orientation="vertical",padding=8,spacing=8,pos_hint={'center_x':0.5,'center_y':0.95})
        box4=BoxLayout(orientation="vertical",padding=8,spacing=8)
        self.btn_1_screen_1=Button(text="доллар",font_size='20sp')
        self.btn_2_screen_1=Button(text="евро",font_size='20sp')
        self.btn_3_screen_1=Button(text="рубль",font_size='20sp')
        self.btn_4_screen_1=Button(text="юани",font_size='20sp')
        self.btn_5_screen_1=Button(text="белорусские рубли",font_size='20sp')
        self.btn_6_screen_1=Button(text="тенге",font_size='20sp')
        self.btn_1_screen_1.background_color=btn_color
        self.btn_2_screen_1.background_color=btn_color
        self.btn_3_screen_1.background_color=btn_color
        self.btn_4_screen_1.background_color=btn_color
        self.btn_5_screen_1.background_color=btn_color
        self.btn_6_screen_1.background_color=btn_color
        box2.add_widget(self.btn_1_screen_1)
        box2.add_widget(self.btn_2_screen_1)
        box2.add_widget(self.btn_3_screen_1)
        box3.add_widget(txt_start)
        box4.add_widget(self.btn_4_screen_1)
        box4.add_widget(self.btn_5_screen_1)
        box4.add_widget(self.btn_6_screen_1)
        box1.add_widget(box2)
        box1.add_widget(box3)
        box1.add_widget(box4)
        self.add_widget(box1)
        self.btn_1_screen_1.on_press=self.next_1
        self.btn_2_screen_1.on_press=self.next_2
        self.btn_3_screen_1.on_press=self.next_3
        self.btn_4_screen_1.on_press=self.next_4
        self.btn_5_screen_1.on_press=self.next_5
        self.btn_6_screen_1.on_press=self.next_6
    def next_1(self):
        global first_valuet,result   
        query=first_valuet + " доллару"
        query = query.replace(" ", "+")
        result=get_currency_rate(query)
        self.manager.current = 'screen_3'
    def next_2(self):
        global first_valuet ,result 
        query=first_valuet + " евро"
        query = query.replace(" ", "+")
        result=get_currency_rate(query)
        self.manager.current = 'screen_3'
    def next_3(self):
        global first_valuet,result 
        query=first_valuet + " рублю"
        query = query.replace(" ", "+")
        result=get_currency_rate(query)
        self.manager.current = 'screen_3'
    def next_4(self):
        global first_valuet,result 
        query=first_valuet + " юаню"
        query = query.replace(" ", "+")
        result=get_currency_rate(query)
        self.manager.current = 'screen_3'
    def next_5(self):
        global first_valuet,result 
        query=first_valuet + " белорусскому рублю"
        query = query.replace(" ", "+")
        result=get_currency_rate(query)
        self.manager.current = 'screen_3'
    def next_6(self):
        global first_valuet,result 
        query=first_valuet + " тенге"
        query = query.replace(" ", "+")
        result=get_currency_rate(query)
        self.manager.current = 'screen_3'


class Last_screen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        txt_start=Label(text="Итог перевода",color='white',halign='center',font_size='40sp',pos_hint={'center_x':0.5,'center_y':0.8})
        print(result)
        self.txt_itog=Label(text='',color='white',halign='center',font_size='40sp',pos_hint={'center_x':0.5,'center_y':0.8})
        box1=BoxLayout(orientation="vertical",padding=8,spacing=8,pos_hint={'center_x':0.5,'center_y':0.65})
        box1.add_widget(txt_start)
        box1.add_widget(self.txt_itog)
        self.add_widget(box1)
        self.on_enter=self.before
    def before(self):
        global result
        self.txt_itog.text=str(result)
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyScreen(name='screen_1'))
        sm.add_widget(Second_screen(name='screen_2'))
        sm.add_widget(Last_screen(name='screen_3'))
        return sm
app= MyApp()
app.run()



