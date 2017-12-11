nama= str(input("Masukan Nama: "))
asal= str(input("Masukan Asal: "))
tanggal= str(input("Masukan Tanggal: "))

file= open("biodata.txt","a+")
result= file.write("Nama Saya Adalah %s \n"%(nama))
print(result)

file= open("biodata.txt","a+")
result= file.write("Saya Berasal dari %s \n"%(asal))
print(result)

file= open("biodata.txt","a+")
result= file.write("Saya Lahir Pada %s \n"%(tanggal))
print(result)

file= open("biodata.txt","r")
for data in file:
	print(data)
