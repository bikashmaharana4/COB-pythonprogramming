"""Q1 . Write a Program to read a text file and find all unique words and how
 many times the word occurrences."""



# Entering The Name Of The File 
file_name = input("Enter File Name : ")
print("Generating Result ..... ")
# To Cheack The Existance of The File
try:
    open_file = open('bikashmahrana.txt','r')
except:
    print("This File Doesn't Exist At This Location")

# For Reading File
lines = open_file.read()
# For Getting Every Word
words = lines.split()
# Creating A Dictionary
word_counts = dict()

# Counting  Words Occurance
for word in words:
    word_counts[word] = word_counts.get(word,0) + 1

# printing The Key And Values Separately

# For Unique Words
all_greater_than_one = all(value > 1 for value in word_counts.values())
if all_greater_than_one:
    print("There are No Unique Words.")
else:
    print("Unique Words Are  : ",end="  ")
    for key in word_counts:
        if word_counts[key] == 1:
            print(key, end=", ")

print()
# For Occurance Words
print("Frequency Or Occurance Of Words" )
for key in word_counts:
    print(f'{key} : {word_counts[key]}')
