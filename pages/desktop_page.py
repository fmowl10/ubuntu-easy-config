# Part of ubuntu-easy-config https://github.com/minwook-shin/ubuntu-easy-config
#
# See LICENSE file for copyright and license details
#
# This program written for beginner for ubuntu and "ubuntu Setting" by minwook Shin and hedone21, fmowl10

from gi.repository import Gtk
import common
import gettext
import locale
import logging

def init_localization():
  locale.setlocale(locale.LC_ALL, '') # use user's preferred locale
  # take first two characters of country code
  loc = locale.getlocale()
  filename = "../lang/desktop_%s.mo" % locale.getlocale()[0][0:2]

  try:
    logging.debug( "Opening message file %s for locale %s", filename, loc[0] )
    trans = gettext.GNUTranslations(open( filename, "rb" ) )
  except IOError:
    logging.debug( "Locale not found. Using default messages" )
    trans = gettext.NullTranslations()

  trans.install()

if __name__ == '__main__':
  init_localization()

class DesktopPage(Gtk.ScrolledWindow):

    def __init__(self):
        self.intro()

    def intro(self):
        _desktop_box = common.init_flowbox()

        _unity_button = \
            common.set_button_image(common.IMAGE_PATH + "unity_top.png")
        _gnome3_button = \
            common.set_button_image(common.IMAGE_PATH + "gnome3_top.png")
        _kde5_button = \
            common.set_button_image(common.IMAGE_PATH + "kde5_top.png")

        _unity_button.connect("clicked",
                              self.on_desktop_button_clicked,
                              "unity")
        _gnome3_button.connect("clicked",
                               self.on_desktop_button_clicked,
                               "gnome3")
        _kde5_button.connect("clicked",
                             self.on_desktop_button_clicked,
                             "kde5")

        _desktop_box.insert(_unity_button, 0)
        _desktop_box.insert(_gnome3_button, 1)
        _desktop_box.insert(_kde5_button, 2)
        _desktop_scrolled = common.init_scroll(_desktop_box)

        return _desktop_scrolled

    def get_desktop_page(self, desktop):
        _grid = Gtk.Grid()
        _image = Gtk.Image()
        _text = Gtk.TextView()
        _buffer = Gtk.TextBuffer()
        _return_button = Gtk.Button(_("Return"))
        _install_button = Gtk.Button(_("Install"))

        _file = open(common.TEXT_PATH + desktop, 'r')

        _image.set_from_file(common.IMAGE_PATH + desktop + '.png')
        _image.set_alignment(0.5, 0.5)

        _buffer.set_text(_file.read())
        _text.set_buffer(_buffer)
        _text.set_wrap_mode(Gtk.WrapMode.WORD)
        _return_button.connect("clicked",
                               self.on_return_button_clicked,
                               None)

        _grid.set_column_homogeneous(True)
        _grid.attach(_image, 0, 0, 2, 1)
        _grid.attach(_text, 0, 1, 2, 1)
        _grid.attach(_return_button, 0, 2, 1, 1)
        _grid.attach(_install_button, 1, 2, 1, 1)

        _scroll = common.init_scroll(_grid)

        _file.close()

        return _scroll

    def on_desktop_button_clicked(self, button, data):
        common.WINDOW.desktop_page = self.get_desktop_page(data)

        _label = Gtk.Label(_("Choose Desktop Environment"))

        common.WINDOW.notebook.remove_page(0)
        common.WINDOW.notebook.prepend_page(common.WINDOW.desktop_page, _label)

        common.WINDOW.show_all()
        common.WINDOW.notebook.set_current_page(0)

    def on_return_button_clicked(self, button, data):
        common.WINDOW.desktop_page = self.intro()

        _label = Gtk.Label(_("Choose Desktop Environment"))

        common.WINDOW.notebook.remove_page(0)
        common.WINDOW.notebook.prepend_page(common.WINDOW.desktop_page, _label)

        common.WINDOW.show_all()
        common.WINDOW.notebook.set_current_page(0)

    def on_install_button_clicked(self, button, data):
        self.popup_desktop_install_dialog(data)
