# ASSIGMENT-4
Task-1

try:
    file_1=open('simple.txt', 'r')
    print(file_1.read())
except FileNotFoundError:
    print("Error: The file 'simple.txt' was not found")
finally:
   print('okk')

Task-2
file_1=open("output.txt","r+")
write_file=file_1.write("this is an output file to get more detail about the error")
print(write_file)
file_1.close()
