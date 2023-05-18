#!/usr/bin/env python
# coding: utf-8

# In[1]:


def toplama(sayi1, sayi2):
    return sayi1 + sayi2

def cikarma(sayi1, sayi2):
    return sayi1 - sayi2

def carpma(sayi1, sayi2):
    return sayi1 * sayi2

def bolme(sayi1, sayi2):
    if sayi2 != 0:
        return sayi1 / sayi2
    else:
        return "Hata: Sıfıra bölme hatası!"

print("Hesap Makinesi Programına Hoş Geldiniz!")

while True:
    print("İşlem Seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

    secim = input("Seçiminizi yapın (1/2/3/4/5): ")

    if secim == '5':
        print("Hesap makinesi kapatılıyor...")
        break

    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    if secim == '1':
        print("Sonuç: ", toplama(sayi1, sayi2))
    elif secim == '2':
        print("Sonuç: ", cikarma(sayi1, sayi2))
    elif secim == '3':
        print("Sonuç: ", carpma(sayi1, sayi2))
    elif secim == '4':
        print("Sonuç: ", bolme(sayi1, sayi2))
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")

    print("------------------------")


# In[ ]:




