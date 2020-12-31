def decriptrd(string,shift):
    ciper=''
    for char in string:
        if  char.isupper():
            ciper=ciper+chr((ord(char)-shift-65)%26+65)
    return ciper
text=input("enter the text")
s=int(input("enter the shift key"))
print("the dcripted string :",decriptrd(text,s))