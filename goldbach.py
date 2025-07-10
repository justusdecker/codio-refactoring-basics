def is_prime(number:int) -> bool:
    """ Checks if a given integer is a prime number using a list comprehension. """
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    divisors = [n for n in range(2, int(number**0.5) + 1) if number % n == 0]

    return len(divisors) == 0

def sum_of_two_primes(number):
    """ Attempts to find pairs of prime numbers that sum up to a given even number. """
    if number%2: return []
    already_used: list = []
    for i in range(2,number):
        second = number - i
        if is_prime(i) and second >= 2 and is_prime(second):
            result = [i,second]
            result.sort()
            if result not in already_used:
                already_used.append(result)
    return already_used

def check_user_input_until_integer(prompt:str) -> int:
    """
    Continuously prompts the user for input until a valid integer is provided.
    Returns the to int converted user_input
    """
    user_input: str = ""
    while not user_input:
        user_input = input(prompt)
        user_input = user_input if user_input.isdecimal() else ""
    return int(user_input)

def main():
    """ This is where the action goes """
    number = check_user_input_until_integer("Enter a number: ")
    for a,b in sum_of_two_primes(number):
        print(f"The number {number} equals to the sum of {a} and {b}")

if __name__ == "__main__":
    main()