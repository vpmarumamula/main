print('from anaconda')
harish = {}
harish['name'] = 'Harish'
harish['roll'] = 56
harish['age'] = 23
vara = {}
vara['name'] = 'Prasad'
vara['roll'] = 78
vara['age'] = 21
stud = [harish, vara]
print(harish)
# for var, val in harish.items():
#   print('var = {}, val = {}'.format(var, val))
for student in stud:
    for var, val in student.items():
        print('var = {}, val = {}'.format(var, val))
