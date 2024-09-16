import random

player_inputs_list = []

player_score = 0
computer_score = 0

def prediction():
  count_zero = player_inputs_list.count(0)
  count_one = player_inputs_list.count(1)
  if count_zero > count_one:
    predict = 0
  elif count_zero < count_one:
    predict = 1
  else:
    predict = random.randint(0,1)
  return predict

def update_scores(predicted, player_input):
  global player_score, computer_score
  if predicted == player_input:
    computer_score = computer_score + 1
    print("Computer Score:", computer_score)
    print("Player Score:", player_score)
  else:
    player_score = player_score + 1
    print("Computer Score:", computer_score)
    print("Player Score:", player_score)

def gameplay():
  valid_entries = ['0', '1']
  while True:
    predicted = prediction()
    player_input = input("Enter either 0 or 1: ")
    while player_input not in valid_entries:
      print("Invalid Input!")
      player_input = input("Please enter either 0 or 1: ")

    player_input = int(player_input)
    player_inputs_list.append(player_input)
    update_scores(predicted, player_input)

    if player_score == 5:
      print("Congrats, You Won!")
      break
    elif computer_score == 5:
      print("Bad Luck, You Lost!")
      break

gameplay()
