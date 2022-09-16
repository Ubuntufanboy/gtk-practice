import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class Downloader(Gtk.Window):
    def __init__(self):
        super().__init__(title="YouTube Downloader")
        self.set_size_request(300, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Enter text here")
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)
        self.entry.set_editable(True)
        self.entry.set_visibility(True)
            
        button = Gtk.Button.new_with_label("Enter")
        button.connect("clicked", self.on_enter_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_enter_clicked(self, button):
        print("Download button has been clicked! Running downloader!")
        import os
        cwd = os.cwd()
        os.system("mkdir Videos")
        os.system("cd Videos")
win = Downloader()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()