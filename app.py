import tkinter
import customtkinter as ctk
from PIL import Image
import hashlib
import tkinter.messagebox as tmb

ctk.set_appearance_mode("Dark") # Установка внешнего вида
ctk.set_default_color_theme("blue") # Установка темы
ctk.set_widget_scaling(1.5) # Установка коэффициента масштабирования

class FrameEntry(ctk.CTkFrame): # Создание фрейма для ввода данных
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.value = None # Переменная хранящая состояния сегментного меню
        self.entry = ctk.CTkEntry(self, width=490, # - Поле ввода
                                height=30, 
                                corner_radius=10, 
                                placeholder_text="Enter text to generate hash ...")
        self.entry.pack(padx=2, pady=4)
        self.bgButton = ctk.CTkImage(dark_image=Image.open("imageEncrypt.png"), size=(80, 15)) # - Фон для кнопки хеширования
        self.buttonEncrypt = ctk.CTkButton(self, fg_color="#1E90FF", # - Кнопка хеширования
                                           image=self.bgButton, 
                                           text="", 
                                           command=self.buttonClick)
        self.buttonEncrypt.place(x=4, y=36)
        self.segementedButtonVar = ctk.StringVar(value="Value 1")
        self.segementedButton = ctk.CTkSegmentedButton(self, values=["SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "MD5"],
                                                     command=self.segmentedButtonCallback,
                                                     variable=self.segementedButtonVar)
        self.segementedButton.place(x=168, y=36)
        self.entry2 = ctk.CTkEntry(self, width=490, 
                                   height=30, 
                                   corner_radius=10, 
                                   placeholder_text="--Generated hash--")
        self.entry2.pack(padx=2, pady=[50, 4])
    def buttonClick(self): # - функция хеширования строки
        if self.value == "SHA1":
            stringObject = self.entry.get()
            hashObject = hashlib.sha1(stringObject.encode()).hexdigest()
            self.entry2.delete(0, tkinter.END) # 41
            self.entry2.insert(0, hashObject)
        
        elif self.value == "SHA224":
            stringObject = self.entry.get()
            hashObject = hashlib.sha224(stringObject.encode()).hexdigest()
            self.entry2.delete(0, tkinter.END) # 57
            self.entry2.insert(0, hashObject)
        
        elif self.value == "SHA256":
            stringObject = self.entry.get()
            hashObject = hashlib.sha256(stringObject.encode()).hexdigest()
            self.entry2.delete(0, tkinter.END)# 65
            self.entry2.insert(0, hashObject)
        
        elif self.value == "SHA384":
            stringObject = self.entry.get()
            hashObject = hashlib.sha384(stringObject.encode()).hexdigest()
            self.entry2.delete(0, tkinter.END)# 97
            self.entry2.insert(0, hashObject)

        elif self.value == "SHA512":
            stringObject = self.entry.get()
            hashObject = hashlib.sha512(stringObject.encode()).hexdigest()
            self.entry2.delete(0, tkinter.END)
            self.entry2.insert(0, hashObject)
        
        elif self.value == "MD5":
            stringObject = self.entry.get()
            hashObject = hashlib.md5(stringObject.encode()).hexdigest()
            self.entry2.delete(0, tkinter.END)
            self.entry2.insert(0, hashObject)

        else:
            tmb.showwarning(title="Предупреждение", message="Выбери протокол хеширования!")
# Данная функция проверяет какой пункт сегментного меню выбран и сохраняет в переменную self.value
# - значение выбранного сегмента.
    def segmentedButtonCallback(self, value):
        if value == "SHA1":
            self.value = "SHA1"
            print("segmented button clicked:", value) # Проверка выбора сегмента в консоли
            return value, self.value
        elif value == "SHA224":
            self.value = "SHA224"
            print("segmented button clicked:", value) # Проверка выбора сегмента в консоли
            return value, self.value
        elif value == "SHA256":
            self.value = "SHA256"
            print("segmented button clicked:", value) # Проверка выбора сегмента в консоли
            return value, self.value
        elif value == "SHA384":
            self.value = "SHA384"
            print("segmented button clicked:", value) # Проверка выбора сегмента в консоли
            return value, self.value
        elif value == "SHA512":
            self.value = "SHA512"
            print("segmented button clicked:", value) # Проверка выбора сегмента в консоли
            return value, self.value
        elif value == "MD5":
            self.value = "MD5"
            print("segmented button clicked:", value) # Проверка выбора сегмента в консоли
            return value, self.value


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.title("GO CASTLE")
        self.iconbitmap('main.ico')
        self.minsize(750, 300)
        self.maxsize(750,300)
        self.logo = ctk.CTkImage(dark_image=Image.open("image.png"), size=(320, 50))
        self.logoLabel = ctk.CTkLabel(self, text="", image=self.logo)
        self.logoLabel.pack(padx=2, pady=2)
        self.myFrameEntry = FrameEntry(master=self)
        self.myFrameEntry.pack(padx=2, pady=2)
        self.leVar = tkinter.StringVar()

app = App()
app.mainloop()