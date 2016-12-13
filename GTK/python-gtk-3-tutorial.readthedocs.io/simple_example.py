_author_ = 'Erick'
import gi
gi.require_version('Gtk', '3.0') # to import the Gtk module to be able to access GTK+’s classes and functions
from gi.repository import Gtk

win = Gtk.Window() # creates an empty window.
win.connect("delete-event", Gtk.main_quit) #  connecting to the window’s delete event to ensure click x termination
win.show_all() # we display the window.
Gtk.main() # we start the GTK+ processing loop