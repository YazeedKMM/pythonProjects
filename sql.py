import random

namesb = []
namesb_file = open('namesb.txt', 'r')
nameb_lines = namesb_file.readlines()

for lineb in nameb_lines:
    namesb.append(lineb.strip("\n"))

namesg = []
namesg_file = open('namesg.txt', 'r')
nameg_lines = namesg_file.readlines()

for lineg in nameg_lines:
    namesg.append(lineg.strip("\n"))

birth_dates = []
br_file = open('birth_dates.txt', 'r')
br_lines = br_file.readlines()

for br in br_lines:
    birth_dates.append(br.strip("\n"))

reg_dates = []
reg_file = open('reg_dates.txt', 'r')
reg_lines = reg_file.readlines()

for reg in reg_lines:
    reg_dates.append(reg.strip("\n"))

names = namesb + namesg

gender = None

# n = 7
# e = 8

# print('stu' + str(e) + '@stu.com')
# stu_id = n + 100
# n += 1
# print('(' + str(stu_id)
#       + ',\'' + nameb + '\',\''
#       + teach_birth + '\',\'M\','
#       + '\'' + stu_reg_date + '\',\''
#       + stu_email + '\','
#       + str(random.randint(1, 6)) + ',\''
#       + stu_track + '\','
#       + str(random.randint(30, 100)) + ')' + ',')
# print('stu' + str(e) + '@stu.com')

for n in range(1, 31):
    e = n
    stu_id = n + 99
    stu_email = 'stu' + str(e) + '@stu.com'
    stu_birth = random.choice(birth_dates)
    stu_reg_date = random.choice(reg_dates)
    name = random.choice(names)
    if name in namesb:
        gender = 'M'
    else:
        gender = 'F'
    track = ['Scientific', 'Humanistic']
    stu_track = random.choice(track)
    print('(' + str(stu_id)
          + ',\'' + name + '\',\''
          + stu_birth + '\',\''
          + gender + '\','
          + '\'' + stu_reg_date + '\',\''
          + stu_email + '\','
          + str(random.randint(1, 6)) + ',\''
          + stu_track + '\','
          + str(random.randint(30, 100)) + ')' + ',')

# teach_dates = []
# teach_file = open('teach_birth_dates.txt', 'r')
# teach_lines = teach_file.readlines()
#
# for teach in teach_lines:
#     teach_dates.append(teach.strip("\n"))
#

# for n in range(2, 11):
#     teach_id = n
#     teach_office = n + 109
#     teach_email = 'teach' + str(n) + '@teacher.com'
#     teach_birth = random.choice(birth_dates)
#     name = random.choice(names)
#     if name in namesb:
#         gender = 'M'
#     else:
#         gender = 'F'
#     print('(' + str(teach_id)
#           + ',\'' + name + '\',\''
#           + teach_birth + '\','
#           + '\'' + gender + '\',\''
#           + teach_email + '\','
#           + str(teach_office) + ')' + ',')
