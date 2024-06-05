import random
print("Guess game! You've 5 attempts to guess the correct number and the number is in between 10 to 99")
number = random.randint(10,99)
#print(f"\nthat random no, for this game was: {number}")

attempt_counter = 0
user_input = 0


def if_guess_is_correct():
    if user_input == number:
        return True
    else:
        return False

def wanna_replay():

    while True:
        u_i = input("Wanna replay?... If yes, then input 'y' ..if wanna quit, input 'q': ")

        if u_i not in ('y', 'q'):
            print("You must input either 'y' or 'q' ")
            continue

        if u_i == 'y':return True
        else:return False


def hint_giving():
    if attempt_counter == 1:
        if number > 50 and number%2 == 0:return (f"the number is above 50 and an 'Even number'")
        elif number > 50 and number%2 != 0:return (f"the number is above 50 and an 'Odd number'")
        elif number <= 50 and number%2 == 0:return (f"the number is below or equal to 50 and an 'Even number'")
        elif number <= 50 and number%2 != 0:return (f"the number is below or equal to 50 and an 'Odd number'")

    elif attempt_counter <= 5:
        ranges = [(10, 21), (20, 31), (30, 41), (40, 51), (50, 61), (60, 71), (70, 81), (80, 91), (90, 100)]

        for (f,s) in ranges:
            if number > user_input and number % 2 ==0 and number in range(f,s):
                return (f"the number is above {user_input} and is an 'Even number' and within range {f} to {s-1}")
            elif number > user_input and number % 2 !=0 and number in range(f,s):
                return (f"the number is above {user_input} and is an 'Odd number' and within range {f} to {s-1}")
            elif number <= user_input and number % 2 ==0 and number in range(f,s):
                return (f"the number is below {user_input} and is an 'Even number' and within range {f} to {s-1}")
            elif number <= user_input and number % 2 !=0 and number in range(f,s):
                return (f"the number is below {user_input} and is an 'Odd number' and within range {f} to {s-1}")


#guessing loop
while True:

    while True:

        if attempt_counter == 5:
            print("\nYou've used all the FIVE attempts. Hence exiting the program")
            break

        attempt_counter +=1

        print(f"\nattempt no: {attempt_counter}\nhint: {hint_giving()}")
        user_input = int(input(f"Pls enter your guess: "))

        if user_input not in range(10,100):
            print("Your input must be within 10 to 99")
            continue

        if attempt_counter <=5 and if_guess_is_correct():
            print("\n!!** Congratz **!!.Your guess is correct!")
            break

        else:
            print("Sorry! Your guess is NOT correct")
            continue

    print(f"\n[that random no, for this game was: {number}]")

    if wanna_replay():
        attempt_counter = 0
        continue
    else:
        break








