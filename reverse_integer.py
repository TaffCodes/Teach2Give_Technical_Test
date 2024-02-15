#Write a program that takes an integer as input and returns an integer with reversed digit ordering.
num = int(input("Enter an integer: "))

def reverse_integer(num):

    # Convert the integer to a string and then reverse it
    if num >= 0:
        reversed_str = str(num)[::-1]
    else:
        reversed_str = '-' + str(abs(num))[::-1]
    
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)
    return reversed_num

#Print the reversed integer
print(f"For input {num}, the program returns {reverse_integer(num)}")

# inputs = [500, -56, -90, 91]


