#!/usr/bin/env python

import hashlib
from string import ascii_lowercase as alpha
from operator import mod
from functools import partial
import sys

# Ceasar
t = len(alpha)

def calc(letra, tipo='encrypt'):
    if tipo == 'encrypt':
        exp = alpha.index(letra) + 3
    else: exp = alpha.index(letra) - 3
    return alpha[mod(exp, t)]

dec = partial(calc, tipo='decrypt')

def encrypt(frase: str) -> str:
    return ''.join(map(calc, frase))

def decrypt(frase: str) -> str:
    return ''.join(map(dec, frase))

#HASHS
def md5sum(frase: str) -> str:
    return hashlib.md5((frase).encode('utf-8')).hexdigest()

def sha1sum(frase: str) -> str:
    return hashlib.sha1((frase).encode('utf-8')).hexdigest()

def sha224sum(frase: str) -> str:
    return hashlib.sha224((frase).encode('utf-8')).hexdigest()

def sha256sum(frase: str) -> str:
    return hashlib.sha256((frase).encode('utf-8')).hexdigest()

def sha384sum(frase: str) -> str:
    return hashlib.sha384((frase).encode('utf-8')).hexdigest()

def sha512sum(frase: str) -> str:
    return hashlib.sha512((frase).encode('utf-8')).hexdigest()


def help_ciphy():
    print("./ciphy.py [OPTION] [PHRASE]")
    print("option:")
    print("\t-d\tdecrypt")
    print("Exemple:")
    print("\t./ciphy.py ceaserexemple")
    print("\t./ciphy.py -d fhdvhuhahpsoh")



def main():
    try:
        if sys.argv[1] == '-d':
            return print(decrypt(sys.argv[2]))
        if sys.argv[1] == '--hash' and sys.argv[2] == '--md5':
            return print(md5sum(sys.argv[3]))
        if sys.argv[1] == '--hash' and sys.argv[2] == '--sha1':
            return print(sha1sum(sys.argv[3]))
        if sys.argv[1] == '--hash' and sys.argv[2] == '--sha224':
            return print(sha224sum(sys.argv[3]))
        if sys.argv[1] == '--hash' and sys.argv[2] == '--sha256':
            return print(sha256sum(sys.argv[3]))
        if sys.argv[1] == '--hash' and sys.argv[2] == '--sha384':
            return print(sha384sum(sys.argv[3]))
        if sys.argv[1] == '--hash' and sys.argv[2] == '--sha512':
            return print(sha512sum(sys.argv[3]))
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            return help_ciphy()
        return print(encrypt(sys.argv[1]))
    except ValueError:
        return help_ciphy()

main()
