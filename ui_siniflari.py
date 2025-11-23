# turkcepy/ui_siniflari.py
import tkinter as tk

class Pencere:

    def __init__(self, baslik="Yeni Uygulama", genislik=400, yukseklik=300):
        self.root = tk.Tk()
        self.root.title(baslik)
        self.root.geometry(f"{genislik}x{yukseklik}")

    def baslat(self):
        self.root.mainloop()

class Etiket:
    def __init__(self, pencere_objesi, metin=""):
        self.label = tk.Label(pencere_objesi.root, text=metin)

    def yerlestir(self):
        self.label.pack(pady=10)

