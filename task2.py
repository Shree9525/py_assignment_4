write_data = input("Enter text to write to the file: ")
file = open("output.txt", "w")
writing = file.write(write_data)
print("Data successfully written to output.txt.")
file.close

append_data = input("Enter additional text to append: ")
file = open("output.txt", "a")
appending = file.write("\n"+append_data)
print("Data successfully appended.")
file.close()

print("Final content of output.txt: ")
file = open("output.txt", "r")
reading = file.read()
print(reading)
file.close()