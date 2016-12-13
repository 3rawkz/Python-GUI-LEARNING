_author_ = 'Erick'
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window): # Define a subclass

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World") #calling constructur of super class and ad title

        self.button = Gtk.Button(label="Click Here")          #Creating buttons
        self.button.connect("clicked", self.on_button_clicked)# connect clicked signal and add it ass child to top-level window
        self.add(self.button)                                 #

    def on_button_clicked(self, widget): # method on_button_clicked
        print("Hello World")             # will be called

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()