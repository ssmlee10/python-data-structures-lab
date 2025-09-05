# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  example_list = ['fountain pen', 'ink', 'pen case']
  example_list.append('ink cartridge')
  example_list.append('planner')
  example_list.append('pencil')
  for element in example_list:
      print(element)

example_list_function()

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
  student_list = ['Spongebob', 'Squidward', 'Patrick']
  first_student = student_list[1]
  last_student = student_list[-1]
  return first_student, last_student

print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
  foods = ('kimbap', 'bibimbap', 'japchae')
  meal = ''

  for food in foods:
     meal += food + ', '

  return meal.rstrip(', ')
     
print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
  foods = ('kimbap', 'ddeokbokki', 'bibimbap', 'japchae')
  last_two_foods = foods[-2:]
  return last_two_foods

print('Exercise 3:', slice_foods())
