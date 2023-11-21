#Blind Sign Authentication

import random

print("Aditi Patra 21BIT0125")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

m = int(input("Enter your message: "))

p = int(input("Enter first prime number: "))
while not is_prime(p):
    print("The number entered is not prime. Please enter a prime number.")
    p = int(input("Enter first prime number: "))

q = int(input("Enter second prime number: "))
while not is_prime(q):
    print("The number entered is not prime. Please enter a prime number.")
    q = int(input("Enter second prime number: "))

#-------------------Key Generation-----------------------------------
phi = (p-1) * (q-1)
print("Φ = ", phi)
N = p * q
print("N = ", N)

# Selection of e
e = random.randint(2, phi - 1)
while gcd(e, phi) != 1: #Check if e and phi are coprime
    e = random.randint(2, phi - 1)

print("Selected e = ", e)

# Private Key
def modular_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

d = modular_inverse(e, phi)  # Calculate the modular multiplicative inverse of e modulo phi
print("Process d = ", d)
#----------------------------------------------------------------------

#---------------------Encryption----------------------------------------
r = random.randint(2, N-1)  # Generate a random value for r between 2 and N-1
while gcd(r, N) != 1:  # Check if r and N are coprime
    r = random.randint(2, N-1)
print("r = ", r)

#Blind Factor
bf = pow(r, e, N)
print("Blind Factor = ", bf)

#Blind Message
bm = (pow(r, e, N) * m) % N
print("Blind Message = ", bm)
#-----------------------------------------------------------------------

#---------------------Sign Generation-----------------------------------
sg = pow(bm, d, N) #Sign Generated
print("Sign Generated = ", sg)
#-----------------------------------------------------------------------

#---------------------Sign Verification---------------------------------
sv = pow(r, -1, N)
print("Sign Verified = ", sv)
bdm = (sg * sv) % N #Blinded Message
print("Blinded Message = ", bdm)
fm = pow(bdm, e, N)
print("The Computed Message = ", fm)
#-----------------------------------------------------------------------

#--------------------------Verification of the Code---------------------
if fm == m:
    print("The process is correct as the computed message is the same as the original Message")
else:
    print("The process is incorrect as the computed message is not the same as the original Message")

#-----------------------------------------------------------------------
