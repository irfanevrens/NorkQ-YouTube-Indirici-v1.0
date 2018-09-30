from tkinter import *
from ttk import *
from tkinter import filedialog
import VideoDownloader
"""ITAGS = {
    5: ('240p', '64kbps'),
    6: ('270p', '64kbps'),
    13: ('144p', None),
    17: ('144p', '24kbps'),
    18: ('360p', '96kbps'),
    22: ('720p', '192kbps'),
    34: ('360p', '128kbps'),
    35: ('480p', '128kbps'),
    36: ('240p', None),
    37: ('1080p', '192kbps'),
    38: ('3072p', '192kbps'),
    43: ('360p', '128kbps'),
    44: ('480p', '128kbps'),
    45: ('720p', '192kbps'),
    46: ('1080p', '192kbps'),
    59: ('480p', '128kbps'),
    78: ('480p', '128kbps'),
    82: ('360p', '128kbps'),
    83: ('480p', '128kbps'),
    84: ('720p', '192kbps'),
    85: ('1080p', '192kbps'),
    91: ('144p', '48kbps'),
    92: ('240p', '48kbps'),
    93: ('360p', '128kbps'),
    94: ('480p', '128kbps'),
    95: ('720p', '256kbps'),
    96: ('1080p', '256kbps'),
    100: ('360p', '128kbps'),
    101: ('480p', '192kbps'),
    102: ('720p', '192kbps'),
    132: ('240p', '48kbps'),
    151: ('720p', '24kbps'),

    # DASH Video
    133: ('240p', None),
    134: ('360p', None),
    135: ('480p', None),
    136: ('720p', None),
    137: ('1080p', None),
    138: ('2160p', None),
    160: ('144p', None),
    167: ('360p', None),
    168: ('480p', None),
    169: ('720p', None),
    170: ('1080p', None),
    212: ('480p', None),
    218: ('480p', None),
    219: ('480p', None),
    242: ('240p', None),
    243: ('360p', None),
    244: ('480p', None),
    245: ('480p', None),
    246: ('480p', None),
    247: ('720p', None),
    248: ('1080p', None),
    264: ('1440p', None),
    266: ('2160p', None),
    271: ('1440p',  None),
    272: ('2160p', None),
    278: ('144p', None),
    298: ('720p', None),
    299: ('1080p', None),
    302: ('720p', None),
    303: ('1080p', None),
    308: ('1440p', None),
    313: ('2160p', None),
    315: ('2160p', None),
    330: ('144p', None),
    331: ('240p', None),
    332: ('360p', None),
    333: ('480p', None),
    334: ('720p', None),
    335: ('1080p', None),
    336: ('1440p', None),
    337: ('2160p', None),

    # DASH Audio
    139: (None, '48kbps'),
    140: (None, '128kbps'),
    141: (None, '256kbps'),
    171: (None, '128kbps'),
    172: (None, '256kbps'),
    249: (None, '50kbps'),
    250: (None, '70kbps'),
    251: (None, '160kbps'),
    256: (None, None),
    258: (None, None),
    325: (None, None),
    328: (None, None),
}"""

from tkinter import *
from ttk import *

class AnaMenu():
    acikYol = ""

    def __init__(self, master):

        #Pencere özellikleri
        master.title("NorkQ YouTube İndirici")
        master.geometry("250x300")
        master.resizable(False, False)
        master.configure(background="white")

        #Araçların tanımlanması
        self._link = Entry(master, width=40)
        self._link.pack()
        self._indirmeYolu = Entry(master, width=30)
        self._indirmeYolu.pack()
        self._indirmeYolu.insert(0, "C:/")
        # VideoDownloader dosyasının yola ulaşabilmesi için acikYol degiskenine _indirmeYolunun default değerini gönderiyorum.
        acikYol = str(self._indirmeYolu.get())
        self._yolSec = Button(text="Seç", width=7, command=self.YolDegistir)
        self._yolSec.pack()
        self._indirmeTuru = Combobox(master, values=("144p Video", "240p Video", "360p Video", "480p Video", "720p Video", "1080p Video", "1440p Video", "2160p Video(Ses yok)", "128kbps Ses", "256kbps Ses"), width=38)
        self._indirmeTuru.pack()

        self._indirButon = Button(master, text="İndir", width=39, command=self.Indır)
        self._indirButon.pack()

        #Araçlara gerekli özellikleri eklemek
        self._link.insert(0, "Linkinizi yapıştırınız")
        self._link.place(relx=0, rely=0)
        self._indirmeTuru.set("İndirme Türü")
        self._indirmeTuru.place(relx=0, rely=0.173)
        self._indirmeYolu.place(relx=0, rely=0.08)
        self._yolSec.place(relx=0.75, rely=0.07)
        self._indirButon.place(rely=0.894)



    def YolDegistir(self):
        self._indirmeYolu.delete(0, END)
        self._indirmeYolu.insert(0, filedialog.askdirectory())
        acikYol = str(self._indirmeYolu.get())
        print(acikYol) #Fonksiyonun çalışıp çalışmadığını kontrol ediyoruz.

    def Indır(self):
        #Butonda kullanabilmek için yeni bir fonksiyon tanımlıyoruz.
        VideoDownloader.Video.VideoIndır(str(self._link.get()), str(self._indirmeTuru.get()))


if __name__ == "__main__":
    root = Tk()
    root.style = Style()

    root.style.theme_use("clam")

    app = AnaMenu(root)
    root.mainloop()