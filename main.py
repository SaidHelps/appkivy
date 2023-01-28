from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.animation import Animation
import smtplib
import time

user = "shaggymufson21@gmail.com"
passwd = "bfjhcjwhfxivjyrh"
server = "smtp.gmail.com"
port = 587
charset = 'Content-Type: text/plain; charset=utf-8'
mime = 'MIME-Version: 1.0'


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.odin = 0
        self.bad = 0
        self.good = 0


    def build(self):
        self.sm = ScreenManager()
        self.screen1 = Screen(name="Main screen")
        self.screen2 = Screen(name="second screen")
        self.screen3 = Screen(name="thank")

        self.bq = BoxLayout(orientation='vertical', size_hint=(.3, .5))
        self.bq.add_widget(Button(text="1", on_press=lambda x:self.toset(qwe=1)))
        self.bq.add_widget(Button(text="2", on_press=lambda x:self.toset(qwe=2)))
        self.bq.add_widget(Button(text="3", on_press=lambda x:self.toset(qwe=3)))
        self.bq.add_widget(Button(text="4", on_press=lambda x:self.toset(qwe=4)))


        self.bl = FloatLayout(size=(300, 300))
        self.bl.add_widget(Label(text="Оцените Вкус Еды в Столовой!", font_size=50, pos_hint={'x' : 0, 'y' : .4}))

        self.bl.add_widget(self.bq)

        self.stable()

        self.Last = Image(source="3.png", pos_hint={'x': .5, 'y': .2}, size_hint=(.4, .4))
        self.bl.add_widget(self.Last)
        self.Thanks = Label(text="Спасибо за голос!", font_size=50, text_size=(900, 500), pos_hint={'x' : .3, 'y' : .4})
        self.qs = FloatLayout(size=(1000, 1000))
        self.qs.add_widget(self.Thanks)

        # Second window





        self.screen1.add_widget(self.bl)
        self.sm.add_widget(self.screen1)
        self.sm.add_widget(self.screen2)
        self.sm.add_widget(self.screen3)

        return self.sm

    def stable(self):

        try:
            self.bl.remove_widget(self.img1)
            self.bl.remove_widget(self.img2)
            self.bl.remove_widget(self.img3)
            self.bl.remove_widget(self.img4)
            self.bl.remove_widget(self.img5)
        except:
            pass

        self.img1 = Image(source="img1.png", pos_hint={'x': .45, 'y': .35}, size_hint=(.09, .09))
        self.img2 = Image(source="img2.png", pos_hint={'x': .53, 'y': .47}, size_hint=(.09, .09))
        self.img3 = Image(source="img3.png", pos_hint={'x': .655, 'y': .52}, size_hint=(.09, .09))
        self.img4 = Image(source="img4.png", pos_hint={'x': .78, 'y': .47}, size_hint=(.09, .09))
        self.img5 = Image(source="img5.png", pos_hint={'x': .86, 'y': .35}, size_hint=(.09, .09))


        self.bl.add_widget(self.img1)
        self.bl.add_widget(self.img2)
        self.bl.add_widget(self.img3)
        self.bl.add_widget(self.img4)
        self.bl.add_widget(self.img5)

    def toset(self, qwe):
        self.wq = FloatLayout(size=(300, 600))
        self.wqClone = BoxLayout(orientation='vertical', size_hint=(.4, .6))
        self.wqClone.add_widget(Button(text="Ужасно!", text_size=(300, 40), on_press=lambda x: self.golosMinus(num=3, loq=qwe)))
        self.wqClone.add_widget(Button(text="Плохо", text_size=(300, 40), on_press=lambda x: self.golosMinus(num=2, loq=qwe)))
        self.wqClone.add_widget(Button(text="Среднее", text_size=(300, 40), on_press=lambda x: self.golosPlus(num=1, loq=qwe)))
        self.wqClone.add_widget(Button(text="Нормально", text_size=(300, 40), on_press=lambda x: self.golosPlus(num=2, loq=qwe)))
        self.wqClone.add_widget(Button(text="Превосходно!", text_size=(300, 40), on_press=lambda x: self.golosPlus(num=3, loq=qwe)))

        self.screen2.remove_widget(self.wq)
        self.screen2.add_widget(self.wq)
        self.sm.current = "second screen"
        self.wq.clear_widgets()
        self.wq.add_widget(self.wqClone)
        self.wq.add_widget(Button(text="Назад к главному окну ==>", on_press=self.tomain, size_hint=(1, .1), pos_hint={'x':0, 'y':.9}))


    def tomain(self, instance):
        self.sm.current = "Main screen"




    def golosMinus(self, num, loq):
        zon = None
        self.odin += num
        self.bad += num
        if num == 2:
            zon = "Плохо"
        elif num == 3:
            zon = "Ужасно!"
        self.proshayLichnayaZhinh(kurs=loq, message=zon)


    def golosPlus(self, num, loq):
        zon = None
        self.odin += num
        self.good += num
        if num == 2:
            zon = "Нормально"
        elif num == 1:
            zon = "Среднее"
        elif num == 3:
            zon = "Превосходно!"
        self.proshayLichnayaZhinh(kurs=loq, message=zon)





    def proshayLichnayaZhinh(self, kurs, message):
        wq = self.odin / 1.4

        if self.good > self.bad:
            if wq < self.good:
                self.stable()
                self.bl.remove_widget(self.Last)
                self.Last.source = "5.png"
                self.bl.add_widget(self.Last)
                self.bl.remove_widget(self.img5)
                self.bl.add_widget(self.img5)
                self.img5.size_hint = (.13, .13)
                self.img5.pos_hint = {'x': .86, 'y': .34}
            elif wq > self.good:
                self.stable()
                self.bl.remove_widget(self.Last)
                self.Last.source = "4.png"
                self.bl.add_widget(self.Last)
                self.bl.remove_widget(self.img4)
                self.bl.add_widget(self.img4)
                self.img4.size_hint = (.13, .13)
                self.img4.pos_hint = {'x': .78, 'y': .47}
        elif self.good < self.bad:
            if wq < self.bad:
                self.stable()
                self.bl.remove_widget(self.Last)
                self.Last.source = "1.png"
                self.bl.add_widget(self.Last)
                self.bl.remove_widget(self.img1)
                self.bl.add_widget(self.img1)
                self.img1.size_hint = (.13, .13)
                self.img1.pos_hint = {'x': .4, 'y': .32}
            elif wq > self.bad:
                self.stable()
                self.bl.remove_widget(self.Last)
                self.Last.source = "2.png"
                self.bl.add_widget(self.Last)
                self.bl.remove_widget(self.img2)
                self.bl.add_widget(self.img2)
                self.img2.size_hint = (.13, .13)
                self.img2.pos_hint = {'x': .5, 'y': .47}
        elif self.good == self.bad:
            self.stable()
            self.bl.remove_widget(self.Last)
            self.Last.source = "3.png"
            self.bl.add_widget(self.Last)
            self.bl.remove_widget(self.img3)
            self.bl.add_widget(self.img3)
            self.img3.size_hint = (.13, .13)
            self.img3.pos_hint = {'x': .635, 'y': .52}


        to = "shaggymufson21@gmail.com"
        subject = "Курс обучения: " + str(kurs) + ", оценка: " + str(message)
        text = str(self.bad) + " Плохих голосов, " + str(self.good) + " Хороших голосов, " + str(self.odin) + " Общее количество голосов."

        body = "\r\n".join((f"From: {user}", f"To: {to}", f"Subject: {subject}", mime, charset, "", text))

        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.login(user, passwd)
        smtp.sendmail(user, to, body.encode('utf-8'))

        print("Отправленно!")

        self.sm.current = "Main screen"



MyApp().run()
