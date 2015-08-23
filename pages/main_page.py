from gi.repository import Gtk
from desktop_page import DesktopPage
import common
import gettext
import locale
import logging

def init_localization():
  locale.setlocale(locale.LC_ALL, '') # use user's preferred locale
  # take first two characters of country code
  loc = locale.getlocale()
  filename = "../lang/main/messages_%s.mo" % locale.getlocale()[0][0:2]

  try:
    logging.debug( "Opening message file %s for locale %s", filename, loc[0] )
    trans = gettext.GNUTranslations(open( filename, "rb" ) )
  except IOError:
    logging.debug( "Locale not found. Using default messages" )
    trans = gettext.NullTranslations()

  trans.install()

if __name__ == '__main__':
  init_localization()

class MainPage(Gtk.Window):

    desktop_page = Gtk.ScrolledWindow()
    lang_page = Gtk.ScrolledWindow()
    tweak_page = Gtk.ScrolledWindow()

    notebook = Gtk.Notebook()

    def __init__(self):
        Gtk.Window.__init__(self, title=_("Ubuntu Config"))
        self.set_default_size(1040, 600)

        self.notebook.set_tab_pos(Gtk.PositionType.LEFT)

        lang_box = common.init_flowbox()
        tweak_box = common.init_flowbox()

        label1 = Gtk.Label(label=_("Choose Desktop Environment"))
        label2 = Gtk.Label(label=_("Set Language IM"))
        label3 = Gtk.Label(label=_("Tweak Desktop"))

        self.desktop_page = DesktopPage()
        self.lang_page = lang_box
        self.tweak_page = tweak_box

        self.notebook.append_page(self.desktop_page.intro(), label1)
        self.notebook.append_page(self.lang_page, label2)
        self.notebook.append_page(self.tweak_page, label3)

        self.add(self.notebook)

    def popup_desktop_install_dialog(self, desktop):
        _dialog = Gtk.Dialog(title="Desktop Install", button="Install")

        _dialog.run()


common.WINDOW = MainPage()
common.WINDOW.connect("delete-event", Gtk.main_quit)
common.WINDOW.show_all()
Gtk.main()
