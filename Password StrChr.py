import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Lowercase Check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Uppercase Check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Digit Check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Special Character Check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters (e.g., !@#$%).")

    # Strength Evaluation
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    elif score == 5:
        strength = "Very Strong"

    return strength, feedback

def main():
    while True:
        password = input("Enter a password to check its strength (or type 'exit' to quit): ").strip()
        if password.lower() == 'exit':
            print("Exiting program.")
            break

        strength, feedback = check_password_strength(password)
        print(f"Password Strength: {strength}")

        if feedback:
            print("Suggestions to improve your password:")
            for f in feedback:
                print(f"- {f}")

        print("-" * 50)

if __name__ == "__main__":
    main()
