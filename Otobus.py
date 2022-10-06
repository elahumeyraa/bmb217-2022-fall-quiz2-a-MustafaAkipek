    #Ad: Mustafa
    #Soyad: Akipek 
    #No: 20217170030
    #Şube: 1

from main import cikti_test


class Otobus:
    """Otobus bilet satis takip sinifi"""
    def __init__(self,plaka,kalkis,varis,koltuksayisi):
        self.plaka = plaka
        self.kalkis = kalkis
        self.varis = varis
        self.koltuksayisi = koltuksayisi
    

    def bilet_sat(self,satilanbilet):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        for i in range():
            self.koltuksayisi -= satilanbilet
            self.dolukoltuksayisi = self.koltuksayisi
    
    def bilet_iade(self,iadeedilenbilet):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        for i in range():
            self.dolukoltuksayisi + iadeedilenbilet
            self.boskoltuksayisi = self.dolukoltuksayisi

    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print("{},{},{},{},{}".format(self.kalkis,self.varis,self.plaka,self.dolukoltuksayisi,self.boskoltuksayisi))

