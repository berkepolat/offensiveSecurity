import argparse
import subprocess
import sys
import hashlib
import time
from re import match

class Error(Exception):
    """Base class for errors"""
    pass
class HashNotValid(Error):
    """Given hash is not valid"""
    pass
def decrypt(hash,wl):
    line=0
    if len(hash)==32: #MD5
        while True:
            try:
                nextHash = hashlib.md5(wl[line][:len(wl[line])-2]).hexdigest()
                word = wl[line][:len(wl[line])-2]
                if nextHash == hash:
                    print('MD5: ' + str(hash) + ' : ' + str(word)[1:])
                    break
                else:
                    line += 1
            except IndexError:
                bool=False
                break
    elif len(hash) == 40: #SHA-1
        while True:
            try:
                nextHash = hashlib.sha1(wl[line][:len(wl[line])-2]).hexdigest()
                word = wl[line][:len(wl[line])-2]

                if nextHash == hash:
                    print('SHA-1: ' + str(hash) + ' : ' + str(word)[1:])
                    break
                else:
                    line += 1
            except IndexError:
                bool=False
                break
    elif len(hash) == 56: #SHA-224 SHA3-224
        while True:
            try:
                nextHash = hashlib.sha224(wl[line][:len(wl[line])-2]).hexdigest()
                nextHash2 = hashlib.sha3_224(wl[line][:len(wl[line])-2]).hexdigest()
                word = wl[line][:len(wl[line])-2]
                if nextHash == hash:
                    print('SHA-224: ' + str(hash) + ' : ' + str(word)[1:])
                    break
                elif nextHash2 == hash:
                    print('SHA3-224: ' + str(hash) + ' : ' + str(word)[1:])
                else:
                    line += 1
            except IndexError:
                bool=False
                break
    if len(hash) == 64: #Blake2S SHA256 SHA3-256
        while True:
            try:
                nextHash = hashlib.blake2s(wl[line][:len(wl[line])-2]).hexdigest()
                nextHash2 = hashlib.sha256(wl[line][:len(wl[line])-2]).hexdigest()
                nextHash3 = hashlib.sha3_256(wl[line][:len(wl[line])-2]).hexdigest()
                word = wl[line][:len(wl[line])-2]
                if nextHash == hash:
                    print('Blake2S: ' + str(hash) + ' : ' + str(word)[1:])
                    break
                elif nextHash2 == hash:
                    print('SHA256: ' + str(hash) + ' : ' + str(word)[1:])
                    break
                elif nextHash3 == hash:
                    print('SHA3-256: ' + str(hash) + ' : ' + str(word)[1:])
                    break
                else:
                    line += 1
            except IndexError:
                bool=False
                break
    if len(hash) == 96: #SHA384 SHA3-384
        while True:
            try:
                nextHash = hashlib.sha384(wl[line][:len(wl[line])-2]).hexdigest()
                nextHash2 = hashlib.sha3_384(wl[line][:len(wl[line])-2]).hexdigest()
                word = wl[line][:len(wl[line])-2]
                if nextHash == hash:
                    print('SHA384: ' + str(hash) + ' : ' + str(word)[1:])
                    break
                elif nextHash2 == hash:
                    print('SHA3-384: ' + str(hash) + ' : ' + str(word)[1:])
                    break
                else:
                    line += 1
            except IndexError:
                bool=False
                break
    if len(hash) == 128: #Blake2B SHA512 SHA3-512')
        time.sleep(1.2)
        print('Trying Blake2B')
        time.sleep(0.5)
        print('Begin cracking')
        while True:
            try:
                nextHash = hashlib.blake2b(wl[line][:len(wl[line])-2]).hexdigest()
                nextHash2 = hashlib.sha512(wl[line][:len(wl[line])-2]).hexdigest()
                nextHash3 = hashlib.sha3_512(wl[line][:len(wl[line])-2]).hexdigest()
                word = wl[line][:len(wl[line])-2]
                print('Comparing: ' + str(hash) + ' - ' + str(nextHash) + ' ( ' + str(word)[1:] + ' )')
                if nextHash == hash:
                    print('Blake2B: ' + str(hash) + ' : ' + str(word)[1:])
                    break
                if nextHash2 == hash:
                    print('SHA-512: ' + str(hash) + ' : ' + str(word)[1:])
                    break
                if nextHash3 == hash:
                    print('SHA3-512: ' + str(hash) + ' : ' + str(word)[1:])
                    break
                else:
                    line += 1
            except IndexError:
                bool=False
                break

if __name__ == '__main__':
    a="This tool has been written for brute-force decryption. Written by Berke Polat. v.1.0"
    b="Supported encryption types:"
    word=""
    for i in range(len(a)):
        time.sleep(0.001)
        sys.stdout.write(a[i])
        sys.stdout.flush()
    print("")
    for i in range(len(b)):
        time.sleep(0.001)
        sys.stdout.write(b[i])
        sys.stdout.flush()
    list=["MD5","SHA1","SHA224","SHA256","SHA384","SHA512","SHA3-224","SHA3-256","SHA3-384","SHA3-512","BLAKE-2B","BLAKE-2S"]
    for var in list:
        time.sleep(0.001)
        sys.stdout.write(" "+ var)
        sys.stdout.flush()
    print("\n\n"+"-"*90+"\n")
    parser = argparse.ArgumentParser()
    parser.add_argument("-hs","--hash",required=True)
    parser.add_argument("-w","--wordlist",required=True)
    args = vars(parser.parse_args())
    if len(args["hash"]) not in [32,40,56,64,96,128]:
        raise HashNotValid
    else:
        try:
            wlWrite=open(args["wordlist"],'a')
            wlWrite.write("*end_of_file***")
            wlWrite.close()
        except FileNotFoundError:
            print('File does not exist.')
        else:
            wordlist=open(args["wordlist"],'rb').readlines()
    decrypt(args["hash"],wordlist)
