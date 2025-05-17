import tkinter as tk
from tkinter import ttk  # Importamos ttk para widgets temáticos
from tkinter import messagebox  # Importamos messagebox para mensajes
# Importamos scrolledtext para un área de texto con scroll
from tkinter import scrolledtext


class IrrigationOptimizerApp:
    def __init__(self, root):
        # Ventana principal de la aplicación
        self.root = root
        # Título de la ventana
        self.root.title("Optimizador de Riego por Tipo de Suelo")

        # --- Variables para almacenar los inputs y resultados ---
        # Variable para almacenar el tipo de suelo seleccionado
        self.soil_type_var = tk.StringVar()
        # Variable para mostrar las recomendaciones (será un área de texto)
        self.recommendations_text_widget = None  # Usaremos un widget Text para esto

        # --- Notebook para las pestañas ---
        # Creamos un widget Notebook para organizar la interfaz en pestañas
        self.notebook = ttk.Notebook(root)
        # Empaquetamos el notebook para que se expanda y llene la ventana
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")

        # --- Pestaña de Recomendaciones de Riego ---
        # Creamos un Frame para la primera pestaña
        self.recommendations_frame = ttk.Frame(self.notebook, padding="10")
        # Añadimos este Frame al notebook con el texto de la pestaña
        self.notebook.add(self.recommendations_frame,
                          text='Recomendaciones de Riego')

        # Configuramos la columna 0 de este frame para que se expanda
        self.recommendations_frame.columnconfigure(0, weight=1)
        # Configuramos la fila 1 para que el área de texto de recomendaciones se expanda
        self.recommendations_frame.rowconfigure(1, weight=1)

        # --- Sección de Selección de Tipo de Suelo ---
        # Creamos un LabelFrame para agrupar la selección del suelo
        soil_selection_frame = ttk.LabelFrame(
            self.recommendations_frame, text="Seleccionar Tipo de Suelo", padding="10")
        # Posicionamos este LabelFrame en la fila 0, columna 0 de la pestaña de recomendaciones
        soil_selection_frame.grid(
            row=0, column=0, sticky=(tk.W, tk.E), pady=5, padx=5)
        # Configuramos la columna 1 de este frame para que el combobox se expanda
        soil_selection_frame.columnconfigure(1, weight=1)

        # Etiqueta para el Combobox
        ttk.Label(soil_selection_frame, text="Tipo de Suelo:").grid(
            row=0, column=0, sticky=tk.W, padx=5, pady=5)

        # Lista de tipos de suelo comunes (puedes añadir o modificar esta lista)
        soil_types = ["Arenoso", "Franco Arenoso",
                      "Franco", "Franco Arcilloso", "Arcilloso"]

        # Creamos el Combobox (menú desplegable) para seleccionar el tipo de suelo
        # state="readonly" evita que el usuario escriba en el campo, forzando la selección de la lista
        soil_type_combobox = ttk.Combobox(
            soil_selection_frame, textvariable=self.soil_type_var, values=soil_types, state="readonly")
        soil_type_combobox.grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        # Seleccionamos el primer elemento de la lista por defecto
        soil_type_combobox.current(0)

        # Vinculamos una función al evento de selección del combobox
        # Cuando el usuario seleccione un tipo de suelo, se llamará a self.display_recommendations
        soil_type_combobox.bind("<<ComboboxSelected>>",
                                self.display_recommendations)

        # --- Área para mostrar las Recomendaciones ---
        # Creamos un LabelFrame para el área de texto de recomendaciones
        recommendations_output_frame = ttk.LabelFrame(
            self.recommendations_frame, text="Recomendaciones de Riego", padding="10")
        # Posicionamos este LabelFrame debajo de la selección de suelo
        recommendations_output_frame.grid(
            row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5, padx=5)
        # Configuramos este frame para que su contenido (el Text widget) se expanda
        recommendations_output_frame.columnconfigure(0, weight=1)
        recommendations_output_frame.rowconfigure(0, weight=1)

        # Creamos un widget ScrolledText para mostrar las recomendaciones.
        # ScrolledText es un Text widget con barras de desplazamiento automáticas.
        # wrap="word" hace que el texto se ajuste a la anchura del widget.
        # state="disabled" hace que el usuario no pueda editar el texto.
        self.recommendations_text_widget = scrolledtext.ScrolledText(
            recommendations_output_frame, wrap="word", state="disabled", padx=5, pady=5)
        # Empaquetamos el ScrolledText widget para que llene el recommendations_output_frame
        self.recommendations_text_widget.pack(expand=True, fill="both")

        # Mostramos la recomendación inicial para el suelo seleccionado por defecto
        self.display_recommendations()

        # --- Pestaña de Información ---
        # Creamos un Frame para la segunda pestaña
        self.info_frame = ttk.Frame(self.notebook, padding="10")
        # Añadimos este Frame al notebook con el texto de la pestaña
        self.notebook.add(self.info_frame, text='Información')

        # Configuramos este frame para que su contenido se expanda
        self.info_frame.columnconfigure(0, weight=1)
        self.info_frame.rowconfigure(0, weight=1)

        # --- Contenido de la Pestaña de Información ---
        info_content = """
        **Optimizador de Riego por Tipo de Suelo**

        Esta aplicación proporciona recomendaciones básicas para optimizar el riego de tus cultivos basándose en el tipo de suelo predominante en tu parcela.

        **Importancia del Tipo de Suelo en el Riego:**

        El tipo de suelo influye enormemente en cómo el agua se mueve y se retiene en el perfil.
        * **Suelos Arenosos:** Tienen partículas grandes, poros grandes, drenan rápido y retienen poca agua disponible para las plantas. Requieren riegos más frecuentes pero de menor volumen.
        * **Suelos Arcillosos:** Tienen partículas pequeñas, poros pequeños, drenan lento y retienen mucha agua, pero una parte importante no está fácilmente disponible para las plantas. Son propensos al encharcamiento y la compactación si se riega en exceso. Requieren riegos menos frecuentes pero de mayor volumen (aplicado lentamente).
        * **Suelos Francos:** Son una mezcla equilibrada de arena, limo y arcilla, considerados ideales para la agricultura. Tienen buena aireación, drenaje y capacidad de retención de agua.

        **Cómo usar la aplicación:**

        1.  Ve a la pestaña "Recomendaciones de Riego".
        2.  Selecciona el tipo de suelo de tu parcela en el menú desplegable.
        3.  Lee la recomendación básica que aparece en el área de texto de abajo.

        *Nota: Estas son recomendaciones generales. La optimización real del riego también depende de factores como el cultivo, la etapa de desarrollo, las condiciones climáticas (evapotranspiración), la topografía y el sistema de riego utilizado.*

        ---
        Desarrollado por By LuisFarming.
        """

        # Creamos un widget ScrolledText para el contenido de información.
        # Usamos ScrolledText para que tenga barras de desplazamiento si el contenido es largo.
        self.info_text_widget = scrolledtext.ScrolledText(
            self.info_frame, wrap="word", state="disabled", padx=10, pady=10)
        self.info_text_widget.grid(
            row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Insertar el contenido en el widget de texto de información
        # Habilitar temporalmente para insertar
        self.info_text_widget.config(state="normal")
        self.info_text_widget.insert(tk.END, info_content)
        # Deshabilitar nuevamente para hacerlo de solo lectura
        self.info_text_widget.config(state="disabled")

    def display_recommendations(self, event=None):
        """Muestra las recomendaciones de riego basadas en el tipo de suelo seleccionado."""
        selected_soil = self.soil_type_var.get()

        # Diccionario con recomendaciones básicas por tipo de suelo
        # Puedes ampliar o detallar estas recomendaciones
        recommendations = {
            "Arenoso": "Suelos arenosos drenan rápido. Requieren riegos más frecuentes pero de menor volumen. Considera sistemas de riego que apliquen agua lentamente (goteo, microaspersión) para reducir pérdidas por percolación profunda.",
            "Franco Arenoso": "Buena aireación y drenaje. Riegos moderados, ajustando frecuencia según clima. Monitorea la humedad del suelo para regar cuando sea necesario.",
            "Franco": "Suelo ideal con buen equilibrio. Riegos moderados y uniformes, menos frecuentes que en arenosos. La mayoría de los sistemas de riego funcionan bien, pero la eficiencia es clave.",
            "Franco Arcilloso": "Retiene más agua que los francos. Riegos menos frecuentes pero de mayor volumen. Evitar encharcamiento. Permite que el suelo se seque ligeramente entre riegos para mejorar la aireación.",
            "Arcilloso": "Retiene mucha agua pero drena lento. Riegos poco frecuentes y de bajo volumen para evitar compactación y encharcamiento. Es mejor regar en varios pulsos cortos para permitir que el agua se infiltre lentamente. Evita el tráfico pesado sobre el suelo húmedo.",
        }

        # Obtener la recomendación para el suelo seleccionado
        recommendation = recommendations.get(
            selected_soil, "Seleccione un tipo de suelo para ver recomendaciones.")

        # Actualizar el área de texto de recomendaciones
        # Habilitar temporalmente para editar
        self.recommendations_text_widget.config(state="normal")
        self.recommendations_text_widget.delete(
            1.0, tk.END)  # Borrar contenido anterior
        self.recommendations_text_widget.insert(
            tk.END, recommendation)  # Insertar nueva recomendación
        # Deshabilitar nuevamente para hacerlo de solo lectura
        self.recommendations_text_widget.config(state="disabled")


# --- Parte principal del script ---
# Esto se ejecuta solo cuando corres el archivo directamente
if __name__ == "__main__":
    # Creamos la ventana principal de Tkinter
    root = tk.Tk()
    # Creamos una instancia de nuestra clase de aplicación
    app = IrrigationOptimizerApp(root)
    # Iniciamos el bucle principal de Tkinter
    root.mainloop()
