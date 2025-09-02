#Task 1: Read a File and Handle Errors

try:
    file1 = open('sample.txt', 'r+')
    read_file = file1.read()
    print(read_file)
    file1.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")


# Task 2: Write and Append Data to a File

write_file = open('output.txt','r+')
user_input = input('Enter text to write to the file: ')
read_file1 = write_file.write(user_input)
print(read_file1)
if read_file1 > 1:
    print('Data successfully written to output.txt')
write_file.close()


file1= open('output.txt','a')
user_input2 = input('Enter additional text to append: ')
append_file = file1.write('\n' + user_input2)
print(append_file)
if append_file > 1:
    print('Data successfully appended')
file1.close()


file2= open('output.txt','r')
read_file2 = file2.read()
print('Final contents of output.txt: \n', read_file2)
file2.close()
