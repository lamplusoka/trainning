#!/usr/bin/python3
file_name = "/mnt/c/users/lamplus/documents/github/trainning/python3/test_library.txt"
file = open(file_name, 'w')
file.write("dd")
file.close()
file = open(file_name)
data = file.read()
print(data)