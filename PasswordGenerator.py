####################### PROJECT INFORMATION ##########################
# My personal password generator program
# Author: Mainuddin Alam Irteja
######################################################################

# Important modules for the program
import string
import random

# Global variables
alphabets = list(string.ascii_letters)  
numbers = list(string.digits)
specialChar = list(string.punctuation)

###################### PROJECT FUNCTIONS ############################## 

"""
Function to get the company name and user name.

@returns getCompanyName The name of the company
@returns getUserName The name of the user
@returns existingFileName The name of the password storage file
@returns countLines The number of lines in the file
"""
def promptGeneralInfo() -> tuple:
    countLines = 1
    # Get the general info
    existingFileName = "passwordStoreV1"
    getCompanyName = input("Please input the name of the company: ")
    getUserName = input("Please input your username: ")
    doesFileExist = input("Do you have a secret file to store your passwords? Enter yes or no: ")
    # If file exists, get the file name
    if doesFileExist == "yes":
        existingFileName = input("Give the name of your password storage file: ")
        getFile = open(existingFileName, "r")
        countLines = len(getFile.readlines())
        getFile.close()
    # If file does not exist, just create the file
    if doesFileExist == "no":
        createFile = open(existingFileName, "w")
        createFile.write("No.\t\t\tUsername\t\t\tCompany\t\t\tPassword")
        createFile.close()
        
    return getCompanyName, getUserName, existingFileName, countLines

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
            password += random.choice(alphabets)
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
            print("\nMake sure your given password contains letters, numbers and special characters.\nPassword letter length must be atleast 8 characters.\nMust be 6 letters.\nMust have 1 number.\nMust have 1 special character")
            password = input("Enter your password: ")
            # Check whether the given password is valid or not
            isValid = checkPassword(password)
    return password

"""
Function to add new password to the file.

Args:
    givenCompany (str): The company name given by the user
    givenUserName (str): The user name given by the user
    givenFileName (str): The file name given by the user
"""
def insertNewPassword(givenCompanyName : str, givenUserName : str, givenFileName : str, coLine: int) -> None:
    # Generate a new password and add it to the list
    openFile = open(givenFileName, "a")
    getNewPassword = generatePassword()
    print("\nThe new password has been generated and added to the list.")
    openFile.write(f"\n{coLine}\t\t\t{givenUserName}\t\t\t{givenCompanyName}\t\t\t{getNewPassword}")
    openFile.close()
    
"""
Function to update a password in the file.

Args:
    givenCompany (str): The company name given by the user
    givenUserName (str): The user name given by the user
    givenFileName (str): The file name given by the user
"""
def updatePassword(givenCompanyName : str, givenUserName : str, givenFileName : str) -> None:
    ...

"""
Function to check the password given by the user

Args:
    givenPassword (str): The password given by the user
@returns Whether the password is valid
"""
def checkPassword(givenPassword : str) -> bool:
    allConditionsMet = False
    # Creating local variables to track the count of the different symbols
    letterCount = 0
    numCount = 0
    spCharCount = 0
    # Track and check if all the conditions have met
    for i in givenPassword:
        if i.isalpha():
            letterCount += 1
        if i.isdigit():
            numCount += 1
        if i in specialChar:
            spCharCount += 1
    if len(givenPassword) >= 8 and letterCount >= 6 and numCount >= 1 and spCharCount >= 1:
        allConditionsMet = True
    # Return the validity of the password
    return allConditionsMet

############################ MAIN CODE #####################################

# Get the general information from the user
cName, uName, eFile, cLines = promptGeneralInfo()
userQuery = """
    What would you like to do?
    
    1) Generate a new password for that company
    2) Update the existing password
    3) Exit the program
    """
print(userQuery)
# Get the desired choice of the user
userChoice = int(input("Please select either 1, 2, or 3: "))
if userChoice == 1:
    insertNewPassword(cName, uName, eFile, cLines)
elif userChoice == 2:
    updatePassword(cName, uName, eFile, cLines)
else:
    exit()