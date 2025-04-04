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
        if type(image) is str:
            print(image, filename)
            with Image.open(image) as im1:
                im1.save(filename)
        else:
            try:
                image.save(filename)
            finally:
                image.close()



def Gris(image):
    with Image.open(image) as im1:
        im2 = ImageOps.grayscale(im1)
        return im2.copy()

def Sepia(image):
    with Image.open(image) as img:
        width, height = img.size
        new_img = img.copy()
        pixels = new_img.load()

        for py in range(height):
            for px in range(width):
                r, g, b = img.getpixel((px, py))
                tr = min(255, int(0.393 * r + 0.769 * g + 0.189 * b))
                tg = min(255, int(0.349 * r + 0.686 * g + 0.168 * b))
                tb = min(255, int(0.272 * r + 0.534 * g + 0.131 * b))
                pixels[px, py] = (tr,tg,tb)
        return new_img

def Negado(image):
    with Image.open(image) as im1:
        im2 = ImageOps.invert(im1)
        return im2.copy()


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