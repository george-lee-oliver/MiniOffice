# Mini Office

Editor de texto sencillo hecho con Python y PySide6 para la asignatura de Desarrollo de Interfaces (2º DAM).

Es la continuación de la versión alfa (Mini Word). En esta versión he ampliado el panel lateral de buscar y reemplazar, que ahora tiene Buscar anterior, Buscar todas y Reemplazar todas y he añadido dos funciones nuevas: zoom y negrita/cursiva/subrayado.

## Requisitos

- Python 3
- PySide6

## Instalación

Instalar PySide6:

```
pip install PySide6
```

## Ejecución

Desde la carpeta del proyecto:

```
python MiniOffice.py
```

## Funciones principales, menús y atajos

### Archivo

| Opción | Atajo | Qué hace |
|---|---|---|
| Nuevo | Ctrl+N | Deja el documento vacío |
| Abrir | Ctrl+O | Abre un archivo .txt y lo carga en el editor |
| Guardar | Ctrl+S | Guarda el texto. Si el documento no tiene archivo, pregunta dónde guardarlo |
| Salir | Ctrl+Q | Cierra la aplicación |

### Editar

| Opción | Atajo |
|---|---|
| Deshacer | Ctrl+Z |
| Rehacer | Ctrl+Y |
| Cortar | Ctrl+X |
| Copiar | Ctrl+C |
| Pegar | Ctrl+V |
| Buscar | Ctrl+F |
| Reemplazar | Ctrl+H |

### Formato

| Opción | Atajo |
|---|---|
| Tipo de letra | Sin atajo |
| Color de fondo | Sin atajo |
| Negrita | Ctrl+B |
| Cursiva | Ctrl+I |
| Subrayado | Ctrl+U |

### Ver

| Opción | Atajo |
|---|---|
| Acercar | Ctrl++ |
| Alejar | Ctrl+- |

La barra de herramientas tiene los botones Nuevo, Abrir, Guardar, Deshacer, Rehacer, Cortar, Copiar, Pegar, Buscar y Reemplazar. Usan las mismas acciones que los menús.

En la barra de estado salen los mensajes de cada operación (por ejemplo "Archivo guardado con éxito") y a la derecha un contador de palabras que se actualiza al escribir, al abrir un archivo y al pulsar Nuevo.

## Formato de archivo

El editor abre y guarda archivos de **texto plano (.txt)** en UTF-8.

El archivo .txt solo guarda el texto. **No guarda** la negrita, la cursiva, el subrayado, el tipo de letra, el color de fondo ni el zoom. Al volver a abrir el archivo el texto sale sin formato.

## Panel de buscar y reemplazar

Se abre con **Buscar** o **Reemplazar** (desde el menú Editar, la barra de herramientas o con Ctrl+F / Ctrl+H). Aparece a la derecha del editor y el documento se sigue viendo mientras se usa.

Si se cierra con la X y se vuelve a abrir, sale el mismo panel, sin duplicar los controles y con el texto que se había escrito.

El panel tiene:

- **Texto a buscar**: la palabra que se quiere buscar. Pulsando Enter también busca la siguiente.
- **Buscar siguiente**: busca la siguiente coincidencia hacia delante desde donde está el cursor.
- **Buscar anterior**: busca la coincidencia anterior hacia atrás desde donde está el cursor.
- **Buscar todas**: cuenta cuántas veces aparece la palabra en todo el documento y lo muestra en la barra de estado.
- **Reemplazar por**: el texto que se va a poner en lugar de la palabra buscada.
- **Reemplazar**: si la palabra buscada está seleccionada, la cambia. Si no, busca la siguiente para seleccionarla (y al pulsar otra vez la cambia).
- **Reemplazar todas**: cambia todas las coincidencias del documento y dice cuántas ha cambiado.

### Reglas de búsqueda

