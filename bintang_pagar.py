for i in (range(6,0,-1)):
	for j in (range(0,i-1)):
		if(i%2)==1 :
			print("#", end=" ")
		else:
			print("*", end=" ")
	print()
	