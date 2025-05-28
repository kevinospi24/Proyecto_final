import tkinter as tk
from tkinter import messagebox
import pandas as pd
from logica import Analisis
#ventana principal
ventana = tk.Tk()
ventana.configure(bg="skyblue")
ventana.title("Registro de Usuarios")
ventana.geometry("400x600")

#tarifas
tarifas = {"spinning": 7000,"fisioterapia": 10000,"rumba": 5000,"fortalecimiento": 6500}

#funcion registrar usuario
def registrar():
    
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    actividad = actividad_entry.get()
    meses = meses_entry.get()
    clases = clases_entry.get()

    pago = int(clases) * tarifas.get(actividad.lower(), 0)

    nuevo = {"Nombre": nombre,"Edad": edad,"Actividad": actividad,"Meses": meses,"Pago": pago}

    try:
        df = pd.read_csv("usuarios.csv")
    except:
        df = pd.DataFrame(columns=["Nombre", "Edad", "Actividad", "Meses", "Pago"])

    df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
    df = df[["Nombre", "Edad", "Actividad", "Meses", "Pago"]]
    df.to_csv("usuarios.csv", index=False)

    messagebox.showinfo("Pago del Cliente", f"{nombre} debe pagar: ${pago}")

#fuincion mostrar usuarios
def mostrar():
    try:
        df = pd.read_csv("usuarios.csv")
        if df.empty:
            messagebox.showinfo("Usuarios", "No hay registros.")
        else:
            usuarios_texto = df.to_string(index=False)
            messagebox.showinfo("Usuarios Registrados", usuarios_texto)
    except:
        messagebox.showinfo("Usuarios", "No hay registros.")

#funcion modificar
def modificar():
    try:
        df = pd.read_csv("usuarios.csv")
    except:
        messagebox.showerror("Error", "No hay registros.")
        return

    nombre = nombre_entry.get()
    if nombre not in df["Nombre"].values:
        messagebox.showwarning("Modificar", f"{nombre} no existe en el archivo.")
        return

    idx = df[df["Nombre"] == nombre].index[0]
    df.loc[idx, ["Edad", "Actividad", "Meses"]] = [edad_entry.get(), actividad_entry.get(), meses_entry.get()]

    clases = int(clases_entry.get())
    pago = clases * tarifas.get(actividad_entry.get().lower(), 0)
    df.loc[idx, "Pago"] = pago

    df.to_csv("usuarios.csv", index=False)
    messagebox.showinfo("Modificar", f"{nombre} modificado.\nPago nuevo: ${pago}")

#funcion eliminar
def eliminar():
    try:
        df = pd.read_csv("usuarios.csv")
    except:
        messagebox.showerror("Error", "No hay registros.")
        return

    nombre = nombre_entry.get()
    if nombre not in df["Nombre"].values:
        messagebox.showwarning("Eliminar", f"{nombre} no existe en el archivo.")
        return

    df = df[df["Nombre"] != nombre]
    df.to_csv("usuarios.csv", index=False)
    messagebox.showinfo("Eliminar", f"Usuario {nombre} eliminado correctamente.")

#funcion generar reportes
def generar_reportes():
    try:
        analisis = Analisis("usuarios.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo de datos no existe.")
        return
    
    resumen = f"""
Total usuarios: {analisis.total_usuarios()}
Promedio pagos: {analisis.promedio_pagos():.2f}
Actividad más popular: {analisis.actividad_mas_popular()}
Usuario que más pagó: {analisis.usuario_que_mas_pago()['Nombre']} (${analisis.usuario_que_mas_pago()['Pago']})
"""
    messagebox.showinfo("Reporte General", resumen)
    analisis.grafico_barras()
    analisis.histograma_edades()
    analisis.grafico_circular()
  
#campos de entrada
tk.Label(ventana, text="Nombre:", bg="skyblue").pack(pady=5)
nombre_entry = tk.Entry(ventana)
nombre_entry.pack(pady=5)

tk.Label(ventana, text="Edad:", bg="skyblue").pack(pady=5)
edad_entry = tk.Entry(ventana)
edad_entry.pack(pady=5)

tk.Label(ventana, text="Actividad:", bg="skyblue").pack(pady=5)
actividad_entry = tk.Entry(ventana)
actividad_entry.pack(pady=5)

tk.Label(ventana, text="Meses:", bg="skyblue").pack(pady=5)
meses_entry = tk.Entry(ventana)
meses_entry.pack(pady=5)

tk.Label(ventana, text="Clases:", bg="skyblue").pack(pady=5)
clases_entry = tk.Entry(ventana)
clases_entry.pack(pady=5)

#botones
tk.Button(ventana, text="Registrar Usuario", width=30, command=registrar).pack(pady=5)
tk.Button(ventana, text="Mostrar Usuarios", width=30, command=mostrar).pack(pady=5)
tk.Button(ventana, text="Modificar Usuario", width=30, command=modificar).pack(pady=5)
tk.Button(ventana, text="Eliminar Usuario", width=30, command=eliminar).pack(pady=5)
tk.Button(ventana, text="Generar Reportes", width=30, command=generar_reportes).pack(pady=5)
tk.Button(ventana, text="Salir", width=30, command=quit).pack(pady=5)
# Ejecutar ventana
ventana.mainloop()
