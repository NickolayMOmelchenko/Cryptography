# This function takes a ciphertext as input and creates an array of integers as an output.
# Each index in the array corresponds to the count of that letter in the alphabet (0 = A, 1 = B...)
def char_count(cipher):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    cipher_count = [0 for a in range(26)]

    no_space = cipher.replace(" ", "")
    cipher_length = len(no_space)

    # iterate over cipher text and compute frequencies for each character
    for i in range(cipher_length):
        alphabet_index = alphabet.index(no_space[i]) # index of character in alphabet
        cipher_count[alphabet_index] += 1
    return cipher_count


def caesar(cipher):
    # define alphabet and initialize array to store frequencies of characters in cipher text
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    english_freq = [0.080,0.015,0.030,0.040,0.130,0.020,0.015,0.060,0.065,0.005,0.005,0.035,0.030,0.070,0.080,0.020,
                    0.002,0.065,0.060,0.090,0.030,0.010,0.015,0.005,0.020,0.002]
    correlation_freq = [0 for a in range(26)]

    no_space = cipher.replace(" ", "")
    cipher_length = len(no_space)

    # compute the count of each letter in the ciphertext. Then get the frequencies for each character.
    cipher_freq = char_count(cipher)
    for i in range(26):
        cipher_freq[i] = cipher_freq[i] / cipher_length

    # compute the correlation frequencies (phi)
    # compute frequency for every value of i [0, 25]
    for i in range(26):
        # phi(i) = summation[0,25](f(c)*f'(e-i))
        freq = 0
        # sum every letter in the alphabet
        for e in range(len(alphabet)):
            freq += cipher_freq[e]*english_freq[(26 + e - i)%26]
        correlation_freq[i] = freq

    # Find the highest correlation probability and shift ciphertext by the corresponding key.
    max_freq = max(correlation_freq)
    max_index = correlation_freq.index(max_freq)
    cleartext = ""
    for j in range(len(cipher)):
        if cipher[j] == " ":
            cleartext += " "
        else:
            cleartext += (alphabet[(alphabet.index(cipher[j]) + 26 - max_index) % 26])

    return (cleartext, max_freq, max_index)

# Function computes the index of coincidence for a provided ciphertext
def ic(cipher):
    no_space = cipher.replace(" ", "")
    cipher_length = len(no_space)

    # Compute the frequencies for each character in the alphabet
    cipher_freq = char_count(cipher)

    index_coincidence = 0
    
    # compute the scalar applied to the summation (1 / N(N-1))
    scalar = 1 / (cipher_length * (cipher_length-1))

    # Compute the summation IC
    for j in range(26):
            index_coincidence += (cipher_freq[j] * (cipher_freq[j] - 1))
    
    index_coincidence *= scalar
    return(index_coincidence)        

# This function splits the ciphertext into x (number) groups and computes the IC for each group.
def compute_index_coincidences(cipher, number):
    no_space = cipher.replace(" ", "")
    cipher_length = len(no_space)
    
    # i represents the number of groups
    for i in range(2,number+1):
        string_array = ["" for a in range(i)]

        # j represents the length of the ciphertext
        for j in range(cipher_length):
            # k represents the number of groups
            for k in range(i):
                if (j % i == k):
                    # seperate characters every other character into n groups
                    string_array[k] += no_space[j]

        index_coincidence = [0 for a in range(i)]
        avg_index_coincidence = 0
        # for each group compute the index of coincidence and add to average
        for m in range(i):
            index_coincidence[m] = ic(string_array[m])
            avg_index_coincidence += index_coincidence[m]

        avg_index_coincidence = avg_index_coincidence / i
        # print the index and the average IC
        print("Index: " + str(i) + " IC: " + str(avg_index_coincidence))

# This algorithm takes a ciphertext and a period length (taken from compute_index_coincidence function)
# It outputs a string of the most likely cleartext
def vigenere(cipher, period):
    no_space = cipher.replace(" ", "")
    cipher_length = len(no_space)
    
    # Split the ciphertext into groups by the period
    string_array = ["" for a in range(period)]
    for j in range(cipher_length):
        for k in range(period):
            if (j % period == k):
                string_array[k] += no_space[j]

    # compute caesar cipher for every group
    for i in range(period):
        string_array[i] = caesar(string_array[i])[0]

    # Get the maximum length of the string in the array
    maximum = len(string_array[0])

    # Pad smaller strings to the length of maximum
    for i in range(period):
        if len(string_array[i]) < maximum:
            difference = maximum - len(string_array[i])
            for j in range(difference):
                string_array[i] += " "

    # Combine each of the solved groups into one cleartext
    final_string = ""
    for i in range(maximum):
        for j in range(period):
            final_string += string_array[j][i]

    # print the final string
    return(final_string)


if __name__ == '__main__':
    print("\n---- Vigenere Cipher ----")
    cipher = input("Input Vigener chiper: ").upper()
    x = int(input('Enter the desired IC number: '))
    y = int(input('Enter the desired period: '))
    compute_index_coincidences(cipher, x)
    plaintext = vigenere(cipher, y);
    print(plaintext.lower())
