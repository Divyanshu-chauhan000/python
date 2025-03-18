# file = open("File_inp_opt/abc.txt")
# data = file.read()
# print(data)
# file.close()


# readlines

# file = open("File_inp_opt/abc.txt")
# line = file.readlines()
# print(line, type(line))
# file.close()

#  Readline

file= open("File_inp_opt/abc.txt")
line1 = file.readline()
print(line1, type(line1))

line2 = file.readline()
print(line2, type(line2))

line3 = file.readline()
print(line3, type(line3))

file.close()