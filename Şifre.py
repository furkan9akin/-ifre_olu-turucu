import random
x="+-/*!&$#?=@"
y="abcdefghijklnopqrstuvwxyz"
z="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t="1234567890"
par_u=int(input("Parola uzunluğunu giriniz: "))
par=""
i=0;
while i<par_u:
    par+=x[random.randint(0,len(x)-1)]
    x=y
    y=z
    z=t
    t="+-/*!&$#?=@"
    i+=1
    if i%4==0:
        x="+-/*!&$#?=@"
        y="abcdefghijklnopqrstuvwxyz"
        z="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        t="1234567890"
print("Şifreniz: ",par)