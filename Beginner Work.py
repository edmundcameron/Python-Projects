monthConversions = {
    "Jan": "January",
    "Feb": "February",
}

print(monthConversions["Jan"])

i = 1
while i <= 3:
    print(i)
    i += 1

secret_word = "Cat"
user_guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("")

while user_guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        user_guess = input("Enter animal: ")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("Out of guesses, you LOSE")
else:
    print("You win!")

import