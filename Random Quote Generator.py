import random

# List of quotes
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
    "Believe you can and you're halfway there. - Theodore Roosevelt"
]

def display_random_quote():
    """Prints a random quote from the list."""
    print("Here's a quote to inspire you:\n")
    print(random.choice(quotes))

if __name__ == "__main__":
    display_random_quote()
