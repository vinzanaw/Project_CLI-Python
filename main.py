tugas_list = []
def todo_menu():
    print("\n====== TO DO LIST =====")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Update Tugas")
    print("4. Hapus Tugas")
    print("5. Keluar")
    print("=======================")

def tambah_tugas():
    tugas = input("Masukkan Tugas : ")
    tugas_list.append(tugas)
    print("Tugas Berhasil Ditambah, Ayo Kita Lihat Tugasnya")

def lihat_tugas():
    if len(tugas_list) == 0:
        print("❌ Tidak Ada Yang Bisa Dilihat, Ayo Tambahkan Terlebih Dahulu")
    else: 
        for i in range(len(tugas_list)):
            print(f"{i+1}. {tugas_list[i]}") 
    
def update_tugas():
        lihat_tugas()

        update = int(input("Kamu Mau Ubah Yang mana nih? : "))
        if 1 <= update <= len(tugas_list):
            update_list = input("Mau Di Ganti Apa? : ")
            tugas_list[update - 1] = update_list

            print("Berhasil Di ubah")
        else:
            print("Pilih Yang Ada Di Atas Aja Yaa!!")


def hapus_tugas():
   if len(tugas_list) > 0: 
        lihat_tugas()

        hapus = int(input("Yang Mana Yang Mau Kamu Hapus Nih? : "))
        tugas_list.pop(hapus - 1)
        print("Tugas Berhasil Dihapus")

   else:
        print("❌ Tidak Ada Yang Bisa Dihapus, Ayo Tambahkan Terlebih Dahulu")


while True:
    todo_menu()
    menu = input("Masukkan Pilihan : ")
    if menu == "1":
        tambah_tugas()
    elif menu == "2":
        lihat_tugas()
    elif menu == "3":
        update_tugas()
    elif menu == "4":
        hapus_tugas()
    elif menu == "5":
        print("Terimakasih Sudah Menggunakan TODO LIST INI 🤍 !! ")
        break
    elif menu == "":
        print("Pilihan Tidak Boleh Kosong")
    else: 
        print("Tidak Ada Menu itu Silahkan Pilih Yang Ada Diatas 💢 !!")


