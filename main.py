from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

kv = '''
<Marvel>
  Label:
    id: loki
    text: 'loki: I AM YOUR GOD!'
  Button:
    id: hulk
    text: "press to smash loki"
    on_release: root.hulk_smash()
  Button:
    id: qwe
    text: 'fuck you mum'
    on_release: root.leave()
    
Marvel:
    
'''

class Marvel(BoxLayout):
    def hulk_smash(self):
        self.ids.hulk.text = "hulk: puny god!"
        self.ids["loki"].text = "loki: >_<!!!"


    def leave(self):
        self.ids.hulk.text = 'qweasdzxc'

class MyApp(App):
    def build(self):
        return Builder.load_string(kv)


MyApp().run()