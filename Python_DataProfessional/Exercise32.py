#Functions

#Fungsi pertama
def contoh_fungsi():
    print("Halo Dunia")
    print("Aku sedang belajar bahasa python")

contoh_fungsi()

# Fungsi Kedua
def fungsi_dengan_argumen(nama_depan, nama_belakang):
    print(nama_depan + " " + nama_belakang)
fungsi_dengan_argumen("John", "Doe")

#Fungsi ketiga
def fungsi_dengan_argumen(nama_depan, nama_belakang = " "):
	print(nama_depan + " " + nama_belakang)
fungsi_dengan_argumen("John")
fungsi_dengan_argumen("John", "Doe")