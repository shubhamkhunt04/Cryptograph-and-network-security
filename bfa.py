# Brut force attack.
print("**************************************************")
str1 = input("Enter a message :\n")
print("**************************************************")
#key = int(input("Enter the size of key :\n"))
for key in range(0,27):
    print(f"\n====================Shift {key}====================\n")
    for i in range(len(str1)):
        if(str1[i]== " "):
            print(" ",end=" ")
        elif(str1[i].islower()):
            print(chr((ord(str1[i])+key-97)%26+97),end="")
        else:
            print(chr((ord(str1[i])+key-65)%26+65),end="")
    print()  #for new line