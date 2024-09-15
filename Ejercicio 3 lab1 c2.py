import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Lectura de Cédula y Nombre Completo")
        self.setGeometry(100, 100, 300, 200)

        # Etiquetas y campos de entrada
        self.label_cedula = QLabel("Número de Cédula:")
        self.campo_cedula = QLineEdit()

        self.label_nombre = QLabel("Nombre Completo:")
        self.campo_nombre = QLineEdit()

        # Botón para leer datos
        self.boton_leer = QPushButton("Leer Datos")
        self.boton_leer.clicked.connect(self.leer_datos)

        # Diseño de la ventana
        layout = QVBoxLayout()
        layout.addWidget(self.label_cedula)
        layout.addWidget(self.campo_cedula)
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.campo_nombre)
        layout.addWidget(self.boton_leer)

        self.setLayout(layout)

    def leer_datos(self):
        cedula = self.campo_cedula.text()
        nombre = self.campo_nombre.text()

        if cedula and nombre:
            # Mostrar los datos en un cuadro de mensaje
            QMessageBox.information(self, "Datos Leídos", f"Cédula: {cedula}\nNombre: {nombre}")
        else:
            # Mostrar error si faltan campos
            QMessageBox.warning(self, "Error", "Por favor ingrese ambos campos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
