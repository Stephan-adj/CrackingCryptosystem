# CrackingCryptosystem
A short code to crack Experimental ElGamal cryptosystem and Rabin’s method.


Experimental ElGamal cryptosystem
We use the private key x = 151475409.
Hence, we have to calculate
y = r^x mod(p) = 17^151475409 mod(123456791).
Using repeated squaring or Maple, we find y = 113365384.
Alice’s encryption key becomes
K = y^k mod(p) = 113365384^55558888 mod(123456791) = 114304867.
The ciphertext is (C1,C2) with
C1 = r^k mod(p) = 17^55558888 mod(123456791) = 80432542
and
C2 = KM mod(p) = 114304867*66669999 mod(123456791) = 5836150
On receipt of the (C1,C2) I calculate the key
K = C1^x mod(p) = 80432542^151475409 mod(123456791) = 114304867.
Using the Euclidean algorithm or Maple, I invert K:
GCD(K,p) = g = 1 = 123456791*-21439672 + 114304867*23156259
Thus the inverse of K mod(p) is
K^(-1) = 23156259
I finally decipher the message as
K^(-1)*C2 mod(p) = 23156259*5836150 mod(123456791) = 66669999




Crack Rabin’s method with Pollard’s p-1 algorithm
We are trying to solve the equation
x (x + B) = C mod n
where C = 61024756279786677, B = 3 and n = 64952073097727989.
We factorise n=p*q using A = 2^(50!) mod(n) = 2858136211135948
to find p = GCD(A-1,n) = 548229151 and q = n/p = 118476139.
Applying the generalised GCD algorithm we find the decomposition
GCD(p,q) = g = 1 = -78699994*118476139 + (17007617)*548229151
1 = (a) + (b) = -9324071428443166 + (9324071428443167)
We are looking for
u^2 = C mod(p) = 5557479
v^2 = C mod(q) = 20076559
This can be found as both p mod 4 = 3 and q mod 4 = 3.
Thus we can write p=4k-1, q=4j-1 with
k = (p+1)/4 = 137057288
j = (q+1)/4 = 29619035
We then calculate
dp = (C + 4^(-1) B^2) mod p = 142614769
dq = (C + 4^(-1) B^2) mod q = 49695596
taking into account that 4^(-1) denotes the multiplicative
inverse mod p and mod q, respectively.
Hence, we arrive at
yp = dp^k mod(p) = +/- 117781113
yq = dq^j mod(q) = +/- 83116900
and consequently
u1 = (yp - 2^(-1) B) mod p = 391895687
u2 = (-yp - 2^(-1) B) mod p = 156333461
v1 = (yq - 2^(-1) B) mod q = 23878829
v2 = (-yq - 2^(-1) B) mod q = 94597307
where, again, 2^(-1) denotes the multiplicative
inverse mod p and mod q, respectively.
With the Chinese remainder theorem we combine the previous results to
x = a*u + b*v mod(n).
We list the four solutions, only one has valid character values
17758893088464830
64952071296707072
1801020914 (rabin)
47193180009263156
