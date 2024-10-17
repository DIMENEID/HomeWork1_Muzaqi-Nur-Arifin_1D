# INPUT DATA SELEKSI BIDIKMISI
nama = input('Masukkan Nama :')
nim = int(input('Masukkan NIM :'))
tempat_tanggal_lahir = input('Masukkan Tempat Tanggal Lahir :')
pekerjaan_orang_tua = input('Masukkan Pekerjaan Orang Tua (HURUF BESAR SEMUA!) :') 
gaji_orang_tua = float(input('Masukkan Gaji Orang Tua :'))
jumlah_tanggungan = int(input('Masukkan Jumlah Tanggungan Keluarga :'))
nilai_raport = float(input('Masukkan Nilai Raport (Untuk MABA jalur SNBP, Jika selain itu maka diisi 0, gunakan skala 100) :'))
nilai_snbt = float(input('Masukkan Nilai SNBT (Untuk MABA jalur SNBT, Jika selain itu maka diisi 0 :'))
ipk = float(input('Masukkan IPK (Untuk MHS SMT 3 keatas, jika selain itu maka diisi 0):'))

# SYARAT
pengecualian_pekerjaan = ['DOKTER','Dokter','dokter','POLISI','Polisi','polisi', 'TNI','Tni','tni', 'PNS','Pns','pns', 'GURU','Guru','guru']
biaya_peranggota = float(gaji_orang_tua / jumlah_tanggungan)

# PROSES SELEKSI
status_pekerjaan_orang_tua = True if (pekerjaan_orang_tua not in pengecualian_pekerjaan) else False
status_gaji_orang_tua = True if (gaji_orang_tua <= 2500000) else False
status_biaya_peranggota = True if (biaya_peranggota <= 800000) else False
status_nilai_raport = True if (nilai_raport >= 87) else False
status_nilai_snbt = True if (nilai_snbt >= 605) else False
status_ipk = True if (ipk >= 3.2) else False

# TAMPILKAN DATA YANG TELAH DIINPUT
print ('')
print ('')
print('MENYATAKAN HASIL SELEKSI PENDAFTAR BIDIKMISI DENGAN DATA :')
print ('Nama :', nama)
print ('Umur :', nim)
print ('Tempat Tanggal Lahir :', tempat_tanggal_lahir)

# HASIL SELEKSI
hasil_seleksi = 'SELAMAT ANDA DITERIMA SELEKSI BIDIKMISI' if (status_pekerjaan_orang_tua == True and (status_gaji_orang_tua == True or status_biaya_peranggota == True) and (status_nilai_raport == True or status_nilai_snbt == True or status_ipk == True)) else 'MOHON MAAF ANDA GAGAL DALAM SELEKSI BIDIKMISI'
print('')
print('     ', hasil_seleksi , '     ')
print('')
