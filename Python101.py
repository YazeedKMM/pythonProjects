phoneDict = {1111111111: 'Amal', 2222222222: 'Mohammed', 3333333333: 'Khadijah', 4444444444: 'Abdullah',
             5555555555: 'Rawan', 6666666666: 'Faisal', 7777777777: 'Layla'}


def check_numbers(phone):
    count = 0
    if phone.isdigit():
        for n in phone:
            if isinstance(int(n), int):
                count += 1
            else:
                continue

    if count != 10:
        return False
    else:
        return True


def check_names(name):
    for key, value in phoneDict.items():
        if value == name:
            return "The number of " + str(value) + " is " + str(key)

    return "Sorry, the name is not found"


def search_by_number():
    number = input("\nEnter a number consist of 10 integer: ")
    k = 0

    if check_numbers(number):
        for i in phoneDict.keys():
            if i == int(number):
                k = i
    else:
        print("This is invalid number")

    if k != 0:
        print("The Phone Number " + str(k) + " belongs to " + phoneDict[k])
    else:
        print("Sorry, the number is not found")


def search_by_name():
    name = input("\nEnter a name: ")
    print(check_names(name))


def add_to_phonebook():
    user_name, user_pnumber = input("\nEnter user name: "), int(input("\nEnter user phone number: "))
    phoneDict[user_pnumber] = user_name
    print("\nPhonebook has been updated successfully!!"
          "\n\n\tPHONEBOOK:")
    i = 1
    for k in phoneDict.keys():
        print("\n\t\t" + str(i) + ". " + phoneDict[k] + " | " + str(k))
        i += 1


print("\nChoose one of the option to search in Phonebook:"
      "\n\t1) Search by name"
      "\n\t2) Search by number"
      "\n\t3) Add a user to Phonebook")

option = int(input("\nYour option: "))

if option == 1:
    search_by_name()
elif option == 2:
    search_by_number()
elif option == 3:
    add_to_phonebook()
else:
    print("\n\tinvalid option, Try again!")
