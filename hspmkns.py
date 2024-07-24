def Toplama (a , b):
   return (a+b)
def çıkarma (a , b):
   return (a-b)

def çarpma (a , b):
   return (a*b)
  
def bölem (a , b):
   return (a/b)
a = int(input("1.sayıyı girin: "))
b = int(input("2.sayıyı girin : ")) 

print("yapılacak işlemi seçin nüfteen")
print(" toplama")
print(" çıkarma")
print(" çarpma")
print(" bölme")

secim = input("seçiminiz (top/çık/çarp/böl):")


if secim == 'top':
   print( Toplama(a,b))

elif secim == 'çık':
   print( çıkarma(a,b))

elif secim == 'böl':
   print( bölem(a,b))

elif secim == 'çarp':
   print( çarpma(a,b))

else:
   print("geçersiz karaktre") 