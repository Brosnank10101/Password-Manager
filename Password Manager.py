#Password Manager Designed And Created By Kelsey Brosnan.

#Importing Modules.

import time
import random
import logging
import os

#Varables, Lists and file creation.

Alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Alpha_UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S' , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


password_combinded = list(Alpha_lower + Alpha_UPPER)

Num = [1,2,3,4,5,6,7,8,9]


Symbol = ['!', '@' , '#' , '$' , '%' , '^' , '&' , '*' , '-' , '+' , '=' , '`' , '~' , '?' , '.' , ';' ,'’' , ':' , '(' ,')' ,'[',']','{','}','/','<','>']

#Creating the Password.txt Save File Using The logging Module.

logging.FileHandler('Passwords.txt')

symbol_vaild = False

num_vaild = False

print("Welcome To Password Manager")
print('')
time.sleep(1)

#The Main Menu Is within a function so the code inside the function can be run as many times as the user wants to.

def main():
    #Global allows varables and lists to be used inside and outside of functions/loops.
    global symbol_vaild
    global num_vaild
    global Generate_Passwords
    global Alpha_lower
    global password_combinded
    global password_length_vaild
    global Alpha_UPPER
    global password
    global Num
    global Symbol

    #password is an empty list since this list is always changing and doesnt require a set list.
    password = []
    time.sleep(1)
    #asks the user if they Would like to Generate a Password or delete their save file or exit the program.
    print('------------------------------')
    print('')
    print("-Would You Like To Generate a Password?: Press G")
    print('')
    print('-Would You Like To Delete Your Saved Passwords?: Press D')
    print('')
    print("-Would You Like To Exit The Program Press E")
    print('')
    time.sleep(1)

  #Asking The To Enter An Input.
    main_input = input("Enter Your Choice: ").lower()

    #Checking If The Users Input Was Valid.
    while main_input.lower() not in ('delete','d', 'del', 'delete saved passwords', 'delete saved passwords?','generate','g','gen', 'generate passwords', 'generate passwords?','e','exit'):
      print("")
      print("Sorry Your Input Was Invaild Please Try Again")
      print("")
      time.sleep(0.5)
      main_input = input("Enter Your Choice: ").lower()
      continue

    #If The Users Input Is Vaild it will continue the program.
    else:
      #This occurs if the user wants to exit the program.
      if main_input.lower in ('e','exit'):
        print('')
        print('Exiting The Program')
        exit()
      #This occurs in the program when the user chooses to Generate a Password.
      if main_input.lower() in ('generate', 'gen', 'generate passwords', 'generate passwords?','g'):
        time.sleep(1)
        print('')
        print('')
        #The user gets to choose how long their password is.
        while True:
          try:
            length_input = int(input("Password Length 8-60: "))
            if length_input in range(8,61):
              pass
            else:
              print("")
              print("Sorry Your Input Was Invaild Please Try Again")
              print("")
              continue
          except ValueError:
            print("")
            print("Sorry Your Input Was Invaild Please Try Again")
            print("")
            continue
            
          password_length = int(length_input)
          #Asks the user if the Would like numbers in their password.
          print('')
          number_input = input("Would You Like Numbers Yes Or No?: ").lower()
          while number_input.lower() not in ('yes','no'):
            print("")
            print("Sorry Your Input Was Invaild Please Try Again")
            print("")
            number_input = input("Would You Like Numbers Yes Or No?: ").lower()
            continue
          else:
            #This occurs in the program when the user chooses to have numbers in their password.
            if number_input == 'yes':
              password_combinded.append(Num)
              num_vaild = True
            elif number_input == 'no':
              pass

            #Asks the user if the Would like symbols in their password.
            print('')
            symbol_input = input("Would You Like Symbols Yes Or No?: ").lower()
            while symbol_input.lower() not in ('yes','no'):
              print("")
              print("Sorry Your Input Was Invaild Please Try Again")
              print("")
              symbol_input = input("Would You Like Symbols Yes Or No?: ").lower()
              continue
            else:
              #This occurs in the program when the user chooses to have numbers in their password.
              if symbol_input == 'yes':
                password_combinded.append(Symbol)
                symbol_vaild = True
              elif symbol_input == 'no':
                pass
            #The main driver code for Generating Passwords.

            password_count = len(password)
            #This while loop checks the length of the password and will keep generating the password until it reaches the password length that user asked for.

            while password_count < (password_length):
              #adding lower case letters.

              password.append(random.choice(Alpha_lower))
              random.shuffle(password)

              #adding UPPER case letters.

              password.append(random.choice(Alpha_UPPER))
              random.shuffle(password)
            
              #checks if the user wanted symbols.

              if symbol_vaild == True:
                random.shuffle(password)
                password.append(random.choice(Symbol))

              #if the user didnt want symbols it continues to the next part of the main driver code.
              elif symbol_vaild == False:
                pass
              # checks if user wanted numbers.
              if num_vaild == True:
                password.append(random.choice(Num))
                random.shuffle(password)
              elif num_vaild == False:
                pass
              #Checks the password length again to see if it shall continue the loop.
              password_count = len(password)
              random.shuffle(password)

            #This acts as a backup just incase the amount of charcters in the password is NOT what the user wanted - if this is the case it works out how much it needs to add or remove and then adds or removes charcters from the password.
            if password_count > password_length:
              #removes items from the list if there are to many.
              password_count -= password_length
              del password [0:password_count]
              random.shuffle(password)
            elif password_count < password_length:
              #adds items if the list doesnt have enough items.
              password_length -= password_count
              for a in range(password_count):
                password.append(random.choice(Alpha_lower))
                random.shuffle(password)
                password.append(random.choice(Alpha_UPPER))
                random.shuffle(password)
            #When the password = the users choosen password length it will exit the loop and prints the password and turns it into a string.
            random.shuffle(password)
            password = ''.join(map(str, password))
            print('')
            print(password)
            print('')
            #Changes the these varables to false so the program works when the main function is called again.
            symbol_vaild = False
            num_vaild = False


            #Asking the user if they would to save their password.
            print('')
            save1_input = input("Would You Like To Save Your Password Yes Or No?: ").lower()
            while save1_input.lower() not in ('yes','no'):
              print("")
              print("Sorry Your Input Was Invaild Please Try Again")
              print("")
              save1_input = input("Would You Like To Save Your Password Yes Or No?: ").lower()
              continue
            else:
              #uses the in bulit Module named file to add the password to the password.txt file.
              if save1_input == 'yes':
                #opens file
                file = open("Passwords.txt", "a")
                file.write('\n' + password)
                #closes file
                file.close()
                print('')
                #Asks the user if they would like to save a message about their password to help them renember what its for.
                save2_input = input("Would You Like To Save A Message\nAbout Your Password Yes Or No?: ")
                print('')
                while save2_input.lower() not in ('yes','no'):
                  print("")
                  print("Sorry Your Input Was Invaild Please Try Again")
                  print("")
                  save2_input = input("Would You Like To Save A Message\nAbout Your Password Yes Or No?: ").lower()
                  print('')
                  continue
                else:
                  #this occurs if the user wants to save a message.
                  if save2_input == 'yes':
                    #the user enters their message here
                    message = input("Enter Your Message: ")
                    file = open("Passwords.txt", "a")
                    file.write(" - ")
                    #Appending the message to the password and saving it to the Passwords.txt file.
                    file.write(message + '\n')
                    file.close()
                    print('')
                    print("Password Saved")
                    print('')
                    print('You Can Find Your Password Saved In The Password.txt File')
                    main()

                  elif save2_input == 'no':
                    #If the user doesnt want to save a message this occurs.
                    file = open("Passwords.txt", "a")
                    file.write('\n')
                    file.close()
                    print('')
                    print("Password Saved")
                    print('')
                    print('You Can Find Your Password In The Password.txt file')
                    main()


              elif save1_input == 'no':
                #if the user doesnt want to save a password what so ever.
                main()
                break
            main
            break
              
         
      #Deleting Saved Passwords
      elif main_input.lower() in ('delete', 'del','d', 'delete saved passwords','delete saved passwords?'):
        #os.remove - Removes the Password Save file
        os.remove("Passwords.txt")
        print('')
        print("Saved Passwords Deleted")
        print('')
        time.sleep(1)
        print("")
        #Uses logging Module to recreate the Passwords.txt file.
        logging.FileHandler('Passwords.txt')
        main()
      #This exits the program
      if main_input.lower in ('e','exit'):
        print('')
        print('Exiting The Program')
        exit()

#This starts the program
main()
