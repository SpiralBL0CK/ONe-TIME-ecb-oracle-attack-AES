import string
import requests
from numba import jit
from concurrent import futures


"""def f():
    plaintext = ""
    blocksize = 16

    # The flag occupies 2 blocks
    for k in range(2):
        b = ""
        for i in range(1,17):
            string_sent = "a".encode("utf-8").hex()*(16-i)
    
            x = string_sent 
            if(i == 16):
                break
            r = requests.get("http://aes.cryptohack.org/ecb_oracle/encrypt/{}".format(x))
            g1 = r.text[15:-3]
            print(g1)

            g1 = g1[:32+k*32]
            print(r.text)
            print(g1)

            print("String sent: " + x )
            for j in range(256):
               
                    #print(s)
                x  = requests.get("http://aes.cryptohack.org/ecb_oracle/encrypt/{}".format((string_sent + plaintext.encode("utf-8").hex() + b.encode("utf-8").hex() + chr(j).encode("utf-8").hex())))
                g2 = x.text[15:-3]
                g2 = g2[:32+k*32]
                if g1 == g2 and chr(j) in string.printable and j!=10 and j!=0:
                    print (chr(j), j)
                    b += chr(j)
                    break
        plaintext += b
    print(plaintext)
"""

if __name__ == '__main__':
    for i in range(2):
        pad = 'A'*31
        key = ''

        for i in range(32):
            c = 0
            target = requests.get("http://aes.cryptohack.org/ecb_oracle/encrypt/{}".format(pad.encode('utf-8').hex()))
            target =  target.text[15:-3][32:64] 

            for c in range(32, 128):
                x = requests.get("http://aes.cryptohack.org/ecb_oracle/encrypt/{}".format(pad.encode('utf-8').hex() + key.encode('utf-8').hex() + chr(c).encode('utf-8').hex()))
                x = x.text[15:-3][32:64] 
                if (target == x):
        #            print(c)
                    key += chr(c)
                    break
            print(pad)
            pad = pad[1:]
        print(key)


#f()