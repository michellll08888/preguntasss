import tkinter as tk
from tkinter import messagebox

# --- Definición de Colores ---
COLOR_FONDO_VENTANA = "#81A4E6"
COLOR_FONDO_BOTON = "#2E549B"
COLOR_TEXTO_BOTON = "#000000"
COLOR_FONDO_FINAL = "#444487" 
COLOR_SELECCION_RADIO = "#5D8C80"
COLOR_FONDO_RESPUESTA = "#81A4E6" # Ajustado para que sea el mismo que el fondo de ventana para mejorar la legibilidad del texto negro
COLOR_TEXTO_RESPUESTA = "black"  # ¡NUEVO! Color de texto de respuesta en negro

# --- Estructura de Datos del Cuestionario (Sin Cambios) ---
preguntas = [
    {
        "pregunta": "¿Qué describe mejor la criptografía según el documento?",
        "opciones": {
            "A": "Un método para acelerar la transmisión de datos.",
            "B": "La práctica de desarrollar algoritmos codificados para proteger información.",
            "C": "Un sistema para reducir el tamaño de los archivos.",
            "D": "Un protocolo de comunicación inalámbrica."
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Cuál de los siguientes principios busca evitar que el remitente niegue haber enviado información?",
        "opciones": {
            "A": "Confidencialidad",
            "B": "Integridad",
            "C": "Autenticación",
            "D": "No repudio"
        },
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "En la criptografía simétrica, ¿qué característica la define?",
        "opciones": {
            "A": "Usa diferentes claves para cifrar y descifrar",
            "B": "Usa la misma clave para cifrar y descifrar la información",
            "C": "No requiere claves",
            "D": "Depende del uso de firmas digitales",
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Cuál es una ventaja destacada de la criptografía simétrica?",
        "opciones": {
            "A": "Es lenta pero más segura",
            "B": "Es rápida y eficiente para grandes volúmenes de datos",
            "C": "No necesita intercambio de claves",
            "D": "No requiere recursos computacionales"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Qué tipo de criptografía utiliza un par de claves relacionadas matemáticamente (una pública y una privada)?",
        "opciones": {
            "A": "Criptografía simétrica",
            "B": "Criptografía asimétrica",
            "C": "Criptografía híbrida",
            "D": "Criptografía cuántica"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Cuál de los siguientes algoritmos es un ejemplo de criptografía asimétrica?",
        "opciones": {
            "A": "AES",
            "B": "RSA",
            "C": "SHA-256",
            "D": "HMAC"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Qué ventaja tiene la criptografía por hardware en comparación con la de software?",
        "opciones": {
            "A": "Permite mayor flexibilidad de actualización",
            "B": "Es más económica de implementar",
            "C": "Proporciona seguridad física y mejor rendimiento",
            "D": "No requiere dispositivos adicionales"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿Cuál es la función principal de una firma digital según el documento?",
        "opciones": {
            "A": "Comprimir los datos cifrados",
            "B": "Garantizar integridad, autenticidad y no repudio",
            "C": "Aumentar la velocidad del cifrado",
            "D": "Reemplazar las claves públicas"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Qué ventaja ofrece la criptografía de curva elíptica (ECC)?",
        "opciones": {
            "A": "Permite la transmisión sin cifrado",
            "B": "Requiere claves más grandes para mantener la seguridad",
            "C": "Ofrece el mismo nivel de protección con claves más pequeñas",
            "D": "Solo funciona en entornos financieros"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿Qué objetivo tiene la criptografía poscuántica (PQC) mencionada en el documento?",
        "opciones": {
            "A": "Sustituir la criptografía en riesgo ante computadoras cuánticas",
            "B": "Reducir los costos del hardware criptográfico",
            "C": "Eliminar el uso de claves pública",
            "D": "Mejorar la estética del código fuente"
        },
        "respuesta_correcta": "A"
    },
]

class CuestionarioApp:
    def __init__(self, master):
        self.master = master
        master.title("Cuestionario de Criptografía 🔐")
        master.geometry("600x400")
        
        master.config(bg=COLOR_FONDO_VENTANA)
        
        self.puntuacion = 0
        self.pregunta_actual_idx = 0
        self.preguntas_data = preguntas
        
        self.respuesta_seleccionada = tk.StringVar() 
        self.respuesta_seleccionada.set(None)
        
        self.label_pregunta = tk.Label(master, 
                                       text="", 
                                       wraplength=550, 
                                       justify=tk.LEFT, 
                                       font=("Arial", 12, "bold"),
                                       bg=COLOR_FONDO_VENTANA)
        self.label_pregunta.pack(pady=20)
        
        self.opciones_frame = tk.Frame(master, bg=COLOR_FONDO_VENTANA)
        self.opciones_frame.pack(pady=10)
        
        self.boton_siguiente = tk.Button(master, 
                                         text="Siguiente Pregunta", 
                                         command=self.verificar_y_cargar_siguiente,
                                         bg=COLOR_FONDO_BOTON,
                                         fg=COLOR_TEXTO_BOTON)
        self.boton_siguiente.pack(pady=30)
        
        self.cargar_pregunta()

    def cargar_pregunta(self):
        """Carga la pregunta y opciones. Se encarga de limpiar el frame anterior."""
        for widget in self.opciones_frame.winfo_children():
            widget.destroy()

        if self.pregunta_actual_idx >= len(self.preguntas_data):
            self.mostrar_resultado_final()
            return
        
        pregunta_info = self.preguntas_data[self.pregunta_actual_idx]
        numero_pregunta = self.pregunta_actual_idx + 1
        self.label_pregunta.config(text=f"Pregunta {numero_pregunta}/{len(self.preguntas_data)}:\n{pregunta_info['pregunta']}")
        
        self.respuesta_seleccionada.set(None) 

        # Crea los nuevos RadioButtons
        for clave, texto_opcion in pregunta_info['opciones'].items():
            rb = tk.Radiobutton(self.opciones_frame, 
                                text=f"{clave}) {texto_opcion}", 
                                variable=self.respuesta_seleccionada, 
                                value=clave,
                                justify=tk.LEFT,
                                anchor="w", 
                                font=("Arial", 10),
                                bg=COLOR_FONDO_RESPUESTA,         # Fondo ajustado para contraste (es igual que el de la ventana)
                                fg=COLOR_TEXTO_RESPUESTA,         # ¡Color del texto en negro!
                                activebackground=COLOR_FONDO_RESPUESTA, 
                                selectcolor=COLOR_SELECCION_RADIO)
            rb.pack(anchor="w", padx=5, pady=5, fill='x')
            
        if self.pregunta_actual_idx == len(self.preguntas_data) - 1:
            self.boton_siguiente.config(text="Finalizar Cuestionario")
        else:
            self.boton_siguiente.config(text="Siguiente Pregunta")


    def verificar_y_cargar_siguiente(self):
        """Verifica la respuesta, actualiza la puntuación y avanza."""
        respuesta = self.respuesta_seleccionada.get()
        
        if respuesta == "None":
            messagebox.showwarning("Advertencia", "Por favor, selecciona una opción antes de continuar.")
            return

        pregunta_info = self.preguntas_data[self.pregunta_actual_idx]
        if respuesta == pregunta_info['respuesta_correcta']:
            self.puntuacion += 1
        
        self.pregunta_actual_idx += 1
        self.cargar_pregunta()


    def mostrar_resultado_final(self):
        """Muestra el resultado final usando una ventana Toplevel para aplicar el color."""
        self.master.withdraw() 
        
        ventana_resultado = tk.Toplevel(self.master)
        ventana_resultado.title("Resultados")
        ventana_resultado.geometry("400x200")
        
        ventana_resultado.config(bg=COLOR_FONDO_FINAL)
        
        def cerrar_todo():
            ventana_resultado.destroy()
            self.master.destroy()

        # Etiqueta de título
        tk.Label(ventana_resultado, 
                 text="¡Cuestionario Terminado! 🎉", 
                 font=("Arial", 18, "bold"),
                 bg=COLOR_FONDO_FINAL,
                 fg="white").pack(pady=(20, 10))

        # Etiqueta de puntuación
        mensaje = f"Tu puntuación final es: {self.puntuacion} de {len(self.preguntas_data)}."
        tk.Label(ventana_resultado, 
                 text=mensaje, 
                 font=("Arial", 14),
                 bg=COLOR_FONDO_FINAL,
                 fg="white").pack(pady=10)
        
        # Botón para cerrar
        tk.Button(ventana_resultado, 
                  text="Cerrar", 
                  command=cerrar_todo,
                  bg=COLOR_FONDO_BOTON,
                  fg="white").pack(pady=10)

        ventana_resultado.transient(self.master)
        ventana_resultado.grab_set()
        self.master.wait_window(ventana_resultado)

# --- Bloque principal para iniciar la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CuestionarioApp(root)
    root.mainloop()