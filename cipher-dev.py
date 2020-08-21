#!/usr/bin/env python

import hashlib
from string import ascii_lowercase as alpha
from operator import mod
from functools import partial
import sys

def compose(*funcs):
    def inner(*argv):
        for func in funcs:
            argv = func(argv)
        return argv
    return inner

# Ceasar
t = len(alpha)

def calc(letra, tipo='encrypt'):
    if tipo == 'encrypt':
        exp = alpha.index(letra) + 3
    else: exp = alpha.index(letra) - 3
    return alpha[mod(exp, t)]

dec = partial(calc, tipo='decrypt')

def encrypt(frase: str) -> str:
    return print(''.join(map(calc, sys.argv[2]))) if sys.argv[1] == '-c' else None

def decrypt(frase: str) -> str:
    return print(''.join(map(dec, sys.argv[2]))) if sys.argv[1] == '-d' else None 

#HASHS
def md5sum(frase: str) -> str:
    return print(hashlib.md5((sys.argv[2]).encode('utf-8')).hexdigest()) if sys.argv[1] == '-h5' else None

def sha1sum(frase: str) -> str:
    return print(hashlib.sha1((sys.argv[2]).encode('utf-8')).hexdigest()) if sys.argv[1] == '-h1' else None

def sha224sum(frase: str) -> str:
    return print(hashlib.sha224((sys.argv[2]).encode('utf-8')).hexdigest()) if sys.argv[1] == '-h224' else None

def sha256sum(frase: str) -> str:
    return print(hashlib.sha256((sys.argv[2]).encode('utf-8')).hexdigest()) if sys.argv[1] == '-h256' else None

def sha384sum(frase: str) -> str:
    return print(hashlib.sha384((sys.argv[2]).encode('utf-8')).hexdigest()) if sys.argv[1] == '-h384' else None

def sha512sum(frase: str) -> str:
    return print(hashlib.sha512((sys.argv[2]).encode('utf-8')).hexdigest()) if sys.argv[1] == '-h512' else None


def help_ciphy(frase: str) -> str:
    return print("./ciphy.py [OPTION] [PHRASE]\n \
    options:\n \
    \t-d\t\tdecrypt\n \
    \t-h5\t\thash md5\n \
    \t-h1\t\thash sha1\n \
    \t-h224\t\thash sha224\n \
    \t-h256\t\thash sha256\n \
    \t-h384\t\thash sha384\n \
    \t-h512\t\thash sha512\n \
    Example:\n \
    \t./ciphy.py -c ceaserexemple\n \
    \t./ciphy.py -d fhdvhuhahpsoh") if sys.argv[1] == '-h' or sys.argv[1] == '--help' else None
        
main = compose(help_ciphy, decrypt, md5sum, encrypt, sha1sum, sha224sum, sha256sum, sha384sum, sha512sum)

try:
    if sys.argv:
        main(str(sys.argv))
except:
    print("Invalid Option!")