
import kivy
from kivy.uix.label import Label
from kivy.app import App

kivy.require("2.0.0")

class yourApp(App):
    def build(self):
        return Label(text="tech with tim")


if __name__ == "__main__":
   app = yourApp()
   app.run()

