#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def toplama(sayi1, sayi2):
    return sayi1 + sayi2
print("Hesap Makinesi Programına Hoş Geldiniz!")

while True:
    print("İşlem Seçin:")
    print("1. Toplama")

    secim = input("Seçiminizi yapın (1): ")
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    if secim == '1':
        print("Sonuç: ", toplama(sayi1, sayi2))
    print("------------------------")


# In[ ]:




