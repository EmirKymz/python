import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello World")
label.pack()

root.mainloop()


from tkinter import *
from PIL import Image, ImageTk

pencere = Tk()
pencere.geometry("400x400")

# sanatçı adları, bilet fiyatları ve resim yollarını içeren bir liste oluşturun
sanatcilar = [("Sanatçı 1", 50, "resimler/sanatci1.jpg"),
              ("Sanatçı 2", 100, "resimler/sanatci2.jpg"),
              ("Sanatçı 3", 150, "resimler/sanatci3.jpg")]

# listbox oluşturun ve sanatçı adları ve bilet fiyatlarıyla doldurun
listbox = Listbox(pencere, width=30, height=10)
for sanatci in sanatcilar:
    listbox.insert(END, "{} - {} TL".format(sanatci[0], sanatci[1]))
listbox.pack()

# resimleri listbox yanına ekleyin
def secilen_sanatci():
    # listbox'ta seçilen öğenin dizini
    sanatci_index = listbox.curselection()[0]
    # seçilen öğenin tuple'ını alın
    secilen = sanatcilar[sanatci_index]
    # resmi yükleyin ve görüntüleyin
    resim = Image.open(secilen[2])
    resim = resim.resize((100, 100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resim)
    label = Label(image=photo)
    label.image = photo
    label.pack(side=RIGHT)

# "Bilet Al" düğmesini oluşturun ve seçilen sanatçının resmini yükleyin
buton = Button(pencere, text="Bilet Al", command=secilen_sanatci)
buton.pack()

pencere.mainloop()
\




def secilen_sanatci():
    if not listbox.curselection():
        messagebox.showerror("Hata", "Lütfen bir sanatçı seçin.")
        return
    # listbox'ta seçilen öğenin dizini
    sanatci_index = listbox.curselection()[0]
    # seçilen öğenin tuple'ını alın
    secilen = sanatcilar[sanatci_index]
    # resmi yükleyin ve görüntüleyin
    resim = Image.open(secilen.resim)
    resim = resim.resize((100, 100), Image.ANTIALIAS)
    new_window = tk.Toplevel()
    photo = ImageTk.PhotoImage(resim)
    label = tk.Label(new_window, image=photo)
    label.image = photo
    label.pack(side=tk.RIGHT)