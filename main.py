from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello Kivy')

if __name__ == '__main__':
    TestApp().run()
