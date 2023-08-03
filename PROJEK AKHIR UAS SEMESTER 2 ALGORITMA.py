from multiprocessing.managers import BaseListProxy


print("========= KASIR TOKO SEMBAKO PAK UNTUNG =========")
print("========= SELAMAT BERBELANJA =========")

harga = []
barang = []
total_harga = 0
while True:
    print("""
    ========= MENU TOKO =========
    --------------------------------------
    |KODE| NAMA MAKANAN | HARGA |
    --------------------------------------    
    | 1 | MIE SEDAAP         | Rp 3.500,00   |
    | 2 | MINYAK GORENG      | Rp 7.000,00   |
    | 3 | AIR MINERAL        | Rp 2.000,00   |
    --------------------------------------
    """)

    KODE = int(input("masukkan kode barang : "))
    if KODE == 1:
        barang.append("MIE SEDAAP")
        harga.append(3500)
        total_harga += 3500
    elif KODE == 2:
        barang.append("MINYAK GORENG")
        harga.append(7000)
        total_harga += 7000
    elif KODE == 3:
        barang.append("AIR MINERAL")
        harga.append(2000)
        total_harga += 2000-500
    else:
        print("barang tidak terdaftar !!!")
    
    beli_barang_lain = input("beli barang lain ?\tTekan (YES/NO) : ")
    if beli_barang_lain == "NO" :
        print("")
        break

print(f"""
barang : {barang}
harga : Rp.{harga}  
jumlah total harga : Rp.{total_harga}
      """)

bayar = int(input("Rp. "))
if bayar > total_harga:
    print("sisa uang kembali :Rp.",bayar-total_harga)
elif bayar == total_harga:
    print("anda membayar dengan uang pas tidak ada kembalian !")
else:
    print("uang yang anda bayarkan kurang :Rp.",bayar-total_harga)




