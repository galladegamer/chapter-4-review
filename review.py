# pylint:disable=missing-final-newline
# pylint:disable=missing-module-docstring
# pylint:disable=invalid-name
# pylint:disable=consider-using-f-string


# CHAPTER 4 REVIEW


# If your string length is 9 characters long, the character count is: 0, 1, 2, 3, 4, 5, 6, 7, 8
# 13 Characters, count: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

text = "Good Morning!"
print(len(text))

# Subscript operator []
# text[0]: G
# text[7]: r
# text[-1]: !
# text[-3]: n
# text[-13]: G
# check length: len(text) Length function

print(text[0], text[7], text[-1], text[-3], text[-13])

# SLICING STRINGS

# [num:num]

name = "myFile.txt"

# name[0:]: myFile.txt
# name[0:1]: m
# name[:len(name)]: myFile.txt
# name[0:2]: my
# name[0:5]: myFil
# name[-3:]: txt

print(name[0:], name[0:1], name[:len(name)], name[0:2], name[0:5], name[-3:])

# 4-1d Testing for Substring with the in Operator
fileList = ["myFile.txt", "myProgram.exe",
            "myImage.png", "yourVideo.mp4", "yourFile.txt", ]
for fileName in fileList:
    if ".txt" in fileName:
        print(fileName)

print("CEASER CIPHER")
print()

# KEYS OF 0, 1, 2, 3, 4, 5

# abcdefghijklmnopqrstuvwxyz     0
# bcdefghijklmnopqrstuvwxyza     1
# cdefghijklmnopqrstuvwxyzab     2
# defghijklmnopqrstuvwxyzabc     3
# efghijklmnopqrstuvwxyzabcd     4
# fghijklmnopqrstuvwxyzabcde     5

print("ENCRYPTING")
plaintext = input("Enter the plaintext: ")
key = int(input("Enter the distance value: "))
code = ""
caps=0
for ch in plaintext:
    if ord(ch)>=ord("A") and ord(ch)<=ord("Z"):
        ch = ch.lower()
        caps=1
    else:
        caps=0
    if ch.isalpha():
        ordVal = ord(ch)
        cipherVal = ordVal+key
        while cipherVal > ord("z"):
            cipherVal -= 26
        ench = chr(cipherVal)
        if caps==1:
            ench=ench.upper()
        code += ench
    else:
        code += ch
print("PLAINTEXT:", plaintext)
print("CODE:     ", code)

print()

print("DECRYPTING")
code = input("Enter the code: ")
key = int(input("Enter the distance value: "))
plaintext = ""
caps=0
for ch in code:
    if ord(ch)>=ord("A") and ord(ch)<=ord("Z"):
        ch = ch.lower()
        caps=1
    else:
        caps=0
    if ch.isalpha():
        ordVal = ord(ch)
        cipherVal = ordVal-key
        while cipherVal < ord("a"):
            cipherVal += 26
        ench = chr(cipherVal)
        if caps==1:
            ench=ench.upper()
        plaintext += ench
    else:
        plaintext += ch
print("CODE:     ", code)
print("PLAINTEXT:", plaintext)
print(ord("a"))
print(ord("z"))

# DECIMAL, BINARY, OCTAL, HEXADECIMAL

# DECIMAL:     0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# BINARY:      0, 1
# OCTAL:       0, 1, 2, 3, 4, 5, 6, 7
# HEXADECIMAL: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

# BINARY TO DECIMAL
print("BINARY TO DECIMAL")
binary=input("Enter the bitstring: ")
exponent=len(binary)-1
decimal=0
for a in binary:
    b=2**exponent
    c=int(a)
    d=c*b
    decimal+=d
    exponent-=1
print("BINARY:     ", binary)
print("DECIMAL:    ", decimal)

#DECIMAL TO BINARY
print()
print("DECIMAL TO BINARY")
decimal=int(input("Enter a number: "))
if decimal == 0:
    print("DECIMAL:    ", 0)
    print("BINARY:     ", 0)
else:
    print("%-5s%15s%12s"%("QUOTIENT", "REMAINDER", "BINARY"))
    bitstring = ""
    b=decimal
    e=""
    while b>0:
        a=b%2
        a=str(a)
        b//=2
        bitstring=a+bitstring
        e+=a
        print("%-5s%14s%16s"%(b, a, bitstring))
    print()
    print("DECIMAL:    ", decimal)
    print("BINARY:     ", bitstring)

#OCTAL TO BINARY
print()
print("OCTAL TO BINARY")
octal=input("Enter the octal number: ")
bitstring=""
error=0
for a in octal:
    if a=="0":
        b="000"
    elif a=="1":
        b="001"
    elif a=="2":
        b="010"
    elif a=="3":
        b="011"
    elif a=="4":
        b="100"
    elif a=="5":
        b="101"
    elif a=="6":
        b="110"
    elif a=="7":
        b="111"
    else:
        print("ERROR")
        error=1
        b="0"
        break
    bitstring+=b
if error==0:
    print("OCTAL:      ", octal)
    print("BINARY:     ", bitstring)

#HEX TO BINARY
print()
print("HEXADECIMAL TO BINARY")
hexnum=input("Enter the hexadecimal number: ")
hexnum=hexnum.lower()
bitstring=""
error=0
for a in hexnum:
    if a=="0":
        b="0000"
    elif a=="1":
        b="0001"
    elif a=="2":
        b="0010"
    elif a=="3":
        b="0011"
    elif a=="4":
        b="0100"
    elif a=="5":
        b="0101"
    elif a=="6":
        b="0110"
    elif a=="7":
        b="0111"
    elif a=="8":
        b="1000"
    elif a=="9":
        b="1001"
    elif a=="a":
        b="1010"
    elif a=="b":
        b="1011"
    elif a=="c":
        b="1100"
    elif a=="d":
        b="1101"
    elif a=="e":
        b="1110"
    elif a=="f":
        b="1111"
    else:
        print("ERROR")
        error=1
        b="0"
        break
    bitstring+=b
if error==0:
    print("HEXADECIMAL:", hexnum)
    print("BINARY:     ", bitstring)