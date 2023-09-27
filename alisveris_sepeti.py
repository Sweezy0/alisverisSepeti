class AlisverisSepeti:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, *args, **kwargs):
        for urun in args:
            self.urunler.append(urun)
        for urun, miktar in kwargs.items():
            self.urunler.extend([urun] * miktar)

    def urun_cikar(self, *args, **kwargs):
        for urun in args:
            if urun in self.urunler:
                self.urunler.remove(urun)
        for urun, miktar in kwargs.items():
            for i in range(miktar):
                if urun in self.urunler:
                    self.urunler.remove(urun)

    def sepeti_goster(self):
        print("Alışveriş Sepeti:")
        for urun in self.urunler:
            print(urun)

# Alışveriş sepeti oluştur
sepet = AlisverisSepeti()

# Ürünleri sepete ekleyin
sepet.urun_ekle("Elma", "Muz", elma=2, portakal=3)

# Sepeti göster
sepet.sepeti_goster()

# Ürünleri sepetten çıkarın
sepet.urun_cikar("Elma", "Karpuz", muz=1)

# Güncellenmiş sepeti göster
sepet.sepeti_goster()