#k = int(input("please enter a key value = "))
k = 15
p = input("please enter a word to encrypt : ")
p = p.upper()
f = list(p)
enc = []
for i in f :
    ac = ord(i)-65
    c = (ac*k)%26
    enc.append(c)
# print(enc)
length1 = range(len(enc))
print("The cipher text is ",end="")
for a in length1 :
    v = enc[a]
    print(chr(v+65),end="")
print("")
j = 0
h = 0
while h!=1 :
    h = (j*k)%26
    j = j+1
ki = j-1
dec = []
for l in enc :
    p = (l*ki)%26
    dec.append(p)
#print(dec)
print("The text is ",end = "")
length = range(len(dec))
for b in length :
    v = dec[b]
    print(chr(v+65),end="")
print("")