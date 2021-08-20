import instaloader
import threading
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton
bot = instaloader.Instaloader()
User_Name = '''
MDTextField:
    hint_text: 'Enter user_name here.'
    size_hint_x:None
    pos_hint:{'center_x':.5,'center_y':.5}
    helper_text_mode:'on_focus'
    helper_text:"Enter user_name"
    required:True
    width:230
'''
class Instgram_scrapper(MDApp):
    def build(self):
        self.screen = Screen()
        Window.size = (350, 640)
        self.user_name = Builder.load_string(User_Name)
        self.label = MDLabel(text = "Instgram Loader",
                                pos_hint = {'center_x':.7,'center_y':.9},
                                font_style = "H5")
        self.press_btn = MDRoundFlatButton(text = "start",
                                            on_press = self.user_loader_threading,
                                            pos_hint = {'center_x':.5,'center_y':.2},
                                            size_hint = (.35,.059))
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.user_name)
        self.screen.add_widget(self.press_btn)
        return self.screen
    def user_loader(self):
        profile = instaloader.Profile.from_username(bot.context, self.user_name.text)
        self.label.text = "Instgram data"
        self.label.pos_hint = {'center_x':.75,'center_y':.9}
        self.screen.clear_widgets()
        self.screen.add_widget(self.label)
        l1 = MDLabel(text = "Username: " + profile.username,
                                pos_hint = {'center_x':.53,'center_y':.8})
        l2 = MDLabel(text = "User ID: " + str(profile.userid),
                                pos_hint = {'center_x':.53,'center_y':.75})
        l3 = MDLabel(text = "Number of Posts: "+ str(profile.mediacount),
                                pos_hint = {'center_x':.53,'center_y':.7})
        l4 = MDLabel(text = "Followers: " + str(profile.followers),
                                pos_hint = {'center_x':.53,'center_y':.65})
        l5 = MDLabel(text = "Followees: "+ str(profile.followees),
                                pos_hint = {'center_x':.53,'center_y':.6})
        l6 = MDLabel(text = "Bio: "+ str(profile.biography)+str(profile.external_url),
                                pos_hint = {'center_x':.53,'center_y':.55})
        self.return_btn = MDRoundFlatButton(text = "return back",
                                            on_press = self.return_back,
                                            pos_hint = {'center_x':.5,'center_y':.2},
                                            size_hint = (.4,.059))
        
        self.screen.add_widget(l1)
        self.screen.add_widget(l2)
        self.screen.add_widget(l3)
        self.screen.add_widget(l4)
        self.screen.add_widget(l5)
        self.screen.add_widget(l6)
        self.screen.add_widget(self.return_btn)
    def user_loader_threading(self,*args):
        thread_login = threading.Thread(target = self.user_loader)
        thread_login.start()
    def return_back(self,*args):
        self.label = MDLabel(text = "Instgram Loader",
                                pos_hint = {'center_x':.7,'center_y':.9},
                                font_style = "H5")
        self.screen.clear_widgets()
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.user_name)
        self.screen.add_widget(self.press_btn)
Instgram_scrapper().run()
