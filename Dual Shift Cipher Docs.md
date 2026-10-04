Dual Shift Cipher - S.S Amber

https://github.com/Amber-Moons/Dual-Shift-Cipher

Keys:

Keys are how you encipher and decipher this cipher. For this cipher you will need a key with at least the same amount of symbols as in your plaintext, its eaiseast to randomize the alphabet for your key. Once you have all of charicters for a key you will need to give them each a unique number in acneding order. In this guide we will be using two keys, one the ordered alphabet (key1), and the other a randomized alphabet (key2). For convience in this example the second and third digit will be the charicters assigned number.

Key1:
    A01 B02 C03 D04 E05 F06 G07 H08 I09 J10 K11 L12 M13 N14 O15 P16 Q17 R18 S19 T20 U21 V22 W23 X24 Y25 Z26 ,27 .28 ?29 !30 131 232 333 434 535 636 737 838 939 040

Key2:
    M01 Y02 O03 ,04 .05 306 R07 U08 C09 D10 H11 Z12 S13 E14 415 716 A17 I18 X19 J20 W21 K22 ?23 T24 825 L26 !27 B28 529 N30 131 Q32 V33 G34 035 936 F37 238 P39 640

If you want to input the key into the script use this
Key1:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ,.?!1234567890

Key2:
    MYO,.3RUCDHZSE47AIXJWK?T8L!B5N1QVG09F2P6

Or additonaly the most convient way on paper
Key1:
    |A|B|C|D|E|         
    |F|G|H|I|J|
    |K|L|M|N|O|
    |P|Q|R|S|T|
    |U|V|W|X|Y|
    |Z|,|.|?|!|
    |1|2|3|4|5|
    |6|7|8|9|0|

Key2:
    |M|Y|O|,|.|
    |3|R|U|C|D|
    |H|Z|S|E|4|
    |7|A|I|X|J|
    |W|K|?|T|8|
    |L|!|B|5|N|
    |1|Q|V|G|0|
    |9|F|2|P|6|


Enciphering:

Firstly you will need a message to encipher, it must be at least 2 charicters long and not contain any chraticers that are not in the key. During direction only Key1 will be used, at the end their will be an example enciphered using Key2. The example plaintext we will be using will be:
    The quick brown fox jumps over the lazy dog
This is example will not use punctuation nor numbers allthough possible.
1. To begin enciphering first remove all spaces and keep all charicters the same case, for example:
    THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG
2. Next take the first two letters and find their numerical value. For instance the first two letters here are T and H, T is the 20th letter in the key while H is the 8th.
3. Add these two numbers togehter, if the anwnser is greater than the highest keyed number subtract the highest key number. In our example T + H is 28, however for example if our first two letters were T(20) and Y(25) we would be left with 45. This is higher than our highest number of 0(40) so we subtract 40 from 45 to be left with 5.
4. Now find the letter in the key that corosopnds to the number you've just added. Here we have 28 and the 28th charicter in our key is "."
5. Replace this new charicter with the first letter of the two you added. Now our example text should look like this:
    .HEQUICKBROWNFOXJUMPSOVERTHELAZYDOG
6. Repeat this but moving the two charicters forward each time until only one original charicter remains. Therefor our next two charicters will be H(8) and E(5) which will give us 13, and the 13th charicter in the key is M. Now our example text should look like this:
    .MV8!LNMT387TU9414?547,W8.MQM,K?SVG
7. For the final charicter its mostly the same pattern however for the second charicter which is missing use the first ciphered letter. For example here its G(7) and .(28) which is 35 and the 35th charicter of the key is 5, now your cipher text should be:
    .MV8!LNMT387TU9414?547,W8.MQM,K?SV5

If you were to use Key2 to encipher the sampple text it should be:
    0836L!1D0DTH!6KPBC6Z79RW1086O5EZSF5