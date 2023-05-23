import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

colores = {
     "rojo": (255, 0, 0),
    "rojo claro": (255, 102, 102),
    "rojo oscuro": (204, 0, 0),
    "verde": (0, 255, 0),
    "verde claro": (102, 255, 102),
    "verde oscuro": (0, 204, 0),
    "azul": (0, 0, 255),
    "azul claro": (102, 102, 255),
    "azul oscuro": (0, 0, 204),
    "amarillo": (255, 255, 0),
    "amarillo claro": (255, 255, 102),
    "amarillo oscuro": (204, 204, 0),
    "morado": (128, 0, 128),
    "morado claro": (178, 102, 255),
    "morado oscuro": (102, 0, 102),
    "naranja": (255, 165, 0),
    "naranja claro": (255, 204, 153),
    "naranja oscuro": (204, 102, 0),
    "rosa": (255, 192, 203),
    "rosa claro": (255, 204, 229),
    "rosa oscuro": (204, 102, 153),
    "blanco": (255, 255, 255),
    "negro": (0, 0, 0),
    "gris": (128, 128, 128),
    "gris claro": (192, 192, 192),
    "gris oscuro": (64, 64, 64),
    "marrón": (139, 69, 19),
    "marrón claro": (205, 133, 63),
    "marrón oscuro": (101, 67, 33),
    "beige": (245, 245, 220),
    "celeste": (178, 255, 255),
    "celeste claro": (204, 255, 255),
    "celeste oscuro": (102, 204, 204),
    "turquesa": (64, 224, 208),
    "turquesa claro": (0, 255, 255),
    "turquesa oscuro": (0, 206, 209),
    "violeta": (238, 130, 238),
    "violeta claro": (221, 160, 221),
    "violeta oscuro": (148, 0, 211),
    "amarillo limón": (255, 255, 102),
    "amarillo mostaza": (204, 204, 0),
    "verde lima": (50, 205, 50),
    "verde oliva": (128, 128, 0),
    "azul celeste": (135, 206, 235),
    "azul marino": (0, 0, 128),
    "azul pavo": (0, 128, 128),
    "rosa salmón": (250, 128, 114),
    "rosa viejo": (188, 143, 143),
    "café": (139, 69, 19),
    "oro": (255, 215, 0),
    "plata": (192, 192, 192)
}

def color_a_rgb(color):
    color = color.lower()

    if color in colores:
        return colores[color]
    else:
        return None

def rgb_a_hex(rgb):
    return '#%02x%02x%02x' % rgb

class ColorConverter(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Conversor de Colores")

        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        self.search_entry = Gtk.Entry()
        self.search_entry.connect("changed", self.on_search_entry_changed)
        vbox.pack_start(self.search_entry, False, False, 0)

        self.combo = Gtk.ComboBoxText.new()
        self.refresh_combo()
        self.combo.connect("changed", self.on_combo_changed)
        vbox.pack_start(self.combo, False, False, 0)

        self.rgb_label = Gtk.Label(label="")
        vbox.pack_start(self.rgb_label, False, False, 0)

        rgb_copy_button = Gtk.Button.new_with_label("Copiar RGB")
        rgb_copy_button.connect("clicked", self.copy_rgb)
        vbox.pack_start(rgb_copy_button, False, False, 0)

        self.hex_label = Gtk.Label(label="")
        vbox.pack_start(self.hex_label, False, False, 0)

        hex_copy_button = Gtk.Button.new_with_label("Copiar Hexadecimal")
        hex_copy_button.connect("clicked", self.copy_hex)
        vbox.pack_start(hex_copy_button, False, False, 0)

    def on_search_entry_changed(self, entry):
        self.refresh_combo()

    def refresh_combo(self):
        search_text = self.search_entry.get_text().lower()
        self.combo.remove_all()
        for color in colores.keys():
            if search_text in color:
                self.combo.append_text(color)

    def on_combo_changed(self, combo):
        color = combo.get_active_text()
        if color:
            rgb = color_a_rgb(color)
            if rgb:
                self.rgb_label.set_text(f"RGB: {rgb}")
                hex_code = rgb_a_hex(rgb)
                self.hex_label.set_text(f"Hexadecimal: {hex_code}")
            else:
                self.rgb_label.set_text(f"No se encontró una representación en RGB para el color {color}.")
                self.hex_label.set_text("")

    def copy_rgb(self, widget):
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(self.rgb_label.get_text(), -1)

    def copy_hex(self, widget):
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(self.hex_label.get_text(), -1)

win = ColorConverter()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

