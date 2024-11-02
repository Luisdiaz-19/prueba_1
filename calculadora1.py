#luis jose diaz urieles
#31/10/2024
#grupo 2 semestre 5

import tkinter as tk

def calcular(operacion):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operacion == 'suma':
            resultado.set(num1 + num2)
        elif operacion == 'resta':
            resultado.set(num1 - num2)
        elif operacion == 'multiplicacion':
            resultado.set(num1 * num2)
        elif operacion == 'division':
            if num2 != 0:
                resultado.set(num1 / num2)
            else:
                resultado.set("No se puede dividir por cero")
    except ValueError:
        resultado.set("Error")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x200")  # Ajusta el tamaño de la ventana (ancho x alto)

tk.Label(root, text="Primer número:").grid(row=0, column=0)
tk.Label(root, text="Segundo número:").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

# Asignación de botones a la función calcular con el tipo de operación
tk.Button(root, text="+", command=lambda: calcular('suma')).grid(row=2, column=0)
tk.Button(root, text="-", command=lambda: calcular('resta')).grid(row=2, column=1)
tk.Button(root, text="*", command=lambda: calcular('multiplicacion')).grid(row=3, column=0)
tk.Button(root, text="/", command=lambda: calcular('division')).grid(row=3, column=1)

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado).grid(row=4, column=0, columnspan=2)

root.mainloop()


