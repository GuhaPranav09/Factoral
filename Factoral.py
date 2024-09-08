import random
import number_list

def get_factors(n):
    pairs = []
    for i in range(2, n):  # Start from 2 to avoid trivial pairs (1, n)
        if n % i == 0 and i <= n // i:
            pairs.append((i, n // i))
    return pairs

def provide_digit_feedback(guess, actual_pair):
    feedback = []
    
    for i in range(2):
        guess_str = str(guess[i])
        actual_str = str(actual_pair[i])
        feedback.append(['Gray'] * len(actual_str))
        
        for j in range(len(guess_str)):
            if guess_str[j] == actual_str[j]:
                feedback[i][j] = 'Green'
            elif guess_str[j] in actual_str:
                feedback[i][j] = 'Yellow'
    
    return feedback

def get_best_score(filename):
    try:
        with open(filename, 'r') as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return None

def update_best_score(filename, new_score):
    with open(filename, 'w') as file:
        file.write(str(new_score))


def play_game():
    # List of semi-prime numbers to choose from (varied digit length factors)
    semi_prime_numbers = number_list.semi_prime_numbers
    
    print("\n\nWelcome to the Wordle-like Factor Guessing Game!")
    print("Rules:")
    print("1. The semi-prime number has factors of any digit length.")
    print("2. The smaller factor comes first, and the larger factor comes second.")
    print("3. Green means a digit is in the correct position.")
    print("4. Yellow means the digit is in the factor but in the wrong position.")
    print("5. Gray means the digit is not in the factor.")
    
    # Randomly choose a semi-prime number
    number_to_guess = random.choice(semi_prime_numbers)
    
    # Get all possible pairs
    possible_pairs = get_factors(number_to_guess)
    
    correct_pair = random.choice(possible_pairs)
    
    # Display the number of digits in the smaller and larger factors
    smaller_factor_digits = len(str(correct_pair[0]))
    larger_factor_digits = len(str(correct_pair[1]))
    
    print(f"\nThe semi-prime number is: {number_to_guess}")
    print(f"The smaller factor has {smaller_factor_digits} digits.")
    print(f"The larger factor has {larger_factor_digits} digits.")
    print("Enter your guess as two numbers separated by a space.")

    best_score = get_best_score("best_score.txt")
    tries = 0
    
    while True:
        try:
            user_input = input("\nYour guess: ")
            guess = tuple(map(int, user_input.split()))
            tries+=1

            if len(guess) != 2 or guess[0] < 2 or guess[1] < 2:
                print("Please enter exactly two numbers greater than 1.")
                continue

            if len(str(guess[0])) != smaller_factor_digits or len(str(guess[1])) != larger_factor_digits:
                print(f"Please enter a {smaller_factor_digits}-digit number first and a {larger_factor_digits}-digit number second.")
                continue
            
            if guess[0] > guess[1]:
                print("Smaller number should come first")
                continue
            
            if guess == correct_pair:
                print("Congratulations! You guessed the correct pair:", correct_pair)
                if best_score is None or tries < best_score:
                    print(f"Tries taken: {tries}")
                    print(f"\nNew best score! Previous best was {best_score}.")
                    update_best_score("best_score.txt", tries)
                else:
                    print(f"Best score remains {best_score}.")
                break
            else:
                feedback = provide_digit_feedback(guess, correct_pair)
                print("Feedback:")
                for i in range(2):
                    print(f"Factor {i+1}: {' '.join(feedback[i])}")
                print("Product: ", guess[0] * guess[1])
        except ValueError:
            print("Please enter valid numbers.")
    
play_game()
