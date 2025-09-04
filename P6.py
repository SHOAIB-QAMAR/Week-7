# Consider two files having some lines of statements. Write a Python program to swap
# content present at middle line of first file with the content of last line of the second
# file. (Note: First file contains odd numbers of lines of statement)

file1_path = "Files_Swap/file1.txt"
file2_path = "Files_Swap/file2.txt"

with open(file1_path, "r") as f1:
    lines1 = f1.readlines()

with open(file2_path, "r") as f2:
    lines2 = f2.readlines()

middle_index1 = len(lines1) // 2 

last_index2 = len(lines2) - 1

lines1[middle_index1], lines2[last_index2] = lines2[last_index2], lines1[middle_index1]

with open(file1_path, "w") as f1:
    f1.writelines(lines1)

with open(file2_path, "w") as f2:
    f2.writelines(lines2)

print("Lines swapped successfully!")