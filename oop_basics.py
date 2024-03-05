'''
import random

class xyz:
    float_number=1.0

    def random_function():
        return random.randrange(1,100)

xyz1=xyz
print(xyz1.float_number)
print(xyz1.random_function())

'''

'''
class calculator:
    def addition(a,b):
        return a+b
    def subtraction(a,b):
        return a-b
    def multiplication(a,b):
        return a*b 
    def division(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("zero division error")


calc=calculator
print('enter two number⬇️') 
print('_'*30)
first=int(input('enter first number: '))
second=int(input('enter second number: '))
print('_'*30)

while True:
    choice=input('enter your choice:\n1.[+]\n2.[-]\n3.[*]\n4.[/]\n')
    print('_'*30)
    match choice:
        case '+':
            print(calc.addition(first,second))
        case '-':
            print(calc.subtraction(first,second))
        case '*':
            print(calc.multiplication(first,second))
        case '/':
            print(calc.division(first,second))
        case _:
            print('HEY, choose valid choice:')

    ch=input('do you want to continue? [y/n]: ')
    if ch.lower()=='n':
        break
'''
'''

import datetime

class remind_me:
    def __init__(self):
        self.rem = {}

    def store(self):
        print('Enter the date you want to save, yy/mm/dd:')
        year = int(input('Enter year: '))
        month = int(input('Enter month: '))
        day = int(input('Enter day: '))
        event = input('Enter the event: ')
        self.rem[year, month, day] = event

    def check(self):
        sp = []
        now = datetime.datetime.now()
        sp.append(now.year)
        sp.append(now.month)
        sp.append(now.day)
        return tuple(sp)

# Create an instance of the remind_me class
reminder = remind_me()

while True:
    reminder.store()
    choice = input("Press 'n' to terminate program or any other key to add more events: ")
    if choice.lower() == 'n':
        break

# Check for events on the current date
current_date = reminder.check()
for key, value in reminder.rem.items():
    if key == current_date:
        print(f'Event on {current_date}: {value}')
'''


import datetime

class RemindMe:
    def __init__(self):
        self.rem = {}

    def store(self):
        try:
            print('\n===== Add Event =====')
            year = int(input('Enter year (e.g., 2024): '))
            month = int(input('Enter month (1-12): '))
            day = int(input('Enter day (1-31): '))
            event = input('Enter the event: ')
            
            # Validate the date
            datetime.datetime(year, month, day)
            
            self.rem[year, month, day] = event
            print('Event added successfully!')
        except ValueError:
            print('Invalid input. Please enter valid integers for year, month, and day.')

    def delete_event(self):
        print('\n===== Delete Event =====')
        if not self.rem:
            print('No events to delete.')
            return

        print('Select event to delete:')
        for i, (key, value) in enumerate(self.rem.items(), 1):
            print(f'{i}. {value} on {key}')

        try:
            choice = int(input('Enter the number corresponding to the event you want to delete: '))
            if 1 <= choice <= len(self.rem):
                event_to_delete = list(self.rem.keys())[choice - 1]
                del self.rem[event_to_delete]
                print('Event deleted successfully!')
            else:
                print('Invalid choice.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    def view_events(self):
        print('\n===== View Events =====')
        if not self.rem:
            print('No events available.')
            return

        print('Select an option:')
        print('1. View events for today')
        print('2. View events for a specific date')
        print('3. View all events')

        choice = input('Enter your choice (1, 2, or 3): ')

        if choice == '1':
            self.view_events_for_date(datetime.datetime.now())
        elif choice == '2':
            try:
                year = int(input('Enter the year: '))
                month = int(input('Enter the month: '))
                day = int(input('Enter the day: '))
                selected_date = datetime.datetime(year, month, day)
                self.view_events_for_date(selected_date)
            except ValueError:
                print('Invalid input. Please enter valid integers for year, month, and day.')
        elif choice == '3':
            self.view_all_events()
        else:
            print('Invalid choice. Please enter 1, 2, or 3.')

    def view_events_for_date(self, selected_date):
        found_events = [value for key, value in self.rem.items() if key == (selected_date.year, selected_date.month, selected_date.day)]

        if found_events:
            print(f'\nEvents for {selected_date.date()}:')
            for event in found_events:
                print(f'- {event}')
        else:
            print(f'\nNo events for {selected_date.date()}.')

    def view_all_events(self):
        print('\nAll Events:')
        for key, value in self.rem.items():
            print(f'{value} on {key}')

    def check(self):
        sp = []
        now = datetime.datetime.now()
        sp.extend([now.year, now.month, now.day])
        return tuple(sp)

# Create an instance of the RemindMe class
reminder = RemindMe()

while True:
    print('\n===== Menu =====')
    print('1. Add Event')
    print('2. Delete Event')
    print('3. View Events')
    print('4. Exit')
    
    choice = input('Enter your choice (1, 2, 3, or 4): ')

    if choice == '1':
        reminder.store()
    elif choice == '2':
        reminder.delete_event()
    elif choice == '3':
        reminder.view_events()
    elif choice == '4':
        print('Exiting the program. Goodbye!')
        break
    else:
        print('Invalid choice. Please enter 1, 2, 3, or 4.')