- **No distingue mayúsculas y minúsculas**: buscar "partido" también encuentra "Partido".
- **Coincidencia parcial**: encuentra la palabra aunque esté dentro de otra. Buscar "partido" también encuentra "partidos".
- **Al llegar al final o al principio** la búsqueda se para y avisa con "No se han encontrado más hacia adelante" o "No se han encontrado más hacia atrás". No vuelve a empezar sola.
- **Buscar todas** y **Reemplazar todas** recorren siempre el documento entero desde el principio.
- Si el campo de búsqueda está **vacío**, sale el mensaje "Escribe un texto para buscar".
- Si la palabra **no existe**, sale un mensaje avisando de que no se ha encontrado.
- En estos casos el documento **no se modifica**.

## Mejoras añadidas

### Zoom

**Qué aporta:** permite ver el texto más grande o más pequeño sin cambiar el documento. Es útil para leer mejor o para ver más texto en la pantalla.

**Cómo se usa:** con **Ctrl++** para acercar y **Ctrl+-** para alejar o desde el menú **Ver > Acercar** y **Ver > Alejar**.

**Cómo comprobarlo:**
1. Escribir un texto en el editor.
2. Pulsar Ctrl++ varias veces: el texto se ve más grande.
3. Pulsar Ctrl+- varias veces: el texto se ve más pequeño.

### Negrita, cursiva y subrayado

**Qué aporta:** permite resaltar partes del texto.

**Cómo se usa:** seleccionar el texto y pulsar **Ctrl+B** (negrita), **Ctrl+I** (cursiva) o **Ctrl+U** (subrayado) o usar el menú **Formato**. Si se vuelve a pulsar, se quita.

**Cómo comprobarlo:**
1. Seleccionar una palabra y pulsar Ctrl+B: se pone en negrita.
2. Seleccionar otra y pulsar Ctrl+I: se pone en cursiva.
3. Seleccionar otra y pulsar Ctrl+U: se subraya.
4. Volver a seleccionar la primera y pulsar Ctrl+B: se quita la negrita.

Recordar que estos estilos no se guardan en el .txt.

## Pruebas realizadas

Para las pruebas usé este texto, donde "partido" aparece 4 veces:

```
Este finde hay partido del Betis. El partido es el sabado a las 9.
Quedamos en casa de Pablo para ver el partido y pedir unas pizzas.
Si ganamos el partido salimos a celebrarlo.
```

### Prueba 1 - Buscar siguiente
- **Esperaba:** que fuera pasando por los 4 "partido" y al final avisara de que no hay más.
- **Resultado:** correcto. Recorre las 4 coincidencias y al final muestra "No se han encontrado más hacia adelante".

![Buscar siguiente](Capturas/buscar_siguiente.png)

### Prueba 2 - Buscar anterior
- **Esperaba:** que fuera hacia atrás por los "partido" y al llegar al primero avisara de que no hay más.
- **Resultado:** correcto. Recorre las coincidencias hacia atrás y al llegar al primero muestra "No se han encontrado más hacia atrás".

![Buscar anterior](Capturas/buscar_anterior.png)

### Prueba 3 - Buscar todas
- **Esperaba:** que contara todas las veces que aparece "partido" en el texto.
- **Resultado:** correcto. Muestra "Se han encontrado 4 coincidencias".

![Buscar todas](Capturas/buscar_todas.png)

### Prueba 4 - Reemplazar una
- **Esperaba:** que solo cambiara el "partido" seleccionado por "concierto" y el resto siguiera igual.
- **Resultado:** correcto. Cambia solo esa coincidencia y muestra "Texto reemplazado".

![Reemplazar](Capturas/reemplazar.png)

### Prueba 5 - Reemplazar todas
- **Esperaba:** que cambiara los 3 "partido" que quedaban por "concierto" y dijera cuántos ha cambiado.
- **Resultado:** correcto. Reemplaza las 3 coincidencias que faltaban y muestra "Se han reemplazado 3 coincidencias".

![Reemplazar todas](Capturas/reemplazar_todas.png)

### Prueba 6 - Palabra que no existe
- **Esperaba:** que avisara de que no encuentra "perro" y que el texto no cambiara.
- **Resultado:** correcto. Buscar todas y Reemplazar todas muestran "No se ha encontrado el texto", Buscar siguiente muestra "No se han encontrado más hacia adelante" y Buscar anterior "No se han encontrado más hacia atrás". El documento no se modifica.

![Palabra que no existe](Capturas/palabra_no_existe.png)

### Prueba 7 - Campo vacío
- **Esperaba:** que avisara de que hay que escribir algo y que el texto no cambiara.
- **Resultado:** correcto. Todos los botones del dock muestran "Escribe un texto para buscar" y el documento no se modifica.

![Campo vacío](Capturas/campo_vacio.png)

### Prueba 8 - Abrir y guardar después de usar el dock
- **Esperaba:** poder guardar el texto, crear un documento nuevo y volver a abrir el archivo con el mismo texto.
- **Resultado:** correcto. Al guardar muestra "Archivo guardado con éxito". Al pulsar Nuevo el editor se queda vacío y el contador pasa a "Palabras: 0". Al abrir prueba.txt aparece el mismo texto y muestra "Archivo abierto con éxito".

![Guardar](Capturas/guardar.png)
![Nuevo](Capturas/nuevo.png)
![Abrir](Capturas/abrir.png)

### Prueba 9 - Editar y redimensionar después de usar el dock
- **Esperaba:** poder seguir escribiendo en el editor y que al cambiar el tamaño de la ventana todo se adaptara.
- **Resultado:** correcto. Se puede escribir con normalidad y el contador de palabras se actualiza. Al hacer la ventana más pequeña o más grande, el editor se ajusta y el dock se mantiene a la derecha.

![Editar](Capturas/editar.png)
![Redimensionar](Capturas/redimensionar.png)

### Prueba 10 - Cerrar y volver a abrir el dock
- **Esperaba:** que al cerrar el dock y volver a abrirlo apareciera el mismo dock sin duplicar controles.
- **Resultado:** correcto. Al cerrarlo con la X desaparece y al volver a abrirlo con Ctrl+F, el botón Buscar o el botón Reemplazar aparece el mismo dock con los mismos botones y con el mismo texto que había escrito en el campo de búsqueda.

![Dock cerrado](Capturas/dock_cerrado.png)
![Dock reutilizado](Capturas/dock_reutilizado.png)

### Prueba 11 - Zoom
- **Esperaba:** que el texto se viera más grande al acercar y más pequeño al alejar, tanto con los atajos como desde el menú Ver.
- **Resultado:** correcto. Con Ctrl++ o Ver > Acercar el texto se agranda y con Ctrl+- o Ver > Alejar se hace más pequeño. El contenido del documento no cambia, solo cómo se vé.

![Zoom acercar](Capturas/zoom_acercar.png)
![Zoom alejar](Capturas/zoom_alejar.png)

### Prueba 12 - Negrita, cursiva y subrayado
- **Esperaba:** que al seleccionar una palabra y usar Ctrl+B, Ctrl+I o Ctrl+U se aplicara el formato y que al repetirlo se quitara.
- **Resultado:** correcto. Se aplica negrita, cursiva y subrayado a la palabra seleccionada, tanto con los atajos como desde el menú Formato y al pulsarlo de nuevo se quita.

![Formato](Capturas/formato.png)

### Prueba 13 - El .txt no guarda los estilos
- **Esperaba:** que al guardar y volver a abrir el archivo se conservara el texto pero no la negrita, la cursiva ni el subrayado porque el formato .txt solo guarda texto plano.
- **Resultado:** correcto. Al abrir prueba.txt aparece el mismo texto pero sin ningún estilo.

![Txt sin formato](Capturas/txt_sin_formato.png)

## Limitaciones conocidas

- Solo trabaja con archivos .txt en UTF-8. Si se intenta abrir otro tipo de archivo (por ejemplo un .docx o una imagen) la aplicación puede cerrarse.
- El .txt no guarda la negrita, la cursiva, el subrayado, el tipo de letra, el color de fondo ni el zoom.
- El tipo de letra y el color de fondo se aplican a todo el editor, no a una parte del texto.
- La búsqueda no tiene opción para distinguir mayúsculas ni para buscar solo palabras completas.
- Al llegar al final o al principio, la búsqueda no vuelve a empezar sola.
- No avisa si hay cambios sin guardar al pulsar Nuevo, Abrir o Salir, así que esos cambios se pierden.