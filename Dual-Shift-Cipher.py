

DEFAULT_KEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ,.?!1234567890"
Plain1 = "THEQUICKBROWNFOXJUMPSJOVERTHELAZYDOG"
Keylen = 40
Keyadd = list(DEFAULT_KEY)
Key = [None]
Key.extend(Keyadd)

Plain = list(Plain1)
def Encipher():
    Enc2 = Plain[1]
    Enc1 = Plain.pop(0)
    Enc1n = Key.index(Enc1)
    Enc2n = Key.index(Enc2)
    Encnu = Enc1n + Enc2n
    if Encnu > Keylen:
        Encnu = Encnu - Keylen
    Enclet = Key[Encnu]
    return Enclet
Cipherout = []
Messagelen = len(Plain)
while Messagelen > 1:
    
    Ciphnxt = Encipher()
    Messagelen -= 1
    Ciphersec = list(Ciphnxt)
    Cipherout.extend(Ciphersec)
Out = "".join(Cipherout)
print (Out)
