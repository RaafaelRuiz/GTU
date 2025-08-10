import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Crear ventana
ventana = tk.Tk()
ventana.title("Gráfica Frame")
ventana.geometry("600x500")

# Entradas y etiquetas
tk.Label(ventana, text="Valor X:").place(x=30, y=30)
entrada_x = tk.Entry(ventana)
entrada_x.place(x=100, y=30)

tk.Label(ventana, text="Valor Y:").place(x=30, y=70)
entrada_y = tk.Entry(ventana)
entrada_y.place(x=100, y=70)

# Resultado
resultado_label = tk.Label(ventana, text="Resultado: ")
resultado_label.place(x=400, y=100)

# Frame para la gráfica
ancho_px = 400
alto_px = 300
frame_grafica = tk.Frame(ventana, width=ancho_px, height=alto_px, bg="white")
frame_grafica.place(x=100, y=140)

# Función para graficar
def graficar():
    try:
        x = float(entrada_x.get())
        y = float(entrada_y.get())
        x = float(entrada_x2.get())
        y = float(entrada_y2.get())

        # Limpiar gráfica anterior
        for widget in frame_grafica.winfo_children():
            widget.destroy()

        # Convertir tamaño del frame de píxeles a pulgadas
        dpi = 100
        ancho_pulg = ancho_px / dpi
        alto_pulg = alto_px / dpi

        # Crear figura
        fig = plt.figure(figsize=(ancho_pulg, alto_pulg), dpi=dpi)
        plt.plot([0, x], [0, y], marker='o')
        plt.title("Punto ingresado")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")

        # Mostrar figura en Frame
        canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=0, width=ancho_px, height=alto_px)

    except ValueError:
        resultado_label.config(text="Ingresa solo números.")

# Funciones matemáticas
def sumar():
    try:
        x = float(entrada_x.get())
        y = float(entrada_y.get())
        resultado = x + y
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Ingresa solo números.")

def restar():
    try:
        x = float(entrada_x.get())
        y = float(entrada_y.get())
        resultado = x - y
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Ingresa solo números.")

def multiplicar():
    try:
        x = float(entrada_x.get())
        y = float(entrada_y.get())
        resultado = x * y
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Ingresa solo números.")

# Botones
tk.Button(ventana, text="Graficar", command=graficar).place(x=290, y=100)
tk.Button(ventana, text="Restar", command=restar).place(x=230, y=100)
tk.Button(ventana, text="Multiplicar", command=multiplicar).place(x=150, y=100)
tk.Button(ventana, text="Sumar", command=sumar).place(x=90, y=100)

ventana.mainloop()

