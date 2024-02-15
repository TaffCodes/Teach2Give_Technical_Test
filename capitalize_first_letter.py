#Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string

def capitalize_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # capitalizes each word
    capitalized_words = [word.capitalize() for word in words]
    
    # Joins the capitalized words
    result = ' '.join(capitalized_words)
    
    return result

input_string = input("Enter a string: ")
result_string = capitalize_words(input_string)
print(result_string)

