import random
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Button  
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout


class Application(App):
    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
        self.all = 0
        self.bad = 0
        self.good = 0
        self.wq = 0
        self.sm = ScreenManager()
        self.screen1 = Screen(name="main")
        self.screen2 = Screen(name="second")
        self.sm.add_widget(self.screen1)
        self.sm.add_widget(self.screen2)
    
    def build(self):
        self.fl = FloatLayout()
        bl = BoxLayout(orientation="horizontal", size_hint=(.4, .4))
        bar = Image(source="gradient.png", pos_hint={'x':.8,'y':.1}, size_hint=(.1, .8))
        self.point = Image(color="red", size_hint=(.1, .005), pos_hint={'x':.7,'y':.495})
        text = Label(text="Выберите ваш курс обучения", font_size=35, pos_hint={'x':-.1,'y':.05})
        
        gl = GridLayout(cols=2, size_hint=(.4, .4), spacing=10, pos_hint={'x':.05,'y':.05})

        gl.add_widget(Button(text="1", font_size=30, on_press=lambda x:self.change(kurs=1)))
        gl.add_widget(Button(text="2", font_size=30, on_press=lambda x:self.change(kurs=2)))
        gl.add_widget(Button(text="3", font_size=30, on_press=lambda x:self.change(kurs=3)))
        gl.add_widget(Button(text="4", font_size=30, on_press=lambda x:self.change(kurs=4)))

        self.fl.add_widget(text)
        self.fl.add_widget(bar)
        self.fl.add_widget(self.point)
        self.fl.add_widget(gl)
        
        self.fl.add_widget(bl)
        self.screen1.add_widget(self.fl)
        blq = BoxLayout(orientation="horizontal")
        blq.add_widget(Button(text="main win", on_press=lambda x:self.tomain()))
        blq.add_widget(Button(text="add", on_press=lambda x:self.enjoy(num=1)))
        blq.add_widget(Button(text="get", on_press=lambda x:self.enjoy(num=-1)))
        self.screen2.add_widget(blq)

        self.thanksText = Label(text="Спасибо за голос!", font_size=70, opacity=0)
        self.screen1.add_widget(self.thanksText)
        self.fl2 = FloatLayout()

        return self.sm
    

    def change(self, kurs):
        self.sm.current = "second"


    def tomain(self):
        self.fl.opacity = 0
        self.sm.current = "main"
        anom = Animation(
            opacity=1,
            duration=2
        )

        anom += Animation(
            opacity=0,
            duration=1.5
        )
        

        anim = Animation(
            opacity=1,
            duration=1
        )

        achko = Animation(
            pos_hint={'x':.7,'y':self.wq},
            duration=random.uniform(0.5, 1.5)
        )

        def por(instance):
            if self.wq == 0:
                pass
            else:
                achko.start(self.point)

        def lor(instance):
            anim.start(self.fl)
            anim.on_complete=por

        anom.start(self.thanksText)
        anom.on_complete=lor

    def enjoy(self, num):
        self.all += 1
        if num == -1:
            self.bad += 1
        elif num == 1:
            self.good += 1

        #Максимум вверх 5
        if self.bad * 5 < self.good and self.bad * 4.7 > self.good:
            self.wq = .895
        elif self.bad == 0 and self.good != 0:
            self.wq = .895
        
        #Больше вверх 4
        if self.bad * 2.5 < self.good and self.bad * 2.7 > self.good:
            self.wq = .695

        #Центр 3
        if self.good == self.bad:
            self.wq = .495

        # Больше в низ 2
        if self.good * 2.5 < self.bad and self.good * 2.7 > self.bad:
            self.wq = .295

        #Максимум вниз 1
        if self.good * 5 < self.bad:
            self.wq = .095
        elif self.good == 0 and self.bad != 0:
            self.wq = .095


        # 4 блока 4 блока 4 блока 4 блока 4 блока 4 блока 4 блока
        if self.bad > self.good:
            # Блок 1
            if self.good * 4.7 < self.bad and self.good * 5 > self.bad:
                self.wq = .115
            elif self.good * 4.4 < self.bad and self.good * 4.7 > self.bad:
                self.wq = .130
            elif self.good * 4.1 < self.bad and self.good * 4.4 > self.bad:
                self.wq = .155
            elif self.good * 3.8 < self.bad and self.good * 4.1 > self.bad:
                self.wq = .180
            elif self.good * 3.5 < self.bad and self.good * 3.8 > self.bad:
                self.wq = .205
            elif self.good * 3.2 < self.bad and self.good * 3.5 > self.bad:
                self.wq = .240
            elif self.good * 2.9 < self.bad and self.good * 3.2 > self.bad:
                self.wq = .275
            elif self.good * 2.7 < self.bad and self.good * 2.9 > self.bad:
                self.wq = .280

            # Блок 2
            elif self.good * 2.2 < self.bad and self.good * 2.5 > self.bad:
                self.wq = .325
            elif self.good * 1.9 < self.bad and self.good * 2.2 > self.bad:
                self.wq = .350
            elif self.good * 1.6 < self.bad and self.good * 1.9 > self.bad:
                self.wq = .375
            elif self.good * 1.3 < self.bad and self.good * 1.6 > self.bad:
                self.wq = .400
            elif self.good * 1.0 < self.bad and self.good * 1.3 > self.bad:
                self.wq = .425
            elif self.good * 0.7 < self.bad and self.good * 1.0 > self.bad:
                self.wq = .450
            elif self.good * 0.5 < self.bad and self.good * 0.7 > self.bad:
                self.wq = .475
            elif self.good * 0.3 < self.bad and self.good * 0.5 > self.bad:
                self.wq = .485

        if self.good > self.bad:
                # Блок 3
            if self.bad * 0.3 < self.good and self.bad * 0.5 > self.good:
                self.wq = .525
            elif self.bad * 0.5 < self.good and self.bad * 0.7 > self.good:
                self.wq = .550
            elif self.bad * 0.7 < self.good and self.bad * 1.0 > self.good:
                self.wq = .575
            elif self.bad * 1.0 < self.good and self.bad * 1.3 > self.good:
                self.wq = .600
            elif self.bad * 1.3 < self.good and self.bad * 1.6 > self.good:
                self.wq = .625
            elif self.bad * 1.6 < self.good and self.bad * 1.9 > self.good:
                self.wq = .650
            elif self.bad * 1.9 < self.good and self.bad * 2.2 > self.good:
                self.wq = .675
            elif self.bad * 2.2 < self.good and self.bad * 2.5 > self.good:
                self.wq = .685

                # Блок 4
            if self.bad * 2.7 < self.good and self.bad * 2.9 > self.good:
                self.wq = .725
            elif self.bad * 3.0 < self.good and self.bad * 3.2 > self.good:
                self.wq = .750
            elif self.bad * 3.3 < self.good and self.bad * 3.5 > self.good:
                self.wq = .775
            elif self.bad * 3.6 < self.good and self.bad * 3.8 > self.good:
                self.wq = .800
            elif self.bad * 3.9 < self.good and self.bad * 4.1 > self.good:
                self.wq = .825
            elif self.bad * 4.2 < self.good and self.bad * 4.4 > self.good:
                self.wq = .850
            elif self.bad * 4.5 < self.good and self.bad * 4.7 > self.good:
                self.wq = .875
            elif self.bad * 4.7 < self.good and self.bad * 5.0 > self.good:
                self.wq = .885

        self.tomain
        
        


Application().run()