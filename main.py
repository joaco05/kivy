from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

from helpers import nombres_imagenes, Guardar, Sepia, Gris, Negado
import os


#TODO add on_resize resizes
temp_image = "./temp/tmp.png"
class RootWidget(BoxLayout):
    w_width = 0
    w_height = 0

<<<<<<< HEAD
=======
    def on_window_resize(self, window, width, height):
        # Esta funcion se llama cada vez que se redimensiona la ventana
        # y actualiza el tamaño de la ventana
        self.w_width, self.w_height = Window.size

>>>>>>> 3507a725cb4fa10a75c74bc9fb1e8931a6c3174b
    def __init__(self):

        self.w_width, self.w_height = Window.size #Consigo el ancho y alto de la ventana
        # Esta linea es necesaria por que sin ella
        # se sobrescribe el init del padre y no inicializo
        # bien la clase
        
        super().__init__()
<<<<<<< HEAD
        Window.bind(on_resize=self.on_window_resize)
=======

        self.w_width, self.w_height = Window.size #Consigo el ancho y alto de la ventana
        Window.bind(on_resize=self.on_window_resize)

>>>>>>> 3507a725cb4fa10a75c74bc9fb1e8931a6c3174b
        dropdown = DropDown()
        imagenes = nombres_imagenes()
        # Para colocar un dropdown con el nombre de las imagenes
        # Creo un boton por cada imagen y lo agrego al widget dropdown
        for imagen in imagenes:
            # Quito el nombre de la ruta
            nombre_de_imagen = imagen.split("\\").pop()
            btn = Button(text='%s' % nombre_de_imagen, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        # Agrego un boton que aloje el widget dropdown
        print(f"las ids son {self.ids}")

<<<<<<< HEAD
        # vinculo objetos con ids
=======
>>>>>>> 3507a725cb4fa10a75c74bc9fb1e8931a6c3174b
        mainbutton = self.ids["botonazo"]
        original = self.ids["orig"]

        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(original, 'source', f"./images/{x}"))

        #funcionalidad filtros
        sepia = self.ids["filter_sepia"]
        gris = self.ids["filter_grey"]
        negado = self.ids["filter_invert"]
        self.esta_procesando = False
        
        sepia.bind(on_press=lambda x: self.aplicar_filtro("sepia"))
        gris.bind(on_press=lambda x: self.aplicar_filtro("gris"))
        negado.bind(on_press=lambda x: self.aplicar_filtro("negado"))

        return
    

    def on_window_resize(self, window, width, height):
        # Esta funcion se llama cada vez que se redimensiona la ventana
        # y actualiza el tamaño de la ventana
        self.w_width, self.w_height = Window.size
        return
        
    def aplicar_filtro(self, filter_func):
        if self.esta_procesando:
            return
            
        self.esta_procesando = True
        try:
            original = self.ids["orig"]
            modificada = self.ids["mod"]
            
            # Create temp directory if it doesn't exist
            if not os.path.exists("./temp"):
                os.makedirs("./temp")
                
            setattr(modificada, 'source', '')
            
            match(filter_func):
                case "gris":
                    imagen = Gris(original.source)
                case "negado":
                    imagen = Negado(original.source)
                case "sepia":
                    imagen = Sepia(original.source)
                    
            Guardar(imagen)
            
            setattr(modificada, 'source', temp_image)
            
        except Exception as e:
            print(f"Error aplicando filtro: {e}")
        finally:
            self.esta_procesando = False



class ProgramaApp(App):
    def build(self):
        print(Window.size)
        return RootWidget()



        


if __name__ == "__main__":
    ProgramaApp().run()