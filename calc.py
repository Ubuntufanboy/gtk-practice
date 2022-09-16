import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class Calculator(Gtk.Window):
    def __init__(self) -> None:
        super().__init__(title="YouTube Downloader")
        self.set_size_request(500, 500)

        row1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6) # making the first row
        self.add(row1)
        
        # making a list of the buttons relevent to the operation
        self.work = []
        button1 = Gtk.Button.new_with_label("1")
        button1.connect("clicked", self.on_one_clicked)
        row1.pack_start(button1, True, True, 0)
        
        def on_one_clicked(self, button):
            self.work.append(1)
        button2 = Gtk.Button.new_with_label("2")
        button2.connect("clicked", self.on_two_clicked)
        row1.pack_start(button2, True, True, 0)
        
        button3 = Gtk.Button.new_with_label("3")
        button3.connect("clicked", self.on_three_clicked)
        row1.pack_start(button3, True, True, 0)

        # Second Row
        row2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6) # making the first row
        self.add(row2)
        
        button4 = Gtk.Button.new_with_label("4")
        button4.connect("clicked", self.on_four_clicked)
        row2.pack_start(button4, True, True, 0)

        button5 = Gtk.Button.new_with_label("5")
        button5.connect("clicked", self.on_five_clicked)
        row2.pack_start(button5, True, True, 0)

        button6 = Gtk.Button.new_with_label("6")
        button6.connect("clicked", self.on_six_clicked)
        row2.pack_start(button6, True, True, 0)

win = Calculator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()