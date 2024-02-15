# Write a program that counts the number of vowels in a sentence.

def count_vowels(sentence):
    # Define the vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert the sentence to lowercase for flexibility
    sentence = sentence.lower()
    vowel_count = 0
    
    # Iterate through each character in the sentence
    for char in sentence:
        # Add to the the counter when the character is a vowel
        if char in vowels:
            vowel_count += 1
    
    return vowel_count
input_sentence = input("Enter a sentence: ")
print("Number of vowels:", count_vowels(input_sentence))
