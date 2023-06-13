import add
if __name__ == '__main__':
	f = open("file.txt", "w")
	add.parse(f)
	f.close()