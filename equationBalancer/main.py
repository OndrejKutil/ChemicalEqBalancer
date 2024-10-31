from balancer import EquationBalancer

#! add comments to the functions
def display_welcome_screen():
      print('Welcome to the Equation Balancer!')
      print('This program helps you balance chemical equations.')
      print('')
      print('Instructions:')
      print('1. Enter a chemical equation when prompted.')
      print('2. Input is case sensitive.')
      print('3. Use "->" to separate reactants and products.')
      print('4. Use "+" to separate molecules.')
      print('5. You can use spaces between molecules and atoms.')
      print('')
      print('Example input 1: H2 + O2 -> H2O')
      print('Example input 2: NaCl + AgNO3 -> NaNO3 + AgCl')
      print('')

def prompt_user_for_equation():
      return input('Enter your equation: ')

display_welcome_screen()

balancer = EquationBalancer()

while True:
    equation = prompt_user_for_equation()
    solution, exitCode = balancer.balanceEquation(equation)
    if exitCode == 0:
        print('')
        print(f'Balanced equation: {solution}')
        print('')
    else:
        print('')
        print(solution)
        print('')
        continue

    while True:
        another = input('Do you want to balance another equation? (y/n): ')
        if another.lower() == 'n':
            print('Thank you for using the Equation Balancer. Goodbye!')
            exit(1)
        elif another.lower() == 'y':
            break
        else:
            print('Invalid input. Please enter "y" or "n".')
