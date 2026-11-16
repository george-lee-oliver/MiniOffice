# Mini Word

Primera versión (alfa) de MiniOffice: un editor de notas sencillo hecho con Python y PySide6.

## Requisitos

- Python 3
- PySide6

## Instalación

```
pip install PySide6
```

## Ejecución

```
python MiniWord.py
```

## Formato de archivo

El editor abre y guarda archivos de **texto plano (.txt)** en UTF-8.
El tipo de letra y el color de fondo no se guardan en el archivo, solo el texto.

## Funciones

- **Archivo:** Nuevo (Ctrl+N), Abrir (Ctrl+O), Guardar (Ctrl+S) y Salir (Ctrl+Q).
- **Editar:** Deshacer (Ctrl+Z), Rehacer (Ctrl+Y), Cortar (Ctrl+X), Copiar (Ctrl+C) y Pegar (Ctrl+V).
- **Formato:** cambiar el tipo de letra y el color de fondo del editor.
- **Buscar (Ctrl+F) y Reemplazar (Ctrl+H):** abren un panel lateral donde se escribe el texto a buscar y el texto por el que se quiere reemplazar.
- **Barra de estado:** muestra mensajes de las operaciones y un contador de palabras.