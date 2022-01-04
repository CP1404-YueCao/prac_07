from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Name_1", "Name_2", "Name_3"}
