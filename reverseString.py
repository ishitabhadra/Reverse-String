string = input("Enter a string to reverse: ")

list = []

for char in string:
  list.insert(0,char)

word = ''.join(list)


print("Reversed string is",word)

#To check if the word is a palindrome

# if string == word:
#   print("yes it is a palindrome")
# else:
#   print("no, not a palindrome")
