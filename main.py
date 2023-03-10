student_names = ['Chris', 'Tina', 'Jordan', 'Eric', ]
student_hometowns = ['Detroit', 'Chicago', 'Memphis', 'Dallas']
student_favfood = ['Coney', 'Pizza', 'Ribs', 'Steak']

list_num = 1

print("Greeting! Here is our list of students.")
for name in student_names:
    print(f'{list_num} {name}')
    list_num += 1

while True:
    while True:
        student_query = int(input('Which student would you like to inquire about? Enter their number: '))
        query_index = student_query - 1
        if student_query > len(student_names) or student_query < 1:
            print('Incorrect answer, please try again.')
            continue
        else:
            print(f'Student {student_query} is {student_names[query_index]}. What would you like to know?')
            break

    while True:
        category = input('Enter a category: "Hometown" or "Food": ')
        if category.title() != 'Hometown' and category.title() != 'Food':
            print('Invalid Entry, try again')
            continue
        elif category.title() == 'Hometown':
            print(f'{student_names[query_index]} is from {student_hometowns[query_index]}')
            break
        elif category.title() == 'Food':
            print(f"{student_names[query_index]}'s favorite food is {student_favfood[query_index]}")
            break

    re_run = input('Would you like to learn about another student? (Enter "y" or "n") ')
    if re_run.lower() == 'y':
        continue
    elif re_run.lower() == 'n':
        break






