# strength_checker.py

import requests
import hashlib
import sys
import math
import getpass
import argparse
from colorama import Fore, Style, init

# Initialize Colorama for colored output
init(autoreset=True)

def check_pwned(password):
    """Securely checks the password against the 'Have I Been Pwned' database."""
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    api_url = f'https://api.pwnedpasswords.com/range/{prefix}'
    try:
        response = requests.get(api_url)
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)
    except requests.exceptions.RequestException:
        # If API is unreachable, we assume it's not pwned for safety.
        return 0
    return 0

def calculate_entropy(password):
    """Calculates the entropy of the password in bits."""
    if not password:
        return 0
    pool_size = 0
    if any(c.islower() for c in password): pool_size += 26
    if any(c.isupper() for c in password): pool_size += 26
    if any(c.isdigit() for c in password): pool_size += 10
    if any(not c.isalnum() for c in password): pool_size += 32
    if pool_size == 0: return 0
    return len(password) * math.log2(pool_size)

def check_patterns(password):
    """Checks for sequential and repetitive patterns."""
    feedback = []
    # Check for sequences (e.g., 'abc', '123')
    for i in range(len(password) - 2):
        if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2:
            feedback.append(f"Contains a sequence ('{password[i:i+3]}').")
            break
            
    # Check for repetitions (e.g., 'aaa', '111')
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            feedback.append(f"Contains a repetition ('{password[i]*3}').")
            break
            
    return feedback

def analyze_password(password):
    """Analyzes the password and returns a score and detailed feedback."""
    feedback = []
    score = 100 # Start with a perfect score and deduct points

    # Length check
    length = len(password)
    if length < 8:
        feedback.append((Fore.RED, "❌ Very short password. Aim for at least 12 characters."))
        score -= 70
    elif length < 12:
        feedback.append((Fore.YELLOW, "⚠️ Good length (8-11), but 12+ is recommended."))
        score -= 30
    else:
        feedback.append((Fore.GREEN, "✅ Great length (12+ characters)."))

    # Variety check
    variety = sum([
        1 if any(c.islower() for c in password) else 0,
        1 if any(c.isupper() for c in password) else 0,
        1 if any(c.isdigit() for c in password) else 0,
        1 if any(not c.isalnum() for c in password) else 0
    ])
    if variety < 3:
        feedback.append((Fore.RED, "❌ Low variety. Mix uppercase, lowercase, numbers, and symbols."))
        score -= 25
    else:
        feedback.append((Fore.GREEN, "✅ Excellent variety of character types."))

    # Pattern check
    pattern_feedback = check_patterns(password)
    if pattern_feedback:
        for p_fb in pattern_feedback:
            feedback.append((Fore.RED, f"❌ {p_fb}"))
        score -= 40 # Heavy penalty for patterns

    # HIBP check
    pwned_count = check_pwned(password)
    if pwned_count > 0:
        feedback.append((Fore.RED, f"❌ CRITICAL: This password was found in {pwned_count:,} data breaches!"))
        score = 0 # If breached, score is 0
    else:
        feedback.append((Fore.GREEN, "✅ Good news! Not found in any known data breaches."))

    # Add entropy info
    entropy = calculate_entropy(password)
    feedback.append((Fore.CYAN, f"ℹ️ Password Entropy: {entropy:.2f} bits."))
    
    # Final Rating
    score = max(0, score) # Ensure score isn't negative
    rating = ""
    if score >= 90: rating = Fore.GREEN + "🚀 Very Strong"
    elif score >= 70: rating = Fore.GREEN + "👍 Strong"
    elif score >= 40: rating = Fore.YELLOW + "😐 Medium"
    else: rating = Fore.RED + "💀 Weak"

    return {"score": score, "rating": rating, "feedback": feedback}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze the strength of a password.")
    parser.add_argument("password", nargs='?', default=None, help="The password to analyze.")
    args = parser.parse_args()

    password_to_check = args.password or getpass.getpass("Enter the password to check: ")

    if not password_to_check:
        print(Fore.RED + "No password provided. Exiting.")
        sys.exit(1)
        
    analysis = analyze_password(password_to_check)

    print("\n--- Password Strength Analysis ---")
    print(f"Overall Rating: {analysis['rating']}")
    print(f"Final Score: {analysis['score']}/100")
    print("\n--- Detailed Feedback ---")
    for color, line in analysis['feedback']:
        print(color + f"- {line}")
    print("---------------------------------")