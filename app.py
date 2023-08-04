import tkinter
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("Dark") # Установка внешнего вида
ctk.set_default_color_theme("blue") # Установка темы
ctk.set_widget_scaling(1.5) # Установка коэффициента масштабирования


class FrameEntry(ctk.CTkFrame): # Создание фрейма для ввода данных
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.entry = ctk.CTkEntry(self, width=400, height=30, corner_radius=10, placeholder_text="Enter text to generate hash ...")
        self.entry.pack(padx=2, pady=4)
        self.bgButton = ctk.CTkImage(dark_image=Image.open("imageEncrypt.png"), size=(70, 15))
        self.buttonDecrypt = ctk.CTkButton(self, fg_color="#1E90FF", image=self.bgButton, text="", command=self.button_click)
        self.buttonDecrypt.place(x=4, y=36)
        self.segemented_button_var = ctk.StringVar(value="Value 1")
        self.segemented_button = ctk.CTkSegmentedButton(self, values=["SHA1", "SHA2", "SHA256", "SHA512", "MD5"],
                                                     command=self.segmented_button_callback,
                                                     variable=self.segemented_button_var)
        self.segemented_button.place(x=154, y=36)
        self.entry2 = ctk.CTkEntry(self, width=400, height=30, corner_radius=10, placeholder_text="Generated hash")
        self.entry2.pack(padx=2, pady=[50, 4])
    def button_click(self):
        print("button click")
    def segmented_button_callback(value):
        print("segmented button clicked:", value)

def slider_event(self, value):
        print(value)
def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

def segmented_button_callback(value):
    print("segmented button clicked:", value)
#Базовый фрейм
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.title("GO CASTLE")
        self.iconbitmap('main.ico')
        self.minsize(700, 300)
        self.maxsize(700,300)
        self.logo = ctk.CTkImage(dark_image=Image.open("image.png"), size=(320, 50))
        self.logoLabel = ctk.CTkLabel(self, text="", image=self.logo)
        self.logoLabel.pack(padx=2, pady=2)
        self.myFrameEntry = FrameEntry(master=self)
        self.myFrameEntry.pack(padx=2, pady=2)
        self.leVar = tkinter.StringVar()

app = App()
app.mainloop()