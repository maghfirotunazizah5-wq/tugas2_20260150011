print ("---Data Diri---")
nama         = input ("Masukkan nama : ")
NIM          = input ("Masukkan NIM : ")
berat_badan  = float(input ("Masukkan berat badan (kg) : "))
tinggi_badan = float(input ("Masukkan tinggi badan (cm) : "))

tinggi_meter = tinggi_badan / 100
bmi = berat_badan / (tinggi_meter ** 2)
print (f" BMI anda adalah : {bmi:.2f}")

print ("\n=== PROGRAM SISTEM KASIR ===")
barang_1 = input ("Masukkan nama barang 1 : ")
harga_1 = float(input ("Masukkan harga barang 1 (Rp) : "))
barang_2 = input ("Masukkan nama barang 2 : ")
harga_2  = float(input ("Masukkan harga barang 2 (Rp) : "))
total_harga = harga_1 + harga_2
diskon = total_harga * 0.05
harga_setelah_diskon = total_harga - diskon
pajak = harga_setelah_diskon *0.11
total_bayar = harga_setelah_diskon + pajak
total_harga_print = round(total_harga, 2)
diskon_print = round (diskon, 2)
pajak_print  = round (pajak, 2)
total_bayar_print = round (total_bayar, 2)

print ("\n---Struk Belanja---")
print (f"Nama Barang 1 : {barang_1} / harga : Rp {harga_1}")
print (f"Nama Barang 2 : {barang_2} / harga : Rp {harga_2}")
print("-"*30)
print (f"Total_harga : Rp {total_harga_print}")
print (f"Diskon 5% : Rp {diskon_print}")
print (f"pajak 11% : Rp {pajak_print}")
print ("-"*30)
print (f"Total bayar : Rp {total_bayar_print}")
print("=====Terima Kasih Telah Berbelanja di toko kami=====")