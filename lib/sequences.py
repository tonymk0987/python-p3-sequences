def print_fibonacci(length):
    # If length is 0, print an empty list and return
    if length == 0:
        print("[]")
        return

    # Initializing the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]

    # Looping so as to generate Fibonacci sequence up to the specified length
    while len(fibonacci_sequence) < length:
        # Calculate the next Fibonacci number by adding the last two numbers
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        # Append the next Fibonacci number to the sequence
        fibonacci_sequence.append(next_number)
    if length == 1:
        print([0])
    else:
        print(fibonacci_sequence)

