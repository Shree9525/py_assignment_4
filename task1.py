try:
    file = open('file.txt', 'r')
    reading_line1= file.readline()
    reading_line2= file.readline()
    print("Reading file content:")
    print("Line 1: ", reading_line1)
    print("Line 2: ", reading_line2)
    file.close()
except FileNotFoundError:
    print("The file 'file.txt' was not found.")