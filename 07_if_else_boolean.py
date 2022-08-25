# what if user enter -10
# conditionals a == b, a != b, a < b, a <= b, a > b, a >= b


calculate_to_units = 4
name_of_unit = "seconds"
num_of_days = 2


def days_to_units(num_of_days):
    if num_of_days > 0:
        return print(f"converted value {num_of_days} is  {num_of_days * calculate_to_units}")
    elif num_of_days == 0:
        print(f"Hello in elif")
        return print(f"value zero no conversion")
    elif num_of_days < 0:
        print(f"in 2nd elif")
        return
    else:
        return print(f"you entered negative value")


days_to_units(1)
my_var = days_to_units(5)
print(f"{my_var}")
user_input = input("enter number of days it will be converted to seconds \n")
user_input_variable = int(user_input)

my_var = days_to_units(int(user_input))
