
# **Dual-Shift-Cipher**


<div align="left">

[![Stars](https://img.shields.io/github/stars/Amber-Moons/Dual-Shift-Cipher?style=flat-square&label=Stars&color=gold&logo=github)](https://github.com/Amber-Moons/Dual-Shift-Cipher/releases)
[![Latest Release](https://img.shields.io/github/v/release/Amber-Moons/Dual-Shift-Cipher?style=flat-square&include_prereleases&logo=github&label=Version)](https://github.com/Amber-Moons/Dual-Shift-Cipher/releases/latest)

</div>

## About:

Dual Shift Cipher is a pen paper cipher that while time consuming is difficult to break. It's widely configurable to be able to include anything from normal characters to abstract symbols. This is done via adding adjacent
letters key value and the inverse for enciphering and deciphering. This doc will be split into two parts, firstly the instructions for how to use the solver program, and secondly, how to use the cipher on paper.

## Dual Shift Cipher solver instructions:



## Dual Shift Cipher pen paper:



### Keys:

Keys are the guide you will need to encipher and decipher this cipher. For this cipher you will need a key with at least the same amount of symbols as in your plaintext, its easiest to randomize the alphabet for your key. 
Once you have all of characters for a key you will need to give them each a unique number in ascending order. In this guide we will be using two keys, one the ordered alphabet (key1), and the other a randomized alphabet (key2). 
Numbers will be assigned left to right top to bottom.

Key1:

| A | B | C | D | E |
| - | - | - | - | - | 
|F|G|H|I|J|
|K|L|M|N|O|
|P|Q|R|S|T|
|U|V|W|X|Y|
|Z|,|.|?|!|
|1|2|3|4|5|
|6|7|8|9|0|



Key2:

| M | Y | O | , | . |
| - | - | - | - | - | 
|3|R|U|C|D|
|H|Z|S|E|4|
|7|A|I|X|J|
|W|K|?|T|8|
|L|!|B|5|N|
|1|Q|V|G|0|
|9|F|2|P|6|


### Enciphering:

Firstly you will need a message to encipher, it must be at least 2 characters long and not contain any characters that are not in the key. During direction only Key1 will be used, at the end their will be an example 
enciphered using Key2. The example plaintext we will be using will be:

*The quick brown fox jumps over the lazy dog*
    
This is example will not use punctuation nor numbers although possible.
1. To begin enciphering first remove all spaces and keep all characters the same case, for example:
    *THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG*
2. Next take the first two letters and find their numerical value. For instance the first two letters here are T and H, T is the 20th letter in the key while H is the 8th.
3. Add these two numbers together, if the answer is greater than the highest keyed number subtract the highest key number. In our example T + H is 28, however for example if our first two letters were T(20) and Y(25)
we would be left with 45. This is higher than our highest number of 0(40) so we subtract 40 from 45 to be left with 5.
4. Now find the letter in the key that corresponds to the number you've just added. Here we have 28 and the 28th character in our key is "."
5. Replace this new character with the first letter of the two you added. Now our example text should look like this:
    *.HEQUICKBROWNFOXJUMPSOVERTHELAZYDOG*
6. Repeat this but moving the two characters forward each time until only one plaintext character remains. Therefor our next two characters will be H(8) and E(5) which will give us 13, and the 13th character in the key
is M. Now our example text should look like this:
    ".MV8!LNMT387TU9414?547,W8.MQM,K?SVG"
7. For the final character its mostly the same pattern however for the second character which is missing use the first ciphered letter. For example here its G(7) and .(28) which is 35 and the 35th character of the key 
is 5, now your ciphertext should be:
    *.MV8!LNMT387TU9414?547,W8.MQM,K?SV5*

If you were to use Key2 to encipher the sample text it should be:

*0836L!1D0DTH!6KPBC6Z79RW1086O5EZSF5*

### Deciphering:

To decipher you will need an enciphered message as well as the key that was used to encipher it. Like before only Key1 will receive instructions. We will be deciphering the message:

*.MV8!LNMT387TU9414?547,W8.MQM,K?SV5*

1. Because the last secondary cipher letter is the beginning of the cipher will we use the first letter of the cipher text as character 1 and the last letter of the cipher text as character 2. In our example our first character
 will be "." and the second will be 5. 
2. Like before find each of their corresponding digits. Here character 1 is "." which on our key is 28 and character 2 which is 5 holds the 35th place in they key.
3. Now you must find the difference between character 2 and 1, if the answer is negative begin back at the highest keyed number. Subtracting character 2(35) from character(28) is 7.
4. Next find the character that is in the place of the number you just subtracted. The 7th place in Key1 is G.
5. Now substitute character 2 for the letter you just deciphered. After replacing 5 with G our example text should look like this:
   *.MV8!LNMT387TU9414?547,W8.MQM,K?SVG*
6. Repeat this for each letter by moving both deciphering characters one left each time and using the character one plaintext charicter until the entire message is deciphered. Now charicter 1 will be G(7) while charicter 2 will
 be V(22) which 22 - 7 is O(15). Now our example should be deciphered as:

*THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG*
