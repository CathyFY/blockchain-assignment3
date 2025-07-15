import random

from params import p
from params import g

def keygen():
    sk = random.randint(1, p - 1) 
    pk = pow(g, sk, p)
    return pk,sk


def encrypt(pk,m):
    q = (p - 1) // 2
    r = random.randint(1, q)
    c1 = pow(g, r, p)
    c2 = (pow(pk, r, p) * m) % p
    return [c1,c2]


def decrypt(sk,c):
    c1, c2 = c
    s = pow(c1, sk, p)
    s_inv = modular_inverse(s, p)
    m = (c2 * s_inv) % p
    return m


def modular_inverse(a, m):
    """
    Calculates the modular inverse of 'a' modulo 'm'.
    There is no need to update this function.
    """
    return pow(a, -1, m)

