n = int(input("please enter one big prime number say n = "))
g = int(input("please enter another big prime number say g = "))
x = int(input("please enter one any random number say x = "))
A = pow(g,x)%n
y = int(input("Please choose another random number say y = "))
B = pow(g,y)%n
k1 = pow(B,x)%n 
k2 = pow(A,y)%n
print("k1 value = ",k1,"k2 value = ",k2)