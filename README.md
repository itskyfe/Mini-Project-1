# Mini-Project-1
Nama : Muhammad Rizky Febrianto NIM : 2409116045
![Flowchart Minpro daspro drawio](https://github.com/user-attachments/assets/1c069072-f235-4bfd-96da-e1576860f5ba)

Penjelasan :
1. Baris 1: Untuk memunculkan nama program dengan print
   print("Program Penghitung Gaji")
2. Baris 3: Untuk menandakan awal dari perulangan apabila dilakukan perulangan
3. Baris 5-6: Untuk membuat login sederhana, nama dengan tipe data string, dan nim dengan tipe data integer
   nama = str(input("Masukkan Nama Anda : "))
   nim = int(input("Masukkan NIM Anda : "))
5. Baris 8-12: Untuk memunculkan login sederhana dengan print
6. print("-------------------------------")
   print("Selamat Datang")
   print("Nama :", nama)
   print("NIM :", nim)
   print("-------------------------------")
8. Baris 15-16: Untuk menginput rumus menghitung gaji apabila jam kerja kurang dari sama dengan 160 jam, dan menghitung gaji dengan tambahan bonus apabila jam kerja lebih dari 160 jam
   gaji = tarif_kerja * jam_kerja
   bonus = gaji + gaji * 10 / 100
10. Baris 23-28: Untuk membuat percabangan jika jam kerja kurang dari sama dengan 160 jam dan jika jam kerja lebih dari 160 jam
    if 0 <= jam_kerja <= 160:
       print("Gaji anda =", gaji)
    elif jam_kerja > 160:
       print("Gaji anda =", bonus)
    else:
       print("Anda Tidak Dapat Gaji")
12. Baris 31-34: Untuk melakukan perulangan dengan tekan "y" untuk melakukan perulangan, tekan "n" untuk menyelesaikan program
    opsi = input("Apakah Anda ingin menghitung gaji lagi? (y/n): ").lower()
    if opsi != 'y':
    print("Terima kasih telah menggunakan program ini^^")
          break
   
 
