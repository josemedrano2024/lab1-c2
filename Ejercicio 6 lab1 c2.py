import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QMessageBox

class VentanaEjercicio(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Seleccionar Fruta")
        self.setGeometry(100, 100, 300, 200)

        # Layout vertical
        layout = QVBoxLayout()

        # Etiqueta para seleccionar género
        self.etiqueta_genero = QLabel("Selecciona tu género:")
        layout.addWidget(self.etiqueta_genero)

        # Radio Buttons para seleccionar género
        self.radio_masculino = QRadioButton("Masculino")
        self.radio_femenino = QRadioButton("Femenino")
        layout.addWidget(self.radio_masculino)
        layout.addWidget(self.radio_femenino)

        # Etiqueta para seleccionar fruta
        self.etiqueta_fruta = QLabel("Selecciona una fruta:")
        layout.addWidget(self.etiqueta_fruta)

        # ComboBox para seleccionar fruta
        self.combo_fruta = QComboBox()
        self.combo_fruta.addItems(["Manzana", "Banana", "Naranja", "Fresa"])
        layout.addWidget(self.combo_fruta)

        # Etiqueta para seleccionar cantidad
        self.etiqueta_cantidad = QLabel("Selecciona la cantidad:")
        layout.addWidget(self.etiqueta_cantidad)

        # SpinBox para seleccionar cantidad
        self.spin_cantidad = QSpinBox()
        self.spin_cantidad.setRange(1, 100)  # Rango de 1 a 100
        layout.addWidget(self.spin_cantidad)

        # Botón para enviar la información
        self.boton = QPushButton("Enviar")
        self.boton.clicked.connect(self.mostrar_resumen)
        layout.addWidget(self.boton)

        # Establecer el layout en la ventana
        self.setLayout(layout)

    def mostrar_resumen(self):
        # Obtener las selecciones del usuario
        genero = "Masculino" if self.radio_masculino.isChecked() else "Femenino" if self.radio_femenino.isChecked() else "No especificado"
        fruta = self.combo_fruta.currentText()
        cantidad = self.spin_cantidad.value()

        # Mostrar un mensaje con el resumen de las selecciones
        mensaje = f"Género: {genero}\nFruta: {fruta}\nCantidad: {cantidad}"
        QMessageBox.information(self, "Resumen de Selección", mensaje)

# Crear la aplicación
app = QApplication(sys.argv)

# Crear y mostrar la ventana
ventana = VentanaEjercicio()
ventana.show()

# Ejecutar la aplicación
sys.exit(app.exec_())

#Problema que resuelve
#Este programa permite a los usuarios seleccionar su género, elegir una fruta de una lista y especificar una cantidad. 
# Es útil en situaciones donde se necesita recopilar información de manera estructurada y fácil de entender. 
# Por ejemplo, podría ser utilizado en:
#Encuestas: Para recopilar datos demográficos y preferencias de los encuestados.
#Aplicaciones de pedidos: Donde los usuarios deben seleccionar productos y cantidades antes de realizar un pedido.
#Formularios: Para obtener información básica de los usuarios antes de continuar con un proceso más complejo.