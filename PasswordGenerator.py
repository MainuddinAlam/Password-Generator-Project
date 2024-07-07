# My personal password generator program
# Author: Mainuddin Alam Irteja

"""
Function to get the company name and user name.

@returns getCompanyName The name of the company
@returns getUserName The name of the user
@returns existingFileName The name of the password storage file
"""
def promptGeneralInfo() -> tuple:
    existingFileName = "passwordStoreV1"
    getCompanyName = input("Please input the name of the company: ")
    getUserName = input("Please input your username:")
    doesFileExist = input("Do you have a secret file to store your passwords? Enter yes or no: ")
    if doesFileExist == "yes":
        existingFileName = input("Give the name of your password storage file: ")
    return getCompanyName, getUserName, existingFileName


def generatePassword() -> str:
    password = ""
    #add algorithm

    return password

def insertNewPassword():
    ...


def deletePassword():
    ...


def updatePassword():
    ...


def checkPassword():
    ...

# Get the general information from the user
companyName, uName, eFile = promptGeneralInfo()