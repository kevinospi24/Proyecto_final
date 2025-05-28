import pandas as pd
import matplotlib.pyplot as plt

class Analisis:
    def __init__(self, usuarios):
        try:
            self.df = pd.read_csv(usuarios)
        except FileNotFoundError:
            print("Archivo no encontrado.")
            self.df = pd.DataFrame(columns=["Nombre", "Edad", "Actividad", "Meses", "Pago"])

    def total_usuarios(self):
        return len(self.df)

    def usuarios_incompletos(self):
        incompletos = self.df[self.df.isnull().any(axis=1)]
        return incompletos

    def promedio_pagos(self):
        if self.df.empty:
            return 0
        return self.df['Pago'].mean()

    def actividad_mas_popular(self):
        if self.df.empty:
            return None
        return self.df['Actividad'].value_counts().idxmax()

    def usuario_que_mas_pago(self):
        if self.df.empty:
            return None
        return self.df.loc[self.df['Pago'].idxmax()]

    def grafico_barras(self):
        if self.df.empty:
            print("No hay datos para graficar.")
            return
        self.df['Actividad'].value_counts().plot(kind='bar', color='skyblue')
        plt.title('Usuarios por actividad')
        plt.xlabel('Actividad')
        plt.ylabel('Cantidad de usuarios')
        plt.tight_layout()
        plt.show()

    def histograma_edades(self):
        if self.df.empty:
            print("No hay datos para graficar.")
            return
        self.df['Edad'].plot(kind='hist', bins=10, color='lightgreen', edgecolor='black')
        plt.title('Distribución de edades')
        plt.xlabel('Edad')
        plt.tight_layout()
        plt.show()

    def grafico_circular(self):
        if self.df.empty:
            print("No hay datos para graficar.")
            return
        self.df['Actividad'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
        plt.title('Distribución de inscripciones por Actividad')
        plt.ylabel('')
        plt.tight_layout()
        plt.show()
