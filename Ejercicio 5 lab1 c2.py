import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class PersonaForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Datos de una Persona")

        # Crear etiquetas y campos de entrada para los 10 datos
        self.labels = ["Nombre", "Apellido", "Edad", "Género", "Dirección", "Ciudad", "País", "Teléfono", "Correo Electrónico", "Ocupación"]
        self.inputs = [QLineEdit(self) for _ in range(10)]

        # Crear un botón para enviar los datos
        self.submit_button = QPushButton("Enviar", self)
        self.submit_button.clicked.connect(self.mostrar_datos)

        # Layout para organizar los widgets verticalmente
        layout = QVBoxLayout()

        # Agregar etiquetas y campos al layout
        for label, input_field in zip(self.labels, self.inputs):
            layout.addWidget(QLabel(label))
            layout.addWidget(input_field)

        # Agregar el botón al layout
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def mostrar_datos(self):
        # Obtener los datos ingresados y mostrarlos en la consola
        datos = [input_field.text() for input_field in self.inputs]
        for label, dato in zip(self.labels, datos):
            print(f"{label}: {dato}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PersonaForm()
    ventana.show()
    sys.exit(app.exec_())
