# Vigenère Cipher Breaker

The Vigenère Cipher is a polyalphabetic substitution cipher that uses a keyword to shift letters in the plaintext. This program helps you decrypt Vigenère-encrypted text by determining the likely key length and then decrypting the ciphertext using the Vigenère key.

## How the Vigenère Cipher Works

The Vigenère Cipher uses a keyword to repeatedly encrypt the plaintext. Here's how it works:

Choose a keyword, for example, "KEY."
Repeat the keyword to match the length of the plaintext. For instance, if your plaintext is "HELLOFRIEND," the keyword becomes "KEYKEYKEYK."
Assign a number to each letter in the keyword (A=0, B=1, C=2, ... Z=25).
Shift each letter in the plaintext by the corresponding number from the keyword.
For example, H (7th letter) + K (10th letter) = R (17th letter).

## Using the Program

1. Run the Python script:
```script
python3 vigenerchiper.py
```

Enter the Vigenère cipher you want to decrypt.
Choose the desired IC (Index of Coincidence) number to analyze. The IC helps estimate the key length. The program will calculate IC values for different key lengths and display the results.
After selecting the desired key length, enter the period (key length) you want to use.
The program will decrypt the ciphertext based on the chosen key length and display the cleartext.
Example:

Suppose you have the following Vigenère cipher:

## Input 
```script
Input Vigenere cipher: Rijvs dbmcxh rrelu cme jmb gfogisre yyr dlc zvmqvyw Fccx mp psmo
Enter the desired IC number: 5
Enter the desired period: 3
```

## Output
```script
hellofriendthankyouforcheckingouttheprogrambestofluck
```
