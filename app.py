class Invalid(Exception):
   pass
import random
def Game():
    User_score=0
    computer_score=0
    print('===========================\n     Welcome to Game   \n===========================')
    print('Choose your option \n🪨  ==>Rock \n🗞️  ==>Paper \n✂️  ==>Scissor\n')
    List=['🪨 Rock','🗞️ Paper','✂️ Scissor']
    while True:
      try:
        user=input('\n User Choose : ').capitalize()
        if user=='' or user==' ':
          raise Invalid(' 🚨 option Invalid ')
        Computer=random.choice(List)
        print('\nComputer Choose : ',Computer,"\n")
        if user=="Rock" and Computer=="🪨 Rock":
         print('🪨 Rock V/S 🪨Rock ==> 🪨')
         print('Result : Tie')
        elif user=="Rock" and Computer=='✂️ Scissor':
         print('🪨 Rock V/S ✂️ Scissor ==> 🪨\n')
         print('Result : User is win ')
         User_score+=1
        elif user=="Rock" and Computer=='🗞️ Paper':
         print('🪨 Rock V/S 🗞️ Paper ==> 🗞️\n')
         print("Result : Computer is win ")
         computer_score+=1
        elif user=="Scissor" and Computer=='✂️ Scissor':
         print('✂️ Scissor V/s ✂️ Scissor ==> ✂️\n')
         print('Result : Tie')
        elif user=="Scissor" and Computer=='🪨 Rock':
         print('✂️ Scissor V/S 🪨 Rock ==> 🪨\n')
         print('Result : Computer is win')
         computer_score+=1
        elif user=="Scissor" and Computer=='🗞️ Paper':
         print('✂️ Scissor V/S 🗞️ Paper ==> ✂️\n')
         print('Result : User is win')
         User_score+=1
        elif user=="Paper" and Computer=='🗞️ Paper':
         print('🗞️ Paper V/S 🗞️ Paper ==> 🗞️\n')
         print('Result : Tie')
        elif user=="Paper" and Computer=='✂️ Scissor':
         print('🗞️ Paper V/S ✂️ Scissor ==> ✂️\n')
         print('Result : Computer is win ')
         computer_score+=1
        elif user=="Paper" and Computer=='🪨 Rock':
         print('🗞️ Paper V/S 🪨 Rock ==> 🗞️\n')
         print('Result : User is win ')
         User_score+=1
        else :
         print('user invalid Data Entered\n')
         print('=========\nSCORE\n=========')
         print('User Score     :' ,User_score)
         print('Computer Score :' ,computer_score)
         if User_score>computer_score:
           print('=========\n📊 Result\n=========\n==>User  Win The Game') 
         elif User_score<computer_score :
           print('=========\n📊 Result\n=========\n==>Computer  Win The Game')
         else :
               ('\nThe Game is Tie ')
         play=input('\nDo you want play again 🤔 ? Y/N : ')
         if play=='Y' or play=="y":
           continue
         else :
           print('\nThanks for playing .')
           break
      except Invalid as e:
        print("error",e)
        
Game()

