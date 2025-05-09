from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import sp
from kivy.utils import platform #Gets OS

from helpers import nombres_imagenes, Guardar, Sepia, Gris, Negado
import os


temp_image = "./temp/tmp.png"
class RootWidget(BoxLayout):
    w_width = 0
    w_height = 0

    def __init__(self):

        self.w_width, self.w_height = Window.size #Consigo el ancho y alto de la ventana
        
        super().__init__()
        # Esta linea es necesaria por que sin ella
        # se sobrescribe el init del padre y no inicializo
        # bien la clase
        
        dropdown = DropDown()
        imagenes = nombres_imagenes()
        # Para colocar un dropdown con el nombre de las imagenes
        # Creo un boton por cada imagen y lo agrego al widget dropdown
        for imagen in imagenes:       
            
            if platform == 'win':
                nombre_de_imagen = imagen.split("\\").pop() # Quito el nombre de la ruta
            else:
                nombre_de_imagen = imagen.split("/").pop() # Quito el nombre de la ruta

            btn = Button(
                text = '%s' % nombre_de_imagen, 
                size_hint_y = None, 
                height = 44, 
                background_normal = '', 
                background_color = (0, 0.839, 0.662, 1), 
                color = (0,0,0,1), 
                font_size=sp(self.w_height / 35)) 
            
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        # Agrego un boton que aloje el widget dropdown

        # vinculo objetos con ids
        mainbutton = self.ids["botonazo"]
        original = self.ids["orig"]
        modificado = self.ids["mod"]
        texto = self.ids["txt_in"]
        guardar_imagen = self.ids["save_as"]

        # actualizar atributo texto
        guardar_imagen.bind(on_press=lambda x: Guardar(modificado.source, filename=f"./resultados/{texto.text}.png"))
        
        # actualizar dropdown
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
    
    def guardar_imagen(self, text):
        print("guardando imagen")
        modificada = self.ids["mod"]
        source = modificada.source


    def aplicar_filtro(self, filter_func):
        print('aplicando filtro')
        if self.esta_procesando:
            return
            
        self.esta_procesando = True
        try:
            original = self.ids["orig"]
            modificada = self.ids["mod"]
            
            if not os.path.exists("./temp"):
                os.makedirs("./temp")
                
            modificada.source = original.source
            
            match(filter_func):
                case "gris":
                    imagen = Gris(original.source)
                    print('gris')
                case "negado":
                    imagen = Negado(original.source)
                    print('negado')
                case "sepia":
                    imagen = Sepia(original.source)
                    print('sepia')
            
            Guardar(imagen)
            
            modificada.source = temp_image
            modificada.reload()
            print('setimg')
            
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