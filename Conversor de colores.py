import tkinter as tk
from tkinter import ttk

def color_a_rgb(color):
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
        "negro": (0, 0, 0)
        # Agrega más colores y variantes según tus necesidades
    }

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
    else:
        lbl_rgb["text"] = f"No se encontró una representación en RGB para el color {color}."
        lbl_hex["text"] = ""

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Colores")
ventana.geometry("300x200")

# Crear los componentes de la GUI
lbl_titulo = tk.Label(ventana, text="Conversor de Colores", font=("Arial", 14))
lbl_titulo.pack(pady=10)

lbl_color = tk.Label(ventana, text="Color:")
lbl_color.pack()

colores_disponibles = ["rojo", "rojo claro", "rojo oscuro", "verde", "verde claro", "verde oscuro",
                       "azul", "azul claro", "azul oscuro", "amarillo", "amarillo claro", "amarillo oscuro",
                       "morado", "morado claro", "morado oscuro", "naranja", "naranja claro", "naranja oscuro",
                       "rosa", "rosa claro", "rosa oscuro", "blanco", "negro"]

combo_color = ttk.Combobox(ventana, values=colores_disponibles)
combo_color.pack(pady=5)

btn_convertir = tk.Button(ventana, text="Convertir", command=convertir_color)
btn_convertir.pack(pady=5)

lbl_rgb = tk.Label(ventana, text="")
lbl_rgb.pack()

lbl_hex = tk.Label(ventana, text="")
lbl_hex.pack()

# Ejecutar la aplicación
ventana.mainloop()
