from zxcvbn import zxcvbn
import colorama
from colorama import Fore

colorama.init()

def password_strength(password):
    result = zxcvbn(password)
    score = result['score']
    entropy = result['guesses_log10']
    bar = '█' * (score * 2) + '-' * (10 - score * 2)
    color = [Fore.RED, Fore.YELLOW, Fore.YELLOW, Fore.GREEN, Fore.GREEN][score]
    print(f"Password: {password}")
    print(f"Strength: {color}{bar} {score}/5{Fore.RESET}")
    print(f"Entropy: {entropy:.2f} bits")
    if result['feedback']['warning']:
        print(f"Warning: {result['feedback']['warning']}")

password = input("Enter password to analyze: ")
password_strength(password)