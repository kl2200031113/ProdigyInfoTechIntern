import string
def check_password_strength(password):
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    if length_ok and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length_ok and (has_upper or has_lower) and has_digit:
        return "Moderate"
    else:
        return "Weak"
def main():
    print("Password Complexity Checker")
    print("===========================")
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")
if name == "main":
    main()