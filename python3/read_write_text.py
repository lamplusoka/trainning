#!/usr/bin/python3
import sys
args = sys.argv
file_name = file_name = "/mnt/c/users/lamplus/documents/github/trainning/python3/test_library.txt"
file = open(file_name, "w")
file.write(args[1] + " " + args[2])

file = open(file_name)
data = file.read()
print(data)
file.close