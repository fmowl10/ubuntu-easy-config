from gi.repository import Gtk


# This is Main Window Frame
global WINDOW

# You should put '/' at the end of path.
# [PATH]
global TEXT_PATH
global IMAGE_PATH
global PAGE_PATH

TEXT_PATH = "../assets/text/"
IMAGE_PATH = "../assets/images/"
PAGE_PATH = "../pages/"


# [COMMON FUNCTIONS]
def init_flowbox():
    _box = Gtk.FlowBox()
    _box.set_max_children_per_line(1)
    _box.set_homogeneous(True)

    return _box


def init_grid():
    _box = Gtk.Grid()

    return _box


def init_scroll(flowbox):
    _scroll = Gtk.ScrolledWindow()
    _scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.ALWAYS)
    _scroll.add(flowbox)

    return _scroll


def set_button_image(image_path):
    _button = Gtk.Button()
    _image = Gtk.Image()

    _image.set_from_file(image_path)
    _image.size_request()
    _button.set_image(_image)

    return _button
