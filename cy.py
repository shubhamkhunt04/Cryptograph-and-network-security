# Conver string into cipher text
str1 = input("Enter a string :\n")
key = int(input("Enter the size of key :\n"))
for i in str1:
    if(i.islower()):
        print(chr((ord(i)+key-97)%26+97),end="")
    else:
        print(chr((ord(i)+key-65)%26+65),end="")