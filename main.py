from encryption import decrypt, encrypt, getPrivateKey, getPublicKey
from prime_artihmetic import genPrime


def main():

    message = "A"

    numbered = ""

    for char in message:
        numbered += "{}".format(ord(char))
    numbered = int(numbered)

    q = genPrime(numbered, numbered + 100)
    p = genPrime(q + 1, q + 100)

    print("p = {}, q = {}".format(p, q))

    n = p * q
    totient = (p - 1) * (q - 1)

    pubKey = getPublicKey(totient, 0)
    privKey = getPrivateKey(pubKey, totient)


    print("public Key = {}\nprivate Key = {}".format(pubKey, privKey))


    encrypted = encrypt(numbered, pubKey, n)

    
    decryptedNum = decrypt(encrypted, privKey, n)
    decrypted = ""


    while decryptedNum > 0:
        decrypted += chr(int(decryptedNum % 100))
        decryptedNum /= 100


    print("encrypted = {0}\ndecrypted = {1}".format(encrypted, decrypted))


if __name__ == "__main__":
    main()
