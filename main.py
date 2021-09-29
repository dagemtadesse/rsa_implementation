from encryption import decrypt, encrypt, getPrivateKey, getPublicKey
from prime_artihmetic import genPrime


def main():

    message = "My Super Secret message."

    numbered = []

    for char in message:
        numbered.append(ord(char))

    size = max(numbered)

    q = genPrime(size, size + 100)
    p = genPrime(q + 1, q + 100)

    print("p = {}, q = {}".format(p, q))

    n = p * q
    totient = (p - 1) * (q - 1)

    pubKey = getPublicKey(totient, 0)
    privKey = getPrivateKey(pubKey, totient)


    print("public Key = {}\nprivate Key = {}".format(pubKey, privKey))


    encrypted = [ encrypt(i, pubKey, n) for i in numbered ]

    
    decryptedNum = [decrypt(i, privKey, n) for i in encrypted  ]
    decrypted = ""


    for asci in decryptedNum :
        decrypted += chr(asci)

    print("encrypted = {0}\ndecrypted = {1}".format(encrypted, decrypted))


if __name__ == "__main__":
    main()
