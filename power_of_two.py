#Write a program that takes an integer as input and returns true if the input is a power of two.

def power_of_two(num):
    # Check if the number is positive and not a zero
    if num <= 0:
        return False
    
    # Check if the number has only one set bit
    return (num & (num - 1)) == 0

num = int(input("Enter an integer: "))
print(power_of_two(num))
