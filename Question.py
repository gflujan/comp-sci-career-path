from levels import levels
import time

class Question:
   # 'cfa' stands for 'check final answer'
   cfa_tries = 0

   def __init__(self, question_level):
      self.data = levels[question_level]
      self.level = question_level

   def ask_question(self):
      print(self.data['question'])

   def check_final_answer(self):
      is_final_input = input('Is that your final answer? ([y]es or [n]o): ')

      if is_final_input.lower() == 'yes' or is_final_input.lower() == 'y':
         return 'yes'
      elif is_final_input.lower() == 'no' or is_final_input.lower() == 'n':
         print()
         print('Okay, you can change your answer one time.')
         return 'no'
      else:
         print("You entered an unknown value. We'll just take this as your final answer. ;-)")
         return 'yes'

   def intro(self):
      print(self.data['intro'])

   def is_valid_answer(self, answer):
      return answer == 'a' or answer == 'b' or answer == 'c' or answer == 'd'

   def process(self):
      print('——————————————————————————————————————————\n')
      self.intro()
      self.ask_question()
      print()
      self.show_choices()
      print()
      return self.process_answer()

   def process_answer(self):
      player_input = input("My answer is [pick 'A', 'B', 'C', or 'D']: ")
      self.player_answer = player_input.lower()

      if self.player_answer == 'walk':
         return 'walk'
      elif self.is_valid_answer(self.player_answer):
         if self.cfa_tries == 0:
            is_final_answer = self.check_final_answer()
         else:
            is_final_answer = 'yes'

         if is_final_answer == 'yes':
            time.sleep(3)
            final_result = self.verify_answer()
            print()

            if final_result == True:
               print('Heyo, you got it right!\n')
               return 'succeeded'
            elif final_result == False:
               print("D'oh, that is incorrect.\n")
               return 'failed'
         elif is_final_answer == 'no':
            self.cfa_tries += 1
            return self.process_answer()
      else:
         print('You have entered an incorrect value. Please try again.\n')
         self.process_answer()

   def show_choices(self):
      print(self.data['choices'])

   def verify_answer(self):
      actual_answer = self.data['answer']
      selected_answer = self.data['choices'][self.player_answer]
      return actual_answer == selected_answer
