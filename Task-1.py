
try:
    file_1=open('simple.txt', 'r')
    print(file_1.read())
except FileNotFoundError:
    print("Error: The file 'simple.txt' was not found")
finally:
   print('okk')