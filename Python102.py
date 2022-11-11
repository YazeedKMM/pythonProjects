import datetime


def isvalid(date_str):
    day = date_str.split('-')[0]
    month = date_str.split('-')[1]
    year = date_str.split('-')[2]
    valid_day = day.isdigit() and 0 < int(day) < 32
    valid_month = month.isdigit() and 0 < int(month) < 13
    valid_year = year.isdigit() and 1000 < int(year) < 2023
    if (valid_day and len(day) == 2 or len(day) == 1) \
            and (valid_month and len(month) == 2 or len(month) == 1) \
            and (valid_year and len(year) == 4):
        return True
    else:
        return False


def day_name(date_str):
    return datetime.datetime.strptime(date_str, '%d-%m-%Y').date().strftime('%A')


def get_age(date_str):
    age = 0
    day = date_str.split('-')[0]
    month = date_str.split('-')[1]
    year = date_str.split('-')[2]
    if int(datetime.date.today().month) > int(month):
        age = int(datetime.date.today().year) - int(year)
    elif int(datetime.date.today().month) == int(month):
        if int(datetime.date.today().day) < int(day):
            age = (int(datetime.date.today().year) - 1) - int(year)
    else:
        age = (int(datetime.date.today().year) - 1) - int(year)
    return age


print("\n\t--------------------Welcome to Birth Day Calculator program-----------------\n")
op = input("\n\tDo you want to start the program? (Y/N): ")
br_names = []
ages = {}
while op.casefold() == 'y' or op.casefold() == 'yes':
    name = input("\n\tEnter Your Name: ")
    date_string = input("\n\tEnter Your Birthday (dd-mm-yyyy): ")
    if isvalid(date_string):
        br_names.append([name, day_name(date_string), get_age(date_string)])
        ages[name] = get_age(date_string)
    else:
        br_names.append([name, 'Invalid date'])
    op = input("\n\tDo you want to add more users? (Y/N): ")


if len(br_names) >= 1:
    for u in br_names:
        if len(u) > 2:
            print("\n\t{} is {} years old and she/he was born on {}".format(u[0], u[2], u[1]))
        else:
            print("\n\t{} has entered an {} ".format(u[0], u[1]))

# First Additional Question: sort the users from oldest to youngest and print the result
# if len(br_names) >= 1:
#     c = len(br_names)
#     j = len(br_names) - len(ages)
#     for n, a in sorted(ages.items()):
#         for u in br_names:
#             if len(u) > 2:
#                 if n == u[0]:
#                     print("\n\t{} is {} years old and she/he was born on {}".format(u[0], u[2], u[1]))
#                     c -= 1
#             else:
#                 if c == j:
#                     print("\n\t{} has entered an {} ".format(u[0], u[1]))

oldest = None
youngest = None

if len(ages) == 1:
    print("\n\tThere is no oldest or youngest person")
elif len(ages) > 1:
    for k, v in ages.items():
        if v == max(ages.values()):
            oldest = k
        elif v == min(ages.values()):
            youngest = k

print("\n\tThe oldest one is", oldest)
print("\n\tThe youngest one is", youngest)
print("\n\tTotal people:", len(br_names))
print("\n\tThank you for using our program!")
