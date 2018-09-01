
# Write a python program to take list of numbers as input and to return a tuple of first and last numbers in the list
values=input("enter 5 values:")
mylist=values.split(",")
first_value=mylist[0]
last_value=mylist[-1]
mytuple=(first_value, last_value)
print(mytuple)

# Write a python program to count number of words and characters in a file and the print the output
fileName=input("enter file name:")
infile=open(fileName, 'r')
line=infile.readline()
while line!="":
    for x in line:
        word_count =len(line.split(" "))
    print(" words:", word_count)
    for y in line:
        char_count=len(line)-line.count(' ')
    print("Characters:", char_count)
    line=infile.readline()

# Write a python program to print first letter of name using star symbols
# printing letter A using symbols
def Print_Symbol(n):
    # Outer for loop for number of lines
    for lines in range(n):
        for in_index in range((n // 2) + 1):
            if ((in_index == 0 or in_index == n // 2) and lines != 0 or
                    lines == 0 and in_index != 0 and in_index != n // 2 or
                    lines == n // 2):
                print("*", end="")
            else:
                print(" ", end="")

        print()


Print_Symbol(4)






