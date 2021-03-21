import random
#zad1
# plik = open('tekst.txt',"a")
# a = random.randint(0, 100)
# b = random.randint(0, 100)
# c = random.randint(0, 100)
# d = random.randint(0, 100)
# list1 = [a,b,c,d]
# plik.writelines(str(list1))
# plik.close()

#zad2
# plik = open('tekst.txt',"r")
# linia = plik.readline()
# print(linia)
# plik.close()

#zad 3
# with open("tekst.txt","w") as plik:
#     for i in range(6):
#         plik.write("Tu coc jest napisane %d\n" %(i+1))

#zad 4
# class NaZakupy:
#     nazwa_produktu = "Makaron "
#     ilosc = 1
#     jednostka_miary = " sztuki "
#     cena_jed = 5
#     def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
#         self.nazwa_produktu=nazwa_produktu
#         self.ilosc=ilosc
#         self.jednostka_miary=jednostka_miary
#         self.cena_jed=cena_jed
#
#     def wyswietl_produkty(self):
#         return "Produkt = " + self.nazwa_produktu +" Ilość= "+ str(self.ilosc) +" Jednostka miary =  "+  self.jednostka_miary +" Cena jednostkowa= "+ str(self.cena_jed)+ " zł/"+self.jednostka_miary
#     def ile_produktu(self):
#         return "Produkt " + self.nazwa_produktu +" "+str(self.ilosc)+" "+self.jednostka_miary+self.cena_jed
#
#     def ile_kosztuje(self):
#         return int(self.ilosc) * int(self.cena_jed)
#
# obiekt=NaZakupy("tak",5,"sztuka",5)
# obiekt2=NaZakupy("tak",5,"kg","")
# obiekt3=NaZakupy("",3,"",2)
# print(obiekt.wyswietl_produkty())
# print((obiekt2.ile_produktu()))
# print(obiekt3.ile_kosztuje())

#zad 5
# class Ciag:
#     a1=0
#     n=0
#     r=0
#     w=[]
#
#     def wyswietl_dane(self):
#         return self.w
#     def pobierz_parametry(self,a1,r,n):
#         self.a1=a1
#         self.n=n
#         self.r=r
#     def policz_sume(self):
#         an=self.a1+(self.n-1)*self.r
#         sn=(self.a1+an)/2*self.n
#         self.w.extend(["Suma = %f"%sn])
#     def policz_elementy(self):
#         if self.r !=0 and self.a1 !=0:
#             for i in range(1,self.n+1):
#                 self.w.extend(["a%d= %g"%(i,(self.a1+(i-1)*self.r))])
#
# ciag = Ciag()
# ciag.pobierz_parametry(1,3,5)
# ciag.policz_sume()
# ciag.policz_elementy()
# print(ciag.wyswietl_dane())

#zad6
# class Robaczek:
#     def __init__(self,x,y,krok):
#         self.x=x
#         self.y=y
#         self.krok=krok
#     def idz_w_gore(self,ile_krokow):
#         self.y+=ile_krokow*self.krok
#     def idz_w_dol(self,ile_krokow):
#         self.y-=ile_krokow*self.krok
#     def idz_w_lewo(self,ile_krokow):
#         self.x-=ile_krokow*self.krok
#     def idz_w_prawo(self,ile_krokow):
#         self.x+=ile_krokow*self.krok
#     def pokaz_gdize_jestes(self):
#         return f"Jestes na wspolrzednych x = {self.x} i y = {self.y}"
#
# robaczek=Robaczek(3,6,1)
# print(robaczek.pokaz_gdize_jestes())
# robaczek.idz_w_gore(4)
# robaczek.idz_w_lewo(2)
# robaczek.idz_w_prawo(3)
# robaczek.idz_w_dol(3)
# print(robaczek.pokaz_gdize_jestes())
