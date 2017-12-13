def option():
	print("Pilih salah satu dari tiga fungsionalitas berkut: ")
	print("1. Menyimpan biodata")
	print("2. Tampilkan semua biodata")
	print("3. Keluar program")
	pilihan=int(input("Masukan pilihan anda: "))
	return pilihan

nama=str(input("Masukan nama: "))
asal=str(input("Masukan Asal Daerah: "))
tanggal=str(input("Masukan Tanggal Lahir: "))

pilihan=True
while(pilihan<3):
	pilihan=option()
	if (pilihan==1):
		file= open("modul7.txt","a+")
		data= file.write("Nama: %s \n"%(nama))
		file= open("modul7.txt","a+")
		data= file.write("Asal Daerah: %s \n"%(asal))
		file= open("modul7.txt","a+")
		data= file.write("Tanggal Lahir: %s \n"%(tanggal))
		print("==Menyimpan Biodata==")
	elif(pilihan==2):
		file= open("modul7.txt","r")
		print("== Menampilkan Biodata ==")
		print(file.read())
	else:
		print("Bye Bye")