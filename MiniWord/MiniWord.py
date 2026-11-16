from PySide6.QtWidgets import (QApplication, QDockWidget, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QTextEdit, QToolBar,
                               QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QColorDialog, QFontDialog)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Word")
        self.resize(800, 600)
        self.archivo_actual = None

        barra_menu = self.menuBar()
        menu_archivo = barra_menu.addMenu("Archivo")
        menu_editar = barra_menu.addMenu("Editar")
        menu_formato = barra_menu.addMenu("Formato")

        self.editor = QTextEdit()

        contenedor = QWidget()
        layout_editor = QHBoxLayout(contenedor)
        layout_editor.addStretch(1)
        layout_editor.addWidget(self.editor, 3)
        layout_editor.addStretch(1)
        self.setCentralWidget(contenedor)

        self.etiqueta_palabras = QLabel("Palabras: 0")
        self.statusBar().addPermanentWidget(self.etiqueta_palabras)
        self.editor.textChanged.connect(self.contar_palabras)

        accion_nuevo = QAction("Nuevo", self)
        accion_nuevo.setShortcut("Ctrl+N")
        menu_archivo.addAction(accion_nuevo)
        accion_nuevo.triggered.connect(self.nuevo)

        accion_abrir = QAction("Abrir", self)
        accion_abrir.setShortcut("Ctrl+O")
        menu_archivo.addAction(accion_abrir)
        accion_abrir.triggered.connect(self.abrir)

        accion_guardar = QAction("Guardar", self)
        accion_guardar.setShortcut("Ctrl+S")
        menu_archivo.addAction(accion_guardar)
        accion_guardar.triggered.connect(self.guardar)

        accion_salir = QAction("Salir", self)
        accion_salir.setShortcut("Ctrl+Q")
        menu_archivo.addAction(accion_salir)
        accion_salir.triggered.connect(self.close)

        accion_deshacer = QAction("Deshacer", self)
        accion_deshacer.setShortcut("Ctrl+Z")
        menu_editar.addAction(accion_deshacer)
        accion_deshacer.triggered.connect(self.editor.undo)

        accion_rehacer = QAction("Rehacer", self)
        accion_rehacer.setShortcut("Ctrl+Y")
        menu_editar.addAction(accion_rehacer)
        accion_rehacer.triggered.connect(self.editor.redo)

        accion_cortar = QAction("Cortar", self)
        accion_cortar.setShortcut("Ctrl+X")
        menu_editar.addAction(accion_cortar)
        accion_cortar.triggered.connect(self.editor.cut)

        accion_copiar = QAction("Copiar", self)
        accion_copiar.setShortcut("Ctrl+C")
        menu_editar.addAction(accion_copiar)
        accion_copiar.triggered.connect(self.editor.copy)

        accion_pegar = QAction("Pegar", self)
        accion_pegar.setShortcut("Ctrl+V")
        menu_editar.addAction(accion_pegar)
        accion_pegar.triggered.connect(self.editor.paste)

        accion_buscar = QAction("Buscar", self)
        accion_buscar.setShortcut("Ctrl+F")
        accion_buscar.triggered.connect(self.mostrar_dock)

        accion_reemplazar = QAction("Reemplazar", self)
        accion_reemplazar.setShortcut("Ctrl+H")
        accion_reemplazar.triggered.connect(self.mostrar_dock)

        accion_fuente = QAction("Tipo de letra", self)
        menu_formato.addAction(accion_fuente)
        accion_fuente.triggered.connect(self.cambiar_fuente)

        accion_color = QAction("Color de fondo", self)
        menu_formato.addAction(accion_color)
        accion_color.triggered.connect(self.cambiar_color)

        barra = QToolBar("Herramientas")
        self.addToolBar(barra)
        barra.addAction(accion_nuevo)
        barra.addAction(accion_abrir)
        barra.addAction(accion_guardar)
        barra.addSeparator()
        barra.addAction(accion_deshacer)
        barra.addAction(accion_rehacer)
        barra.addSeparator()
        barra.addAction(accion_cortar)
        barra.addAction(accion_copiar)
        barra.addAction(accion_pegar)
        barra.addSeparator()
        barra.addAction(accion_buscar)
        barra.addAction(accion_reemplazar)

        self.campo_buscar = QLineEdit()
        self.campo_buscar.setPlaceholderText("Texto a buscar")
        self.campo_buscar.returnPressed.connect(self.buscar)
        boton_buscar = QPushButton("Buscar siguiente")
        boton_buscar.clicked.connect(self.buscar)

        self.campo_reemplazar = QLineEdit()
        self.campo_reemplazar.setPlaceholderText("Reemplazar por")
        boton_reemplazar = QPushButton("Reemplazar")
        boton_reemplazar.clicked.connect(self.reemplazar)

        contenido = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.campo_buscar)
        layout.addWidget(self.campo_reemplazar)
        layout.addWidget(boton_buscar)
        layout.addWidget(boton_reemplazar)
        layout.addStretch()
        contenido.setLayout(layout)

        self.dock = QDockWidget("Buscar y Reemplazar", self)
        self.dock.setWidget(contenido)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dock)

    def contar_palabras(self):
        texto = self.editor.toPlainText()
        palabras = texto.split()
        self.etiqueta_palabras.setText("Palabras: " + str(len(palabras)))

    def nuevo(self):
        self.editor.clear()
        self.archivo_actual = None
        self.statusBar().showMessage("Documento nuevo")

    def abrir(self):
        ruta, filtro = QFileDialog.getOpenFileName(self, "Abrir")
        if ruta == "":
            return
        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
        self.editor.setPlainText(texto)
        self.archivo_actual = ruta
        self.statusBar().showMessage("Archivo abierto con éxito")

    def guardar(self):
        if self.archivo_actual is None:
            ruta, filtro = QFileDialog.getSaveFileName(self, "Guardar")
            if ruta == "":
                return
            self.archivo_actual = ruta
        with open(self.archivo_actual, "w", encoding="utf-8") as archivo:
            archivo.write(self.editor.toPlainText())
        self.statusBar().showMessage("Archivo guardado con éxito")

    def mostrar_dock(self):
        self.dock.show()
        self.campo_buscar.setFocus()

    def buscar(self):
        texto = self.campo_buscar.text()
        if self.editor.find(texto):
            self.statusBar().showMessage("Texto encontrado")
        else:
            self.statusBar().showMessage("No se ha encontrado el texto")

    def reemplazar(self):
        texto_buscado = self.campo_buscar.text()
        if texto_buscado == "":
            self.statusBar().showMessage("Escribe el texto a buscar")
            return
        texto_seleccionado = self.editor.textCursor().selectedText()
        if texto_seleccionado.lower() == texto_buscado.lower():
            self.editor.insertPlainText(self.campo_reemplazar.text())
            self.statusBar().showMessage("Reemplazado con éxito")
        else:
            self.buscar()

    def cambiar_fuente(self):
        ok, fuente = QFontDialog.getFont(self)
        if ok:
            self.editor.setFont(fuente)

    def cambiar_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.editor.setStyleSheet("background-color: " + color.name())


if __name__ == "__main__":
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec()