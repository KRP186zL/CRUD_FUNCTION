import function.fungsi
import os
import time
#Running
def main():  
    while True:
        try:
            os.system("clear")
            print(f"""{'*'*30}\n*{'APLIKASI':^28}*\n*{'CRUD SEDERHANA':^28}*\n*{'*'*28}*
* MENU:{'*':>23}
* 1.Tambah Mahasiswa{'*':>10}
* 2.Lihat Mahasiswa{'*':>11}
* 3.Update Mahasiswa{'*':>10}
* 4.Delete Mahasiswa{'*':>10}
* 5.Exit Program{'*':>14}\n{'*'*30}""")
            menu = int(input("Masukkan Pilihan Anda [1/2/3/4/5]: "))
            if menu == 1 :
                function.fungsi.tambah_mahasiswa()
            if menu == 2 :
                function.fungsi.lihat_mahasiswa()
            if menu == 3 :
                function.fungsi.update_mahasiswa()
            if menu == 4 :
               function.fungsi.hapus_mahasiswa()
            if menu == 5 :
                print("\n\nterima kasih sudah menggunakan program saya :)".upper())
                exit()
            else:
                print("Pilihan tidak tersedia. Silahkan pilih kembali !")
                time.sleep(1.2)
            pass
        except ValueError:
            print("Mohon gunakan angka!")
            time.sleep(1.2)

print(main())