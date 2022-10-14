import dollar_sign as ds
import instructions as ins
from levels import levels
from Question import Question

# ==========================================================================
# MAIN GAME KICKOFF LOGIC
# ==========================================================================
def start_game():
   current_level = 1
   is_retry = False
   num_strikes = 0
   total_money_won = 0

   print(ds.dollar_sign)
   print('——————————————————————————————————————————')
   print('Welcome to "Who Wants to be a Millionaire!"')
   print('——————————————————————————————————————————\n')

   player_name = input('What is your name? ')
   print()

   money_response = input(f'Hi, {player_name}! Are you ready to win some money?! ([y]es or [n]o): ')
   print()

   if money_response.lower() == 'yes' or money_response.lower() == 'y':
      print("Awesome! Let's get started!")
      print()
   elif money_response.lower() == 'no' or money_response.lower() == 'n':
      print("Well, too bad! You're gonna win some anyway! (maybe)\n")
   else:
      print("I don't know what you said, but we're gonna play anyway. :-P \n")

   print("DISCLAIMER: This isn't ACTUAL money, it's just pretend. I don't owe you anything. ;-D\n")

   while num_strikes < 3:
      if current_level == 1 and is_retry != True:
         knows_how_to_play = input('Do you already know how to play? ([y]es or [n]o): ')
         print()

         if knows_how_to_play.lower() == 'yes' or knows_how_to_play.lower() == 'y':
            print("Cool! Let's play Millionaire!!!\n")
         else:
            ins.print_instructions()

      current_question = Question(current_level)
      result = current_question.process()

      if result == 'walk':
         print()
         print("You're done? Alright. Well, we hate to see you go, but we love to watch you leave. ;-)")
         print("Don't fake spend it all in one place!\n")
         break
      elif result == 'succeeded':
         total_money_won = levels[current_level]['value']
         current_level += 1
         is_retry = False
      elif result == 'failed':
         num_strikes += 1
         ns_display = "strike" if num_strikes == 1 else "strikes"
         print(f'You have {num_strikes} {ns_display}. But we are going to try again. :-)')
         is_retry = True

      print('- Current Winnings: $' + '{:,}'.format(total_money_won))
      print('- Total Strikes: ' + str(num_strikes) + '\n')

   print('Total Winnings: $' + '{:,}'.format(total_money_won))
   print("Final Strikes: " + str(num_strikes))

# ==========================================================================
# LET'S GO!!!
# ==========================================================================
start_game()
