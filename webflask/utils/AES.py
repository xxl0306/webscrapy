# -*- coding: utf-8 -*-
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

from Crypto.Cipher import AES
import base64
class prpcrypt():
    def __init__(self, key):
        self.bs = 16
        self.cipher = AES.new(key, AES.MODE_CBC,b'0000000000000000')

    def encrypt(self, raw):
        raw = self._pad(raw)
        encrypted = self.cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self.cipher.decrypt(decoded)
        print(decrypted)
        return str(self._unpad(decrypted), 'utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]


if __name__ == '__main__':
    key = '`?.F(fHbN6XK|j!t'
    cipher = prpcrypt(key)

    plaintext = '542#1504891440039'
    encrypted = cipher.encrypt(plaintext)
    print('Encrypted: %s' % encrypted)
    decrypted = cipher.decrypt(encrypted)
    print('Decrypted: %s' % decrypted)
    assert decrypted == plaintext