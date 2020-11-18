from colorama import Fore


number = int(input(Fore.BLUE + 'How many numbers would you like to find the average of: '))
total_calc = 0

for n in range(number):
    numbers = float(input(Fore.CYAN + 'Enter number: '))
    total_calc += numbers

avgerage = total_calc/number
print(Fore.GREEN + 'Average of ', number, ' numbers is: ', avgerage)
