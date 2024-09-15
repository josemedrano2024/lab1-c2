import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

class VentanaClave(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Ingreso de Clave Secreta")
        self.setGeometry(100, 100, 300, 150)

        # Layout vertical
        layout = QVBoxLayout()

        # Etiqueta
        self.etiqueta = QLabel("Ingresa tu clave secreta:")
        layout.addWidget(self.etiqueta)

        # Campo de entrada para la clave secreta (con estilo de contraseña)
        self.campo_clave = QLineEdit()
        self.campo_clave.setEchoMode(QLineEdit.Password)  # Ocultar caracteres
        layout.addWidget(self.campo_clave)

        # Botón para enviar la clave
        self.boton = QPushButton("Enviar")
        self.boton.clicked.connect(self.mostrar_clave)
        layout.addWidget(self.boton)

        # Establecer el layout en la ventana
        self.setLayout(layout)

    def mostrar_clave(self):
        # Obtener la clave ingresada
        clave = self.campo_clave.text()
        # Mostrar un mensaje con la clave (por motivos de demostración)
        QMessageBox.information(self, "Clave Ingresada", f"La clave ingresada es: {clave}")

# Crear la aplicación
app = QApplication(sys.argv)

# Crear y mostrar la ventana
ventana = VentanaClave()
ventana.show()

# Ejecutar la aplicación
sys.exit(app.exec_())
