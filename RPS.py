from random import randint

c = ['Rock', 'Paper', 'Scissors']
computer = c[randint(0, 2)]
player_score = 0
computer_score = 0
game = 'y'
player = input('Welcome to Rock, Paper, Scissors. Select an option: ')

def player_win(): # If the player wins the round
   global player
   global computer
   global player_score
   global computer_score
   if player_score < 3:
      computer = c[randint(0, 2)]
      player = input('Pick another option: ')
   elif player_score == 3:
      print('Congratulations! You won! :)')
      game = input('Do you want to play again? (y = yes) ')
      if game == 'y':
         player_score = 0
         computer_score = 0
         player = input('Welcome to Rock, Paper, Scissors. Select an option: ')
      elif game == 'n':
         game_over()
      else:
         game = input('Please select y or n: ')

def player_lose(): # If the player loses the round
   global player
   global computer
   global player_score
   global computer_score
   if computer_score < 3:
       computer = c[randint(0, 2)]
       player = input('Pick another option: ')
   elif computer_score == 3:
      print('You lost! :(')
      game = input('Do you want to play again? (y = yes, n = no) ')
      if game == 'y':
         player_score = 0
         computer_score = 0
         player = input('Welcome to Rock, Paper, Scissors. Select an option: ')
      elif game == 'n':
         game_over()
      else:
         game = input('Please select y or n: ')

def player_draw():  # If the round is a draw
   global player
   global computer
   global player_score
   global computer_score

   computer = c[randint(0, 2)]
   player = input('Pick another option: ')

def game_over(): # Occurs if the player selects 'n' when asked to play again
   print('Thanks for playing!')

while (player_score and computer_score) < 3 and game == 'y': # First to 3 points wins       
   if player == computer:
      print("It's a draw!")
      print("Player Score:", player_score, " Computer Score:", computer_score)
      player_draw()
   if player == 'Rock' and computer == 'Scissors': 
      player_score += 1
      print('You win! ' + player + ' smashes ' + computer.lower() + '.')
      print("\nPlayer Score:", player_score, " Computer Score:", computer_score)
      player_win()
   if player == 'Rock' and computer == 'Paper':
      computer_score += 1
      print('You lose! ' + computer + ' covers '+ player.lower() + '.')
      print("\nPlayer Score:", player_score, " Computer Score:", computer_score)      
      player_lose()
   if player == 'Paper' and computer == 'Rock': 
      player_score += 1
      print('You win! ' + player + ' covers ' + computer.lower() + '.')
      print("\nPlayer Score:", player_score, " Computer Score:", computer_score)      
      player_win()
   if player == 'Paper' and computer == 'Scissors':
      computer_score += 1 
      print('You lose! ' + computer + ' cuts ' + player.lower() + '.')
      print("\nPlayer Score:", player_score, " Computer Score:", computer_score)      
      player_lose()
   if player == 'Scissors' and computer == 'Paper':
      player_score += 1
      print('You win! ' + player + ' cuts ' + computer.lower() + '.')
      print("\nPlayer Score:", player_score, " Computer Score:", computer_score)
      player_win()
      if player == 'Scissors' and computer == 'Rock':
         computer_score += 1
         print('You lose! ' + computer + ' smashes ' + player.lower() + '.')
         print("\nPlayer Score:", player_score, " Computer Score:", computer_score)      
         player_lose()
