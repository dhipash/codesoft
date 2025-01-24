import string
import random
len=int(input("Enter password length: "))
print('''choose character set for password from these :
      1. Digits
      2. letters
      3. Special characters
      4. Exit''')
charalist=""
while True:
    choice=int(input("Pick a number:"))
    if choice==1:
        charalist += string.ascii_letters
    elif choice==2:
        charalist += string.digits
    elif choice==3:
        charalist += string.punctuation
    elif choice==4:
        break
    else:
        print("Please pick a valid option!")
password=[]
for i in range(len):
    randomchar=random.choice(charalist)
    password.append(randomchar)
print("the random password is"+"".join(password))
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
user=input("how many character do you want in your password?")
while True:
 
    try:
 
        characters_number = int(user)
 
        if characters_number < 8:
 
            print("Your number should be at least 8.")
 
            user = input("Please, Enter your number again: ")
 
        else:
 
            break
 
    except:
 
        print("Please, Enter numbers only.")
 
        user = input("How many characters do you want in your password? ")
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))
result = []
 
for x in range(part1):
 
    result.append(s1[x])
    result.append(s2[x])
 
for x in range(part2):
 
    result.append(s3[x])
    result.append(s4[x])
random.shuffle(result)
password = "".join(result)
print("Strong Password: ", password)
