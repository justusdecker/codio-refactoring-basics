def is_prime(number:int) -> bool:
    """ Checks if a given integer is a prime number using a list comprehension. """
    return [(number-1)%n for n in range(1,number)].count(True) == 1

def short_sotp(number):
    """
    My own list comprehension solution. Does the same as sum_of_two_primes!
    """
    already_used: list = []
    for result in [[[i,j] for j in range(number - i,number) if is_prime(j) and i + j == number] for i in range(2,number) if not number%2 and is_prime(i) and number - i >= 2]:
        if result:
            result[0].sort()
            if result[0] not in already_used:
                already_used.append(result[0])
    return already_used

def sum_of_two_primes(number):
    """ Attempts to find pairs of prime numbers that sum up to a given even number. """
    if number%2: return []
    already_used: list = []
    for i in range(2,number):
        second = number - i
        if is_prime(i) and second >= 2:
            for j in range(second,number):
                if is_prime(j) and i + j == number:
                    result = [i,j]
                    result.sort()
                    if result not in already_used:
                        already_used.append(result)
    return already_used

def check_user_input_until_integer(prompt:str) -> str:
    """ Continuously prompts the user for input until a string representing an integer is provided. """
    user_input: str = ""
    while not user_input:
        user_input = input(prompt)
        user_input = user_input if user_input.isdecimal() else ""
    return user_input

def main():
    """ This is where the action goes """
    number = int(check_user_input_until_integer("Enter a number: "))
    for a,b in short_sotp(number):
        print(f"The number {number} equals to the sum of {a} and {b}")

if __name__ == "__main__":
    main()