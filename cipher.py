#!/usr/bin/env python

from string import ascii_lowercase as alpha
from operator import mod
from functools import partial
import sys

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
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            return help_ciphy()
        return print(encrypt(sys.argv[1]))
    except ValueError:
        return help_ciphy()

main()
