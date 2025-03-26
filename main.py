from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

from helpers import nombres_imagenes, Guardar, Sepia, Gris, Negado

class RootWidget(BoxLayout):
    w_width = 0
    w_height = 0

    def on_window_resize(self, window, width, height):
        # Esta funcion se llama cada vez que se redimensiona la ventana
        # y actualiza el tamaño de la ventana
        self.w_width, self.w_height = Window.size

    def __init__(self):
        # Esta linea es necesaria por que sin ella
        # se sobrescribe el init del padre y no inicializo
        # bien la clase
        super().__init__()

        self.w_width, self.w_height = Window.size #Consigo el ancho y alto de la ventana
        Window.bind(on_resize=self.on_window_resize)

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

        mainbutton = self.ids["botonazo"]
        mainbutton.bind(on_release=dropdown.open)
        mainbutton.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        return
        
    



class ProgramaApp(App):
    def build(self):
        print(Window.size)
        return RootWidget()



        


if __name__ == "__main__":
    ProgramaApp().run()