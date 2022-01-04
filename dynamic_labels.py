from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Name_1", "Name_2", "Name_3"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def display_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widgets(temp_label)


DynamicLabelsApp().run()