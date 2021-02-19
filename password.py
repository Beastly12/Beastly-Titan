import re 

print("Welcome pepple to  games.co ")


password= input(" Enter your password:  ")
pass_len=len(password)
def pass_validator(password):
  if  re.search  ('[!@#$%&*?/><_|~`?;%]',password):
      print('you cant use symbols in your password ')
      return False
  elif not re.search ('[0-9]',password):
      print('you have to use a number in your password ')
      return False
  elif pass_len < 5 :
    print ("Your password is very weak")
    print(f"""The password should be atleast 8 characters 
    :( --  """   ) 
    return False
  elif pass_len >=5 and pass_len < 8:
    print("Your password is weak")
    print(f"""The password should be atleast 8 characters 
    :( --  """   ) 
    return False
  elif pass_len >= 8 :
    print('your password is: ',password )  
    password2=input("Enter password again for confirmation:    ")
    if  password == password2 :
      print("Your password has been set;")    
      return True     
    elif password != password2 : 
        print("Wrong password")
        print('input the password correctlyt this time')
        return False

while not pass_validator(password):
    password= input("Enter password: ")  
    password2=input("Enter Password again for confirmation")


    
password3 = input("Enter your set  password to play * The guess it Game *  ")     
if  password3 == password2: #REMEMBER TO USE THE ELIF AT THE END MY GUY 
    print("You have to guess the answers correctly to win this game, you get 1 points for Every correct answer ")
    

from random import randint
import re

points = 0 
num_guess=0
game_over= False
hidden_num=randint(0,10)

while not game_over:
    guess_nums= int(input("Guess a number from 0 to 10: "))
    if guess_nums==hidden_num: 
        points=points+1
        num_guess=0
        print("The correct number is: " ,hidden_num)
        print(" Your have " , points,"points " )
        print('--------------\n\n')
        
    else:
        if num_guess== 4:
            print("Game over-------- :( ")
            print(" The hidden number was: " , hidden_num)
            print("Total points: " , points )
            game_over=True
        else:
            num_guess=num_guess+1
            print("Remainig Tries: " , (4-num_guess)+1) 


    


