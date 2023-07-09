#setting variable
n1  = input("masukkan nim  ")
n2  = input("masukkan nama  ")
n3  = input("masukkan kelas  ")
n4  = input("masukkan program study  ")

#setting variabel nilai
b_ind   = int(input("Nilai Bahasa Indonesia     :"))
b_ing   = int(input(" Nilai Bahasa Inggris      :"))
pd      = int(input("Nilai Pemrograman Dasar    :"))
mtk     = int(input("Nilai Matematika           :"))
kal1    = int(input("Nilai Klakulus 1           :"))


if(b_ind > 0 and b_ind <=60):
    gind= ("C")
elif(b_ind>60 and b_ind <=75) :
    gind = ("B")
elif(b_ind>75 and b_ind <=85) :
    gind= ("AB")
elif(b_ind >85 and b_ind<=100) :
    gind= ("A")
else: 
    gind=("Grade Anda Tidak ditemukan! ")
    
if(b_ing> 0 and b_ing <=60):
    gind2= ("C")
elif(b_ing>60 and b_ing<=75) :
    gind2 = ("B")
elif(b_ing>75 and b_ing<=85) :
    gind2= ("AB")
elif(b_ing>85 and b_ing<=100) :
    gind2= ("A")
else: 
    gind2=("Grade Anda Tidak ditemukan! ")
  
if(pd> 0 and pd<=60):
    gind3= ("C")
elif(pd>60 and pd<=75) :
    gind3 = ("B")
elif(pd>75 and pd<=85) :
    gind3= ("AB")
elif(pd>85 and pd<=100) :
    gind3= ("A")
else: 
    gind3=("Grade Anda Tidak ditemukan! ")
   
if(mtk > 0 and mtk <=60):
   gind4 = ("C")
elif(mtk>60 and mtk <=75) :
    gind4=("B")
elif(mtk >75 and mtk<=85) :
    gind4= ("AB")
elif(mtk>85 and mtk<=100) :
    gind4= ("A")
else: 
    gind4=("Grade Anda Tidak ditemukan! ")
   
if(kal1> 0 and kal1 <=60):
    gind5= ("C")
elif(kal1>60 and kal1<=75) :
    gind5= ("B")
elif(kal1>75 and kal1<=85) :
    gind5= ("AB")
elif(kal1>85 and kal1<=100) :
    gind5= ("A")
else: 
    gind5=("Grade Anda Tidak ditemukan! ")
   
   
#perhitungan
rata= (b_ind+b_ing+pd+mtk+kal1)/5

if(rata>0 and rata <=60):
    grade_rata=("C")
elif(rata>60 and rata<=75):
    grade_rata=("B")
elif(rata>75 and rata<=85):
    grade_rata=("AB")
elif(rata>85 and rata<=85):
    grade_rata=("A")
else:
    grade_rata=("grade anda tidak ditemukan!")

#menampilkan
print("------------------------------")
print(" kartu hasil study")
print("------------------------------")
print("Nim                 :",n1)
print("Nama lengkap        :",n2)
print("Kelas               :",n3)
print("Progrm study        :",n4)
print("------------------------------")
print("No Nama Makul Nilai Grade")
print("------------------------------")
print("1. bahasa indonesia  ",b_ind,gind)
print("2. bahasa inggris    ",b_ing,gind2)
print("3. pemrograman dasar ",pd,gind3)
print("4. matematika        ",mtk,gind4)
print("kalkulus 1           ",kal1,gind5)
print("------------------------------")
print("rata-rata            ",rata," ",grade_rata)
print("------------------------------")