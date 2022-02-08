from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class LessonsWidget(BoxLayout):
    pass

class TestsWidget(BoxLayout):
    pass

class SettingsWidget(BoxLayout):
    pass


class RootWidget(ScreenManager):
    pass

class MainApp(MDApp):
    
    lesson = "lesson "
    test = "test "

        

    def on_start(self):
        
        for i in range(1, 9):
            button1 = Button(text=self.lesson + str(i))
            button1.bind(on_release=lambda x: print(button1) )
            self.root.ids.lessons_widget.add_widget(button1)
    
        for i in range(1, 10):
            button = Button(text=self.test+ str(i))
            self.root.ids.test_widget.add_widget(button)
        
    
    
    def build(self):
        return RootWidget()
    
    
MainApp().run()
        