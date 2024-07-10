# My personal password generator program
# Author: Mainuddin Alam Irteja

# Important modules for the program
import string
import random

alphabets = list(string.ascii_letters)  
numbers = list(string.digits)
specialChar = list(string.punctuation)

"""
Function to get the company name and user name.

@returns getCompanyName The name of the company
@returns getUserName The name of the user
@returns existingFileName The name of the password storage file
"""
def promptGeneralInfo() -> tuple:
    existingFileName = "passwordStoreV1"
    getCompanyName = input("Please input the name of the company: ")
    getUserName = input("Please input your username: ")
    doesFileExist = input("Do you have a secret file to store your passwords? Enter yes or no: ")
    if doesFileExist == "yes":
        existingFileName = input("Give the name of your password storage file: ")
    return getCompanyName, getUserName, existingFileName

"""
Function to generate password

@returns password The generated password
"""
def generatePassword() -> str:
    password = ""
    askUser = """
    Would you like us to generate a password or make your own? 

    1) Press 1 to generate
    2) Press 2 to make your own
    
    """
    print(askUser)
    # Check what user has chosen
    getPrompt = int(input("Choose 1 or 2: "))
    # Generate the random password
    if getPrompt == 1:
        # Add the letters
        for i in range(6):
            password.append(random.choice(alphabets))
        # Add a random number in a random place of the password string
        ranNum = random.choice(numbers)
        index = random.randint(0, len(password))
        password = password[:index] + ranNum + password[index:]
        # Add a special character in a random place
        ranSpChar = random.choice(specialChar)
        index2 = random.randint(0, len(password))
        password = password[:index2] + ranSpChar + password[index2:]
        
    # Get the user given password
    if getPrompt == 2:
        isValid = False
        while isValid == False:
            # Let important details be known to the user
            print("Make sure your given password contains letters, numbers and special characters.\nPassword letter length must be atleast 8 characters.\nMust be 6 letters.\nMust have 1 number.\nMust have 1 special character")
            password = input("Enter your password: ")
            # Check whether the given password is valid or not
            isValid = checkPassword(password)
    return password

def insertNewPassword():

    ...


def deletePassword():
    ...


def updatePassword():
    ...

"""
Function to check the password given by the user

Args:
    givenPassword (str): The password given by the user
@returns Whether the password is valid
"""
def checkPassword(givenPassword: str) -> bool:
    allConditionsMet = False
    # Creating local variables to track the count of the different symbols
    letterCount = 0
    numCount = 0
    spCharCount = 0
    # Track and check if all the conditions have met
    for i in givenPassword:
        if givenPassword[i].isalpha():
            letterCount += 1
        if givenPassword[i].isdigit():
            numCount += 1
        if givenPassword[i] in specialChar:
            spCharCount += 1
    if len(givenPassword) >= 8 and letterCount >= 6 and numCount >= 1 and spCharCount >= 1:
        allConditionsMet = True
    # Return the validity of the password
    return allConditionsMet



# Get the general information from the user
cName, uName, eFile = promptGeneralInfo()
userQuery = """
    What would you like to do?
    
    1) Generate a new password for that company
    2) Update the existing password
    3) Delete the existing password 
    4) Exit the program
    """
print(userQuery)
# Get the desired choice of the user
userChoice = int(input("Please select either 1, 2, 3 or 4: "))
if userChoice == 1:
    insertNewPassword(cName. uName, eFile)
elif userChoice == 2:
    updatePassword(cName. uName, eFile)
elif userChoice == 3:
    deletePassword(cName. uName, eFile)
else:
    exit()