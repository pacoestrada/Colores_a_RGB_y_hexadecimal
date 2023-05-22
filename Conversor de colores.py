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

def convertir_color():
    color = combo_color.get()
    rgb = color_a_rgb(color)

    if rgb:
        lbl_rgb["text"] = f"RGB: {rgb}"
        hex_code = rgb_a_hex(rgb)
        lbl_hex["text"] = f"Hexadecimal: {hex_code}"
        copiar_al_portapapeles(hex_code)
    else:
        lbl_rgb["text"] = f"No se encontró una representación en RGB para el color {color}."
        lbl_hex["text"] = ""

def copiar_al_portapapeles(texto):
    pyperclip.copy(texto)

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

btn_copiar = tk.Button(ventana, text="Copiar al portapapeles", command=lambda: copiar_al_portapapeles(lbl_hex.cget("text")))
btn_copiar.pack(pady=5)

lbl_rgb = tk.Label(ventana, text="")
lbl_rgb.pack()

lbl_hex = tk.Label(ventana, text="")
lbl_hex.pack()

ventana.mainloop()
