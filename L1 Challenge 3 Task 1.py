def ask_sum_from_one():
  number = ask_user_for_number()
  sum_total = 0
  for i in range(1, int(number)+1):
      sum_total += i
  return sum_total


def sum_from_one(number):
    sum_total = 0
    for i in range(1, int(number)+1):
        sum_total += i
    return sum_total


def product(number):
    prod_total = 1
    for i in range(1, int(number)+1):
        prod_total *= i
    return prod_total


def sum_mult_three_or_five(number):
    new_sum = []
    for i in range(0, int(number)+1):
        if i % 3 == 0 or i % 5 == 0:
            new_sum.append(i)
    return sum(new_sum)


def sum_or_product():
    number = ask_user_for_number()
    choice = input("Would you like to compute the product or sum? \nPlease enter a 1 for the product or 2 for the sum: ")
    if choice == "1":
        return product(number)
    elif choice == "2":
        return sum_from_one(number)
    else:
        return "Invalid choice"


def ask_user_for_number():
  number = int(input("Please enter a number: "))
  if isinstance(number, int):
      return number
  else:
      return "TypeError: Value is not an integer"


print(sum_or_product())
