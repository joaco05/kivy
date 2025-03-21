from glob import glob
from os.path import join, dirname

from PIL import Image, ImageOps

def nombres_imagenes():
    # Consegui los nombres del archivo
    images = set()
    curdir = dirname(__file__)
    for filename in glob(join(curdir, 'images', '*')):
        images.add(filename)
    return tuple(images)

def Guardar(image, filename = "./temp/tmp.png"):
    image.save(filename)

def Gris(image):
    im1 = Image.open(image)
    im2 = ImageOps.grayscale(im1) 
    return im2 


def Sepia(image):
    img = Image.open(image)
    width, height = img.size

    pixels = img.load() # Carga la imagen en un mapa de pixeles

    for py in range(height):
     for px in range(width):
         r, g, b = img.getpixel((px, py))

         tr = int(0.393 * r + 0.769 * g + 0.189 * b)
         tg = int(0.349 * r + 0.686 * g + 0.168 * b)
         tb = int(0.272 * r + 0.534 * g + 0.131 * b)

         if tr > 255:
             tr = 255

         if tg > 255:
             tg = 255

         if tb > 255:
             tb = 255

         pixels[px, py] = (tr,tg,tb)

    return img

def Negado(image):
    im1 = Image.open(image)
    im2 = ImageOps.invert(im1) 
    return im2


# Se ejecuta solo si corro el archivo fuera de una libreria
if __name__ == "__main__":

    imagenes = nombres_imagenes()
    Image.open(imagenes[0]).show()

    imagen = Gris(imagenes[0])
    imagen.show()

    imagen = Negado(imagenes[0])
    imagen.show()

    imagen = Sepia(imagenes[0])
    imagen.show()

    # Para guardar las imagenes
    Guardar(imagen)