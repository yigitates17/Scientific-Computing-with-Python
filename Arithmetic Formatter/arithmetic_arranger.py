def arithmetic_arranger(problems, results=False):

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    temp = problem.split()

    if len(temp[0]) > 4 or len(temp[2]) > 4:
      return "Error: Numbers cannot be more than four digits." 

    if temp[1] not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."
  
  for problem in problems:
    temp = problem.split()
    if temp[0].isdigit() == False:
      return "Error: Numbers must only contain digits."
    elif temp[2].isdigit() == False:
      return "Error: Numbers must only contain digits."

  list_1 = []
  list_2 = []
  operators = []
  final_list = []
  digit_diff = []
  len_diff = []

  for problem in problems:
    problem = problem.split()
    list_1.append(problem[0])
    list_2.append(problem[2])
    operators.append(problem[1])
    if problem[1] == '+':
      final_list.append(str(int(problem[0]) + int(problem[2])))
    else:
      final_list.append(str(int(problem[0]) - int(problem[2])))

  for index in range(len(list_1)):
    digit_diff.append(abs(len(list_1[index]) - len(list_2[index])))
    len_diff.append(max(len(list_1[index]), len(list_2[index]))+2)

  first_line = []
  second_line = []
  third_line = []
  fourth_line = []

  first = ""
  second = ""
  third = ""
  fourth = ""

  for i in range(len(list_1)):
    first_line.append(first.rjust(len_diff[i] - len(list_1[i]), ' ') + str(list_1[i]) + first.rjust(4, ' '))
    second_line.append(operators[i] + second.rjust((len_diff[i]-1)-len(list_2[i]), ' ') + str(list_2[i]) + second.rjust(4, ' '))
    third_line.append(len_diff[i] * '-' + third.rjust(4, ' '))
    fourth_line.append(fourth.rjust(len_diff[i] - len(final_list[i]), ' ') + final_list[i] + fourth.rjust(4, ' '))
                            
  first = first.join(first_line).rstrip(' ')
  second = second.join(second_line).rstrip(' ')
  third = third.join(third_line).rstrip(' ')
  fourth = fourth.join(fourth_line).rstrip(' ')

  arranged_problems = first + "\n" + second + "\n" + third
  
  if results == True:
    arranged_problems += "\n" + fourth

  return arranged_problems
