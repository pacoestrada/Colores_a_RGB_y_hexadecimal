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
    # ... continuar con el resto de los colores
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

