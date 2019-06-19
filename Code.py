'''
Name: Code.py

Purpse: A story game based on basic computer knowledge

Author: Lisa.Tan

Created: 17/06/2019
'''
press_Yes = True

print("You are awakened from an unknown closed room with a laptop and some computer components")
print("You walked up to the computer and see a note on the screen")

print("\n\"In order to exit the room, you must complete some requirements.\"")
press_bottom = input("Press Yes or No to continue：")

if press_Yes and press_bottom == "Yes" or press_bottom == "yes":
    print("\nHere are you requirements")
else:
    print("Too bad, you have to continue. :)")


# First Requirement
print("\nYour first requirement will be: ")
print("\"Enter and Check the storage of this computer.\"")
print("(Hint: The storage of this computer is 250GB)")

storage_first_requirement = input("The storage of this computer: ")

while storage_first_requirement != "250GB":
    print("This is not the correct storage of the computer.")
    storage_first_requirement = input("The storage of this computer: ")

print("Congratulations, You have completed 1 requirement!")

# Second Requirement
print("\nYour second requirement will be: ")
print("\"What can you do to upgrade the temporary storage of the computer?\"")
print("(Hint: Use the computer components beside to help yourself)")

print("\nHere are your available options")
print("a. RAM sticks")
print("b. Hard Drive")
print("c. Graphics Card")
print("d. Monitor")

choice_second_requirement = input("What is your choice: ")

while choice_second_requirement != "a" and choice_second_requirement != "RAM sticks":
    print("Wrong choice! Please Try again.")
    choice_second_requirement = input("What is your choice: ")
print("Congratulations, You have completed 2 requirement!")

# Third Requirement
print("\nHere is your third requirement.")
print("\"This is a computer with a old graphics card\"")
print("What would you do to improve the frame rates and higher resolution of this computer?")

print("\nHere are your available options: ")
print("a. New Motherboard")
print("b. New DSL Modern")
print("c. New Monitor")
print("d. Upgrade the Graphics Card")

choice_third_requirement = input("What is your choice: ")

while choice_third_requirement != "d" and choice_third_requirement != "Upgrade the Graphics Card":
    print("Wrong choice! Please Try again.")
    choice_third_requirement = input("What is your choice: ")
print("Congratulations, You have completed 3 requirement!")

# Fourth Requirement
print("\nHere is your fourth requirement")
print("\"This will be your last requirement before some variables and data-types practice\"")
print("The internet is slow right now. Which, you are not able to accesses the practice questions")
print("What would you do to improve on the internet speed?")

print("\nHere are your available options: ")
print("a. A better mouse")
print("b. A better keyboard")
print("c. A better ISP")
print("d. A better RAM")

choice_fourth_requirement = input("What is your choice: ")

while choice_fourth_requirement != "c" and choice_fourth_requirement != "A better ISP":
    print("Wrong choice! Please Try again.")
    choice_fourth_requirement = input("What is your choice: ")
print("Congratulations, You have completed 4 requirement!")

# Practice
print("\nCongratulations, you have successfully improved your internet speed")
print("Now, it is time for some basic variable and data-types practice!")

print("\nThe most common data types that we generally use are \"str\", \"int\", and \"float\"")

# Q1
print("\nWhich data type out of the three listed is used for pure string letters, symbols, and numbers?")
data_type_q1 = input("What is your answer: ")

while data_type_q1 != "str":
    print("Wrong answer! Please Try again.")
    data_type_q1 = input("What is your answer: ")
print("Congratulation, you got the correct answer")

# Q2
print("Here is your next question: ")
print("\nWhich data type out of the three listed is used for pure non-decimal integer value?")
data_type_q2 = input("What is your answer: ")

while data_type_q2 != "int":
    print("Wrong answer! Please Try again.")
    data_type_q2 = input("What is your answer: ")
print("Congratulation, you got the correct answer")

# Q3
print("\nHere is a question about variable naming")
print("Here is your example, you are acquired to give the proper variable naming")
print("\ngreeting = \"Hello World\"")

print("\nWhat is the variable name for \'greeting\' inside the example?")
print("\"Hint here are are some available choices: \"")
print("a. Name")
print("b. Value")
print("c. Str")

variable_naming_q1 = input("\nWhat is your answer: ")

while variable_naming_q1 != "a" and variable_naming_q1 != "Name":
    print("Wrong answer! Please Try again.")
    variable_naming_q1 = input("What is your answer: ")
print("Congratulation, you got the correct answer")

# Q4
print("\nHere is your next question")
print("What is the variable name for \'Hello World\' inside the example?")

variable_naming_q2 = input("\nWhat is your answer: ")

while variable_naming_q2 != "b" and variable_naming_q1 != "Value":
    print("Wrong answer! Please Try again.")
    variable_naming_q2 = input("What is your answer: ")
print("Congratulation, you got the correct answer")

# Q5
print("\nHere is your last question about variable naming: ")
print("what data-type is this example?")

variable_naming_q3 = input("\nWhat is your answer: ")

while variable_naming_q3 != "c" and variable_naming_q1 != "Str":
    print("Wrong answer! Please Try again.")
    variable_naming_q3 = input("What is your answer: ")
print("Congratulation, you got the correct answer")


print("\nNow, you have successfully completed the basic variable and data-types practice")
print("It is time for the last section of your requirements")

print("\nHere is a data file that contains the password to enter later on for you to exit this room")
print("And here is a link that you can use to get on a \'website\'")

print("\nWhat is your decision? Go on the website or Complete another practice questions to enter the data file?")
print("Your option: ")
print("Go on the website")
print("Complete another practice questions")

user_input = input("\nWhat is your decision: ")

while user_input == "Go on the website" and user_input != "Complete another practice questions":
    print("You have clicked on a link that contains a worm virus")
    print("and this worm virus has duplicate itself and destroyed your data files")
    print("but because you have done well in the previous requirements, I have fixed the file for you and installed a "
          "fire wall")
    print("Be careful on what you are clicking next time!")
    user_input = input("\nWhat is your decision: ")
print("Congratulations! You made a wise decision to avoid a virus danger.")


print("\nNow, in order to receive your password you must list one answer towards the three topics below. The answer may"
      "vary")
print("\nNo.1 How can we improve on reducing negative effects of computers on our environment?")
use_input_environment = input("What is your way of reducing negative effects cost to the environment: ")

print("\nNo.2 What could be some requirements to enter a computer science program in a university?")
use_input_program_requirement = input("Some requirements to get in the program could be: ")

print("\nNo.3 What could be an ethical issue relating to computer")
user_input_ethical_issue = input("Example of an ethical issue could be: ")

print("\nThx for your participation. Here is your password to exit: Dream Exit")
print("\"End Dream\"")
print("(\"This was a dream you once had before a computer science test\")")


