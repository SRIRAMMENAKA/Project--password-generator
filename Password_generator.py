import random
import string

def password_generator(min_length,number=True,special_char=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    
    character=letters
    if number:
        character += digits
    if special_char:
        character += special

    pwd=""
    meets_criteria=False
    has_number=False
    has_special=False
    

    while not meets_criteria or len(pwd) < min_length:

        new_char=random.choice(character)
        pwd += new_char

        if new_char in digits:
            has_number=True
        if new_char in special:
            has_special=True
        
        meets_criteria=True
        if number:
            meets_criteria=has_number
        elif special_char:
            meets_criteria=meets_criteria and has_special
    return pwd

How_many_char=int(input("Enter the minimum length for your password : "))
has_the_number=input("Would like to include numbers in your password? (Yes/no): ").lower() == 'yes'
has_the_Special=input("would like to include special character in your password? (Yes/no): ").lower() == 'yes'
Password=password_generator(How_many_char,has_the_number,has_the_Special)
len_of_pass=len(Password)
print("...Your secure password is ready!...")
print(f"Generated password : {Password}")
print(f"Password length : {len_of_pass}")
print(f"Make sure to save your password securely!")