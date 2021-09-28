from encryption import decrypt, encrypt, getPrivateKey, getPublicKey
from prime_artihmetic import genPrime


def main():
    q = genPrime(3, 5)
    p = genPrime(q + 1, q + 6)

    print("p = {}, q = {}".format(p, q))

    n = p * q
    totient = (p - 1) * (q - 1)

    pubKey = getPublicKey(totient, 0)
    privKey = getPrivateKey(pubKey, totient)


    print("public Key = {}\nprivate Key = {}".format(pubKey, privKey))

    message = 12

    encrypted = encrypt(message, pubKey, n)
    decrypted = decrypt(encrypted, privKey, n)

    print("encrypted = {0}\ndecrypted = {1}".format(encrypted, decrypted))


if __name__ == "__main__":
    main()
