import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

# Define tu nombre completo y edad
nombre_completo = "Jose Isaac Medrano Ventura"  # Cambia esto por tu nombre
edad = "19"                        # Cambia esto por tu edad

# Crear una aplicación
app = QApplication(sys.argv)

# Crear una ventana
ventana = QWidget()
ventana.setWindowTitle("Información Personal")
ventana.setGeometry(100, 100, 300, 200)  # x, y, ancho, alto

# Crear un layout vertical
layout = QVBoxLayout()

# Crear etiquetas para mostrar el nombre y la edad
etiqueta_nombre = QLabel(nombre_completo)
etiqueta_edad = QLabel(edad)

# Centrar las etiquetas
etiqueta_nombre.setAlignment(Qt.AlignCenter)
etiqueta_edad.setAlignment(Qt.AlignCenter)

# Agregar etiquetas al layout
layout.addWidget(etiqueta_nombre)
layout.addWidget(etiqueta_edad)

# Establecer el layout en la ventana
ventana.setLayout(layout)

# Mostrar la ventana
ventana.show()

# Ejecutar la aplicación
sys.exit(app.exec_())
