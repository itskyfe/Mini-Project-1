print("Program Penghitung Gaji")

while True:
#Login Sederhana
    nama = str(input("Masukkan Nama Anda : "))
    nim = int(input("Masukkan NIM Anda : "))

    print("-------------------------------")
    print("Selamat Datang")
    print("Nama :", nama)
    print("NIM :", nim)
    print("-------------------------------")

#Input data
    jam_kerja = int(input("Masukkan Jumlah Jam Kerja Anda : "))
    tarif_kerja = int(input("Masukkan Tarif Kerja per Jam Anda : "))

#Rumus
    gaji = tarif_kerja * jam_kerja  #rumus jika jam kerja kurang dari sama dengan 160 jam 
    bonus = gaji + gaji * 10 / 100  #rumus jika jam kerja lebih dari 160 jam

#Percabangan 
    if 0 <= jam_kerja <= 160:    #jika jam kerja kurang dari sama dengan 160 jam
        print("Gaji anda =", gaji) 
    elif jam_kerja > 160:  #jika jam kerja lebih dari 160 jam
        print("Gaji anda =", bonus)
    else:   #Jika jam kerja tidak terdefinisi
        print("Anda Tidak Dapat Gaji")

#Looping
    opsi = input("Apakah Anda ingin menghitung gaji lagi? (y/n): ").lower()
    if opsi != 'y':
        print("Terima kasih telah menggunakan program ini^^")
        break