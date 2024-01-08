from PIL import Image, ImageDraw

def rectangulo_punto(tamano_imagen, ancho_rectangulo=100, alto_rectangulo=50):
    # Calcular la cantidad de rectángulos en función del tamaño de la imagen y el tamaño de los rectángulos
    x = tamano_imagen[0] // ancho_rectangulo
    y = tamano_imagen[1] // alto_rectangulo

    # Crear una imagen con fondo transparente
    imagen = Image.new('RGBA', tamano_imagen, (0, 0, 0, 0))

    # Objeto para dibujar en la imagen
    dibujo = ImageDraw.Draw(imagen)

    # Dibujar rectángulos y puntos en el centro
    for i in range(x):
        for j in range(y):
            # Coordenadas del rectángulo
            x1 = i * ancho_rectangulo
            y1 = j * alto_rectangulo
            x2 = x1 + ancho_rectangulo
            y2 = y1 + alto_rectangulo

            # Dibujar el rectángulo
            dibujo.rectangle([x1, y1, x2, y2], outline='black')

            # Calcular el centro del rectángulo
            centro_x = (x1 + x2) // 2
            centro_y = (y1 + y2) // 2

            # Dibujar un punto en el centro
            dibujo.point((centro_x, centro_y), fill='black')

    # Guardar la imagen
    imagen.save('salida.png')

# Tamaño de la imagen deseada (2500x2500)
tamano_imagen = (2500, 2500)

def crear_imagen_con_rectangulos_y_fotos(tamano_imagen, ancho_rectangulo=100, alto_rectangulo=50, imagen_path="model.png"):
    # Calcular la cantidad de rectángulos en función del tamaño de la imagen y el tamaño de los rectángulos
    x = tamano_imagen[0] // ancho_rectangulo
    y = tamano_imagen[1] // alto_rectangulo

    # Crear una imagen con fondo transparente
    imagen = Image.new('RGBA', tamano_imagen, (0, 0, 0, 0))

    # Cargar la imagen a pegar en cada rectángulo
    imagen_a_pegar = Image.open(imagen_path)

    # Objeto para dibujar en la imagen
    dibujo = ImageDraw.Draw(imagen)

    # Dibujar rectángulos y pegar la imagen centrada
    for i in range(x):
        for j in range(y):
            # Coordenadas del rectángulo
            x1 = i * ancho_rectangulo
            y1 = j * alto_rectangulo
            x2 = x1 + ancho_rectangulo
            y2 = y1 + alto_rectangulo

            # Dibujar el rectángulo
            dibujo.rectangle([x1, y1, x2, y2], outline='black')

            # Calcular el centro del rectángulo
            centro_x = (x1 + x2) // 2
            centro_y = (y1 + y2) // 2

            # Calcular la posición superior izquierda para centrar la imagen
            posicion_superior_izquierda = (centro_x - imagen_a_pegar.width // 2, centro_y - imagen_a_pegar.height // 2)

            # Pegar la imagen centrada en el rectángulo
            imagen.paste(imagen_a_pegar, posicion_superior_izquierda, imagen_a_pegar)

    # Guardar la imagen
    imagen.save('salida.png')





"""# Ejemplo de uso con rectángulos de ancho 100 y alto 50
"""

def input_int(text):
    valid = False
    while not valid:
        try:
            value = int(input(text))
            valid = True
        except:
            print("Error: Debes ingresar un numero entero")
    return value
        

def main():
    print("Bienvenido a Zhendrek Frame Indexer")
    
    # Dimensiones
    print("Recomendacion: Cuerpos [32,64] - Barca [100, 100]")
    x = input_int("Ingrese un valor numérico para X:")
    y = input_int("Ingrese un valor numérico para Y:")

    # Modo de dibujo
    mode_valid = False
    while not mode_valid:
        print("Ingrese su opcion preferida: \na: Imagen con PJ en el medio \nb: Imagen con Punto en el medio")
        mode = input("Ingrese su opcion: ").upper()
        if mode == "A" or mode == "B":
            mode_valid = True
        else:
            print("Opcion invalida. Por favor, ingrese 'a' o 'b'")
    
    # Llamado de funcion
    tamano_imagen = (2500, 2500)
    if mode == "A":
        crear_imagen_con_rectangulos_y_fotos(tamano_imagen, ancho_rectangulo=x, alto_rectangulo=y, imagen_path = "./Recursos/body.png")
    elif mode == "B":
        rectangulo_punto(tamano_imagen, x, y)
    
    print("Imagen creada con nombre: salida.png")

main()
