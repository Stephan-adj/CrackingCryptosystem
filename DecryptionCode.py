#####Rabin's method
#Public keys
n = 64952073097727989
c = 61024756279786677 

#n = 6189500738854313
#c = 3395792081244847 


B = 3
B2 = B*B

###### POllARD p-1 algorithm
facto = 2
for d in range(2, 51):
    facto = (facto ** d) % n
print("2^50! (mod n)= ",facto)
print("n = ",n)

##### Compute the GCD of a and b
def GCD(a,b) :
    assert (a > 0) and (b > 0)
    if a < b:
        a, b = b, a                   # We swap a and b, assuming a >= b
    a0, b0 = a, b                     # We keep the original value
    # Continue until the remainder is 0. 
    while b != 0:
        # We replace a and b and b by the remainder of the division 
        a, b = b, a % b

    print('The GCD of', a0, 'and', b0, 'is equal to ', a)
    # Verifications
    print(a0 // a, '×', a, '=', (a0 // a * a))
    print(b0 // a, '×', a, '=', (b0 // a * a))
    return a
q=GCD(n, facto-1)    
p=n//q
print("q*p = ", q*p, '=', n)
print(q, '×', p, '=', n)

#give the bézout coefficient
def extended_gcd(a, b):
    s = 0   
    old_s = 1
    r = b  
    old_r = a
         
    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
    
    if b != 0:
        bezout_t = (old_r - old_s * a)// b
    else:
        bezout_t = 0

    return (old_s, bezout_t) #Bézout coefficients + greatest common divisor
def fastpow1(x, y):
    """Fast exponentiation x**y with x and y some integers (modulo p)
    """
    result = 1
    while y>0:
        if y%2!=0: # y odd
            result = (result*x) % p
        x = (x*x) % p 
        y //= 2 
    return result
def fastpow2(x, y):
    """Fast exponentiation x**y with x and y some integers (modulo q)
    """
    result = 1
    while y>0:
        if y%2!=0: # y odd
            result = (result*x) % q
        x = (x*x) % q
        y //= 2 
    return result

#solving u²+3u=C[p]
#inverse of 4 (mod p):
INV_4=fastpow1(4,p-2)
d=(c+INV_4*B2) % p
print("d = C+4^-1*B² =         ", d)
k=(p+1)/4
print("k = (p+1)/4 =", k)
y1=fastpow1(d,k)
#-y=p-y[p]
y2=p-y1

#Verification
print("y1 = d^k (mod p) =", y1)
print("y1² =                   ", (y1*y1)%p)
print("y2 = p-y1 (mod p) =", y2)
print("y2² =                   ", (y2*y2)%p)

#from (u+2^-1B)²=y² [p] we deduce :
#inverse of 2 (mod q):
INV_2=fastpow1(2,p-2)
u1=y1-(INV_2*B)
print("u1 = y1-2^-1*B =", u1)
u2=y2-(INV_2*B)
print("u2 = y2-2^-1*B =", u2)

#Verification
temp = (u1*u1 + 3*u1)%p
print("u1*u1 + 3*u1 (mod p) =", temp)
temp = (u2*u2 + 3*u2)%p
print("u2*u2 + 3*u2 (mod p) =", temp)
print("C [p]=                ", c%p)

#######################
#solving v²+3v=C[q]
#inverse of 4 (mod q):
INV_4=fastpow2(4,q-2)
d=(c+INV_4*B2) % q
print("d =               ", d)
k=(q+1)/4
print("k = ", k)
y3=fastpow2(d,k)
y4=q-y3

#Verification
print("y3 = ", y3)
print("y3² =             ", (y3*y3)%q)
print("y4 = ", y4)
print("y4² =             ", (y4*y4)%q)

#inverse of 2 (mod q):
INV_2=fastpow2(2,q-2)
v1=y3-(INV_2*B)
print("v1 = ", v1)
v2=y4-(INV_2*B)
print("v2 = ", v2)

#Verification
temp = (v1*v1 + 3*v1)%q
print("v1*v1 + 3*v1 (mod q) =", temp)
temp = (v2*v2 + 3*v2)%q
print("v2*v2 + 3*v2 (mod q) =", temp)
print("C [q]=                ", c%q)

#############################
#Extented Euclidean algorithm
(b, a) = extended_gcd(p,q)
print("bézou1 =", a)
print("bézou2 =", b)
print("verif =", b*p+a*q)
a=a*q
b=b*p
print("bézou1 =", a)
print("bézou2 =", b)

#################################
#Finally we compute the solutions
x1=(a*u1+v1*b)%n
print("x1 =", x1)
x2=(a*u1+v2*b)%n
print("x2 =", x2)
x3=(a*u2+v1*b)%n
print("x3 =", x3)
x4=(a*u2+v2*b)%n
print("x4 =", x4)

#Binary conversion
"""
maliste = [x1,x2,x3,x4]
def conversion(n):
    if n > 1:
        conversion(n // 2)
    print(n % 2, end='')
for i in range(0, 4):
    conversion(maliste[i])
    print("")
"""  
#### Word conversion
solution = [x1, x2, x3, x4]
alphabet = ['', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I','J', 'K', 'L','M', 'N', 'O','P', 'Q', 'R','S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
def affichage(x):
    word = str(x)
    if len(word)%2!=0:
        word = '0' + word
    for i in range(0, len(word)-1, 2):
        if 0 < int(word[i])*10+int(word[i+1]) < 26:
            print(alphabet[int(word[i])*10+int(word[i+1])], end='')
        else : 
            print(alphabet[int(word[i])], end='')   
            print(alphabet[int(word[i+1])], end='')  
    print('')        
for k in range(0,4):   
    affichage(solution[k])


############## Experimental ElGamal cryptosystem
def fastpow(x, y):
    #Fast exponentiation x**y with x and y some integers 
    result = 1
    while y>0:
        if y%2!=0: # y odd
            result = (result*x) % p
        x = (x*x) % p 
        y //= 2 
    return result

p = 123456791
r = 17
x = 151475409
Tokenk = 55558888
M = 66669999
y=fastpow(r,x)
print(type(y))
print("My public key y = r^x (mod p)= ",y)
KeyK=fastpow(y,Tokenk)
print("Key : K = y^k (mod p) = ",KeyK)
C1=fastpow(r,Tokenk)
print("C1 = r^k (mod p) = ",C1)
C2=(KeyK*M)%p
print("C2 = K*M (mod p) = ",C2)
verifkey=fastpow(C1,x)
print("We can verify by computing the key : C1^x (mod p) = " , verifkey)
K_Inv=fastpow(KeyK,(p-2)) #because p is prime the inverse is just K^p-2 (mod p)
print("Computing the inverse of K, K_Inv = ",K_Inv)
decoding=(K_Inv*C2)%p
print("And finally decrypt the message : M = K^-1*C2 (mod p) = ",decoding)

def inverse(a, n):
    t = 0     
    newt = 1  
    r = n     
    newr = a    
    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt) 
        (r, newr) = (newr, r - quotient * newr)
    if r > 1 : 
        return "a is not invertible"
    if t < 0 : 
        t = t + n
    return t
print(inverse(KeyK,p))

