#Write a program to generate the Fibonacci sequence up to 100.

def generate_fibonacci(limit):
    # Initialize variables
    fibonacci_sequence = [0, 1]
    next_term = 1
    
    # Generate the sequence
    while next_term <= limit:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_term <= limit:
            fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

# Generate Fibonacci sequence up to the sum of 100
fibonacci_sequence = generate_fibonacci(100)

# Print the Fibonacci sequence
print("Fibonacci sequence up to 100:")
print(fibonacci_sequence)
