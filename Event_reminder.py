
'''
#this is simple python oop program which save events on a given date
#if the current date matched with saved date then it will remind today even
import datetime

class remind_me:
    def __init__(self):
        self.rem = {}

    def store(self):
        print('_'*30)
        print('Enter the date you want to save, yy/mm/dd:')
        print('_'*30)
        year = int(input('Enter year: '))
        month = int(input('Enter month: '))
        day = int(input('Enter day: '))
        event = input('Enter the event: ')
        print('_'*30)

        # Check if the date is already in the dictionary
        date_key = (year, month, day)
        if date_key in self.rem:
            # If the date is already present, append the new event to the existing list
            self.rem[date_key].append(event)
        else:
            # If the date is not present, create a new list with the event
            self.rem[date_key] = [event]

    def check(self):
        now = datetime.datetime.now()
        return now.year, now.month, now.day

# Create an instance of the remind_me class
reminder = remind_me()

while True:
    reminder.store()
    choice = input("Press 'n' to terminate program or any other key to add more events: ")
    print('_'*30)
    if choice.lower() == 'n':
        break

# Check for events on the current date
current_date = reminder.check()
if current_date in reminder.rem:
    print(f'\nEvents on {current_date}: {", ".join(reminder.rem[current_date])}')
else:
    print(f'\nNo events on {current_date}')
'''


#this program is little bit more features_full than above programe
import datetime
import os

class RemindMe:
    def __init__(self):
        self.rem = {}

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def store(self):
        self.clear_screen()
        try:
            print('\n===== Add Event =====')
            year = int(input('Enter year (e.g., 2024): '))
            month = int(input('Enter month (1-12): '))
            day = int(input('Enter day (1-31): '))
            event = input('Enter the event: ')
            
            # Validate the date
            datetime.datetime(year, month, day)
            
            date_key = (year, month, day)
            
            if date_key not in self.rem:
                self.rem[date_key] = []

            self.rem[date_key].append(event)
            print('Event added successfully!')
        except ValueError:
            print('Invalid input. Please enter valid integers for year, month, and day.')

    def delete_event(self):
        self.clear_screen()
        print('\n===== Delete Event =====')
        if not self.rem:
            print('No events to delete.')
            return

        print('Select date to delete an event:')
        for i, (key, events) in enumerate(self.rem.items(), 1):
            print(f'{i}. Events on {key}: {", ".join(events)}')

        try:
            choice = int(input('Enter the number corresponding to the date: '))
            if 1 <= choice <= len(self.rem):
                date_to_delete = list(self.rem.keys())[choice - 1]
                self.delete_event_on_date(date_to_delete)
            else:
                print('Invalid choice.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    def delete_event_on_date(self, date_to_delete):
        events_on_date = self.rem.get(date_to_delete, [])

        if not events_on_date:
            print(f'No events found on {date_to_delete}.')
            return

        print(f'Select event to delete on {date_to_delete}:')
        for i, event in enumerate(events_on_date, 1):
            print(f'{i}. {event}')

        try:
            choice = int(input('Enter the number corresponding to the event you want to delete: '))
            if 1 <= choice <= len(events_on_date):
                event_to_delete = events_on_date[choice - 1]
                self.rem[date_to_delete].remove(event_to_delete)
                print('Event deleted successfully!')
                if not self.rem[date_to_delete]:
                    del self.rem[date_to_delete]
            else:
                print('Invalid choice.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    def view_events(self):
        self.clear_screen()
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
        date_key = (selected_date.year, selected_date.month, selected_date.day)
        events = self.rem.get(date_key, [])

        if events:
            print(f'\nEvents for {selected_date.date()}:')
            for event in events:
                print(f'- {event}')
        else:
            print(f'\nNo events for {selected_date.date()}.')

    def view_all_events(self):
        print('\nAll Events:')
        for key, events in self.rem.items():
            print(f'Events on {key}: {", ".join(events)}')

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
