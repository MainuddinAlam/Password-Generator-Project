# My personal password generator program
# Author: Mainuddin Alam Irteja

# Important modules for the program
import string


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
    if getPrompt == 1:
        ...
    if getPrompt == 2:
        isValid = False
        # Let important details be known to the user
        print("Make sure your given password contains letters, numbers and special characters.\nPassword letter length must be atleast 8 characters.\nMust be 6 letters.\nMust have 1 number.\nMust have 1 special character")
        password = input("Enter your password: ")
        # Check whether the given password is valid or not
        while isValid == False:
            isValid = checkPassword(password)
    return password

def insertNewPassword():

    ...


def deletePassword():
    ...


def updatePassword():
    ...


def checkPassword(givenPassword) -> bool:
    ...

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