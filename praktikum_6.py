data_nilai = {}


def tambah():
    print('\nTambah Data Nilai Mahasiswa')
    print('=============================')
    nama = input('\nMasukkan Nama Mahasiswa\t\t: ')
    nim = int(input('Masukkan NIM Mahasiswa\t\t: '))
    tugas = int(input('Masukkan Nilai Tugas Mahasiswa\t: '))
    uts = int(input('Masukkan Nilai UTS Mahasiswa\t: '))
    uas = int(input('Masukkan Nilai UAS Mahasiswa\t: '))
    hasil = (tugas*0.3) + (uts*0.35) + (uas*0.35)
    data_nilai[nama] = nim, tugas, uts, uas, hasil
    print('\nUntuk melihat data yang sudah ditambahkan silakan pilih nomor 2')

def hapus():
    print('Hapus Data Mahasiswa')
    print('====================')
    nama = input('Masukkan Nama Mahasiswa\t\t:')
    if nama in data_nilai.keys():
        del data_nilai[nama]
        print('\nData mahasiswa berhasil dihapus')
    else:
        print('\nData {0} Tidak Ditemukan'.format(nama))

def ubah():
    print('\nMengubah Data Mahasiswa')
    print('=======================')
    nama = input('Masukkan Nama Mahasiswa\t\t\t: ')
    if nama in data_nilai.keys():
        nim = int(input('Masukkan NIM Baru Mahasiswa\t\t: '))
        tugas = int(input('Masukkan Nilai Tugas Terbaru\t\t: '))
        uts = int(input('Masukkan Nilai UTS Terbaru\t\t: '))
        uas = int(input('Masukkan Nilai UAS Terbaru\t\t: '))
        hasil = (tugas*0.3) + (uts*0.35) + (uas*0.35)
        data_nilai[nama] = nim, tugas, uts, uas, hasil
        print('\nData mahasiswa berhasil diubah pilih nomor 2 untuk melihat data terbaru')

def tampil():
    if data_nilai.items():
        print('\n========================== Daftar Nilai Mahasiswa ===================================')
        print('======================================================================================')
        print('|  NO. |      NAMA     |     NIM    |    TUGAS   |   UTS   |   UAS   |  NILAI AKHIR  |')
        print('======================================================================================')
        i = 0
        for x in data_nilai.items():
            i += 1
            print('| {6:4} | {0:13s} | {1:13} | {2:8d} |  {3:6d} | {4:7d} | {5:12.2f} | '
                      .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print('=====================================================================================')
    else:
        print('===================================== Daftar Nilai ===================================')
        print('======================================================================================')
        print('|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |')
        print('======================================================================================')
        print('|                                    Tidak Ada Data                                  |')
        print('======================================================================================')

while True:
    print('\nPilih salah satu menu di bawah ini:')
    print('=====================================')
    print('\n1.Tambah \n2.Tampil \n3.Hapus \n4.Ubah \n5.Keluar dari program')
    x = input('\nMasukkan Pilihan Menu anda\t: ')
    if x.lower() == "1":
        tambah()
    elif x.lower() == "2":
        tampil()
    elif x.lower() == "3":
        hapus()
    elif x.lower() == "4":
        ubah()
    elif x.lower() == "5":
        print('\nAnda sudah keluar dari program')
        break

    else:
        print('\nPilih menu yang tersedia di atas')
