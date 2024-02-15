# Write a program that prints the numbers from 1 to 100.
# For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz".
# For numbers that are multiples of both 3 and 5, print "FizzBuzz".

# The for loop iterates between the numbers 1 and 100.
for i in range(1, 101):
  #If the input is divisible by 3 and 5, print "FizzBuzz"
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
#If the input is divisible by  only 3, print "Fizz"
  elif i % 3 == 0:
    print("Fizz")
#If output is divisible by  only 5, print "Buzz"
  elif i % 5 == 0:
    print("Buzz")

  else:
    print(i)