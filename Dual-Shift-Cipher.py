

DEFAULT_KEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ,.?!1234567890"
Plain1 = "THEQUICKBROWNFOXJUMPSJOVERTHELAZYDOG"
Encipher = ".MV8!LNMT387TU9414?5?Y7,W8.MQM,K?SV5"
Keylen = 40
Keyadd = list(DEFAULT_KEY)
Key = [None]
Key.extend(Keyadd)
Plain = list(Plain1)
Enciphered = list(Encipher)

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

def Decipher(Encend, Encend2):
    Enc1 = Enciphered[0]
    Enc2 = Enciphered[35]
    print (Enc1)
    print (Enc2)
    Enc1n = Key.index(Enc1)
    Enc2n = Key.index(Enc2)
    print (Enc1n)
    print (Enc2n)
    Encnu = Enc2n - Enc1n
    if Encnu < 1:
        Encnu =+ Keylen
    Enclet = Key[Encnu]
    return Enclet

def FullEncipher():
    Messagelen = len(Plain)
    while Messagelen > 1:
    
        Ciphnxt = Encipher()
        Messagelen -= 1
        Ciphersec = list(Ciphnxt)
        Cipherout.extend(Ciphersec)
    Out = "".join(Cipherout)
    return Out
#Out = FullEncipher()

def FullDecipher():
    Messagelen = len(Enciphered)
    

Out = Decipher(1,34)

print (Out)
