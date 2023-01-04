print('Once upon a time...')

######
# TREENODE CLASS
######
class TreeNode:

  def __init__(self, story_piece):
    # print('Creating a new TreeNode instance...')
    self.choices = []
    self.story_piece = story_piece
  #fed

  def add_child(self, node):
    self.choices.append(node)
  #fed

  def traverse(self):
    story_node = self
    print(story_node.story_piece)
  #fed
#ssalc

######
# VARIABLES FOR TREE
######
story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!

Do you:
1 ) Roar back! 
2 ) Run to the left...
""")

choice_a = TreeNode("""
The bear is startled and runs away.

Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode("""
You come across a clearing full of flowers.
The bear follows you and asks 'what gives?'

Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

# user_choice = input('What is your name?\n')
# print('Hi, ' + user_choice + '!')

######
# TESTING AREA
######
story_root.add_child(choice_a)
story_root.add_child(choice_b)
# print(story_root.story_piece)
story_root.traverse()
