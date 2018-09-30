from pytube import *
import Ana

#"144p Video", "240p Video", "360p Video", "480p Video", "720p Video", "1080p Video", "1440p Video", "2160p Video", "128kbps Ses", "256kbps Ses"
class Video():
    #VideoIndır Fonksiyonu her çalıştığında tekrar tekrar None değerini almaması için sınıf niteliği olarak oluşturuyoruz.
    _cozunurluk = None
    #Videoyu indirmek için gerekli fonksiyonu yazıyoruz.
    @classmethod
    def VideoIndır(cls, _link, _indirmeTuru):

        if _indirmeTuru == "144p Video":
            _cozunurluk = 17
        elif _indirmeTuru == "240p Video":
            _cozunurluk = 5
        elif _indirmeTuru == "360p Video":
            _cozunurluk = 34
        elif _indirmeTuru == "480p Video":
            _cozunurluk = 35
        elif _indirmeTuru == "720p Video":
            _cozunurluk = 95
        elif _indirmeTuru == "1080p Video":
            _cozunurluk = 96
        elif _indirmeTuru == "2160p Video":
            _cozunurluk = 138
        cls.yt = YouTube(_link).streams.get_by_itag(_cozunurluk)
        cls.yt.download(Ana.AnaMenu.acikYol)

