for i in range(1,101):
	if i%7!=0:
		continue
	elif str(i).find("7") is -1:
		print(i)
