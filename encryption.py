from prime_artihmetic import findMultiplicativeInverse,  genRelativePrime


def getPublicKey(totient, lower):
    return genRelativePrime(totient, lower)

def getPrivateKey(pubKey, totient):
    inv =  findMultiplicativeInverse(pubKey, totient)
    if inv == 1:
        raise Exception("Unable to create private Key")
    return inv
    

def encrypt(message, e, n) -> int:
    
    return (message ** e) % n

def decrypt(encrypted, d, n) -> int:
    
    return (encrypted ** d) % n