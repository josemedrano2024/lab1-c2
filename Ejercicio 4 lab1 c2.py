import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class MascotasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Crear el layout principal
        layout = QVBoxLayout()

        # Crear widgets para 3 mascotas
        self.mascota1 = self.crear_formulario_mascota("Mascota 1")
        self.mascota2 = self.crear_formulario_mascota("Mascota 2")
        self.mascota3 = self.crear_formulario_mascota("Mascota 3")

        # Agregar los formularios al layout
        layout.addLayout(self.mascota1['layout'])
        layout.addLayout(self.mascota2['layout'])
        layout.addLayout(self.mascota3['layout'])

        # Botón para mostrar los datos ingresados
        boton = QPushButton("Mostrar datos", self)
        boton.clicked.connect(self.mostrar_datos)
        layout.addWidget(boton)

        self.setLayout(layout)
        self.setWindowTitle('Datos de 3 Mascotas')
        self.show()

    def crear_formulario_mascota(self, titulo):
        # Crear un formulario para una mascota
        layout = QVBoxLayout()
        layout.addWidget(QLabel(titulo))

        nombre_input = QLineEdit()
        nombre_input.setPlaceholderText("Nombre")
        layout.addWidget(nombre_input)

        edad_input = QLineEdit()
        edad_input.setPlaceholderText("Edad")
        layout.addWidget(edad_input)

        tipo_input = QLineEdit()
        tipo_input.setPlaceholderText("Tipo (ej. perro, gato)")
        layout.addWidget(tipo_input)

        return {'layout': layout, 'nombre': nombre_input, 'edad': edad_input, 'tipo': tipo_input}

    def mostrar_datos(self):
        # Obtener los datos de las 3 mascotas y mostrarlos en la consola
        mascotas = [self.mascota1, self.mascota2, self.mascota3]
        for i, mascota in enumerate(mascotas, start=1):
            nombre = mascota['nombre'].text()
            edad = mascota['edad'].text()
            tipo = mascota['tipo'].text()
            print(f"Mascota {i}:")
            print(f"  Nombre: {nombre}")
            print(f"  Edad: {edad}")
            print(f"  Tipo: {tipo}\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MascotasApp()
    sys.exit(app.exec_())
