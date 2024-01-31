import random

# Specify the size of the array
array_size = 10

# Generate an array of random integers
random_integers = [random.randint(1, 100) for _ in range(array_size)]

# Generate an array of random floats
random_floats = [random.uniform(1.0, 100.0) for _ in range(array_size)]

# Print the generated arrays
print("Random Integers:", random_integers)
print("Random Floats:", random_floats)
