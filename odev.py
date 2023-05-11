import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from PIL import ImageTk, Image

class Sanatci:
    def __init__(self, ad, bilet_fiyati, resim):
        self.ad = ad
        self.bilet_fiyati = bilet_fiyati
        self.resim = resim

sanatcilar = [
    Sanatci("Tarkan   150TL", 150, "tarkan.jpg"),
    Sanatci("Sıla 120TL", 120, "sila.jpg"),
    Sanatci("Hande Yener 100TL", 100, "handeyener.jpg"),
    Sanatci("Sezen Aksu 200TL", 200, "sezenaksu.jpg"),
    Sanatci("Ezhel 80TL", 80, "ezhel.jpg")
]

def tarih_ve_saat():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    lbl3.config(text="Tarih: " + dt_string)

def secilen_sanatci(event):
    # listbox'ta seçilen öğenin dizini
    secilen_index = listbox.curselection()
    if secilen_index:
        secilen_index = secilen_index[0]
    # seçilen öğenin tuple'ını alın
        secilen = sanatcilar[secilen_index]
    # resmi yükleyin ve görüntüleyin
        resim = Image.open(secilen.resim)
        resim = resim.resize((100, 100), Image.LANCZOS)
        resim_tk = ImageTk.PhotoImage(resim)
        label_resim.configure(image=resim_tk)
        label_resim.image = resim_tk

        label_ad.configure(text=secilen.ad)


def bilet_al():
    if listbox.curselection():
        sanatci_index = listbox.curselection()[0]
        sanatci = sanatcilar[sanatci_index]
        bilet_fiyati = sanatci.bilet_fiyati
        bilet_sayisi = entry1.get()
        if not bilet_sayisi:
            messagebox.showerror("Hata", "Lütfen bilet sayısı girin!")
        else:
            bilet_sayisi = int(entry1.get())
            toplam_tutar = bilet_fiyati * bilet_sayisi
            messagebox.showinfo("Ödeme Bilgisi", "Ödenecek Tutar: " + str(toplam_tutar) + " TL")
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir sanatçı seçin!")
        return


pencere = tk.Tk()
pencere.geometry("500x400")
pencere.title("Bilet Alma Programı")

lbl1 = tk.Label(text="Sanatçılar")
lbl1.pack()

listbox = tk.Listbox()
for sanatci in sanatcilar:
    listbox.insert("end", sanatci.ad)
listbox.pack(side="left")

lbl2 = tk.Label(text="Bilet Sayısı")
lbl2.pack()

entry1 = tk.Entry()
entry1.pack()

label_ad = tk.Label(pencere, text="")
label_ad.pack()

resim = Image.open("ticket.jpg")
resim = resim.resize((50,50), Image.LANCZOS)
# lanczos hatasi verirse alttaki yorum satirini acin
# resim = resim.resize((50,50), Image.ANTIALIAS)
resim_tk = ImageTk.PhotoImage(resim)
label_resim = tk.Label(pencere, image=resim_tk)
label_resim.pack(side="left")

listbox.bind("<<ListboxSelect>>", secilen_sanatci)

btn1 = tk.Button(text="Bilet Al", command=bilet_al)
btn1.pack()

lbl3 = tk.Label()
lbl3.pack()
tarih_ve_saat()

btn2 = tk.Button(text="Tarih ve Saat", command=tarih_ve_saat)
btn2.pack()

pencere.mainloop()
