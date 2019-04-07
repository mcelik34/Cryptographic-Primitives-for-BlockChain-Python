import random
import hashlib

"""
Programmed by Muhammet Çelik (mcelik - 20418) and Kemal Sarper Yücel(syucel - 21031)
"""

def PoW(plen, q, p, g, fname):
    file = open(fname, "r")
    lines = file.readlines()
    m = ""
    for i in range(len(lines)):
        m += lines[i] + "\n"
    file.close()

    nonce = random.randrange(0, pow(2,128))
    ptext = m + "\nNonce: " + str(nonce)
    h_obj = hashlib.sha3_256(ptext.encode('UTF-8')).hexdigest()
    while h_obj[0:plen] != "0"*plen:
        nonce += 1
        ptext = m + "\nNonce: " + str(nonce)
        h_obj = hashlib.sha3_256(ptext.encode('UTF-8')).hexdigest()
    return ptext
