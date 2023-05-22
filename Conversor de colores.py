import tkinter as tk
from tkinter import ttk, StringVar
import pyperclip

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

def convertir_color():
    color = combo_color.get()
    rgb = color_a_rgb(color)

    if rgb:
        lbl_rgb["text"] = f"RGB: {rgb}"
        hex_code = rgb_a_hex(rgb)
        lbl_hex["text"] = f"Hexadecimal: {hex_code}"
        pyperclip.copy(hex_code)
    else:
        lbl_rgb["text"] = f"No se encontró una representación en RGB para el color {color}."
        lbl_hex["text"] = ""

def actualizar_lista(*args):
    input = buscar_var.get()
    coincidencias = [color for color in colores_disponibles if input.lower() in color.lower()]
    if coincidencias:
        combo_color['values'] = coincidencias
        combo_color.set(coincidencias[0])

ventana = tk.Tk()
ventana.title("Conversor de Colores")
ventana.geometry("300x200")

lbl_titulo = tk.Label(ventana, text="Conversor de Colores", font=("Arial", 14))
lbl_titulo.pack(pady=10)

lbl_buscar = tk.Label(ventana, text="Buscar:")
lbl_buscar.pack()

buscar_var = StringVar()
buscar_var.trace("w", actualizar_lista)

entrada_buscar = tk.Entry(ventana, textvariable=buscar_var)
entrada_buscar.pack()

lbl_color = tk.Label(ventana, text="Color:")
lbl_color.pack()

colores_disponibles = list(colores.keys())

combo_color = ttk.Combobox(ventana, values=colores_disponibles)
combo_color.pack(pady=5)

btn_convertir = tk.Button(ventana, text="Convertir", command=convertir_color)
btn_convertir.pack(pady=5)

lbl_rgb = tk.Label(ventana, text="")
lbl_rgb.pack()

lbl_hex = tk.Label(ventana, text="")
lbl_hex.pack()

ventana.mainloop()
