p = 7
q = 17
def rsaEnc(msg) :
	L = (p-1)*(q-1)
	e = 5
	f=0
	i=0
	while f!=1 :
		 f = (i*5)%L
		 i = i+1
	print ("Decryption key = ",i-1)
	N = p*q
	ct = pow(msg,e)%N
	print ("cipher text = ",ct)	
	return ct,i
def rsaDec(ct,d) :
	N = p*q
	pt = pow(ct,d)%N
	print ("plain text value is = ",pt)
plainText = input("please enter a message value =  ")
ct,d = rsaEnc(int(plainText))
rsaDec(ct,d-1)

