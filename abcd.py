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

    def delete(self):
        print('\n===== Delete Event =====')
        year = int(input('Enter year of the event to delete: '))
        month = int(input('Enter month of the event to delete: '))
        day = int(input('Enter day of the event to delete: '))
        
        if (year, month, day) in self.rem:
            del self.rem[year, month, day]
            print('Event deleted successfully!')
        else:
            print('No event found for the specified date.')

    def view_for_date(self):
        print('\n===== View Events for a Date =====')
        year = int(input('Enter year: '))
        month = int(input('Enter month: '))
        day = int(input('Enter day: '))
        
        target_date = (year, month, day)
        events_for_date = [value for key, value in self.rem.items() if key == target_date]
        
        if events_for_date:
            print(f'\nEvents for {target_date}:')
            for event in events_for_date:
                print(f'- {event}')
        else:
            print(f'\nNo events found for {target_date}.')

    def view_all(self):
        print('\n===== View All Events =====')
        if not self.rem:
            print('No events found.')
            return

        # Sort events by date
        sorted_events = sorted(self.rem.items())

        for key, value in sorted_events:
            print(f'{key}: {value}')

    def search(self):
        print('\n===== Search for Events =====')
        keyword = input('Enter a keyword to search for: ')
        
        matching_events = [value for value in self.rem.values() if keyword.lower() in value.lower()]
        
        if matching_events:
            print(f'\nMatching events:')
            for event in matching_events:
                print(f'- {event}')
        else:
            print('No matching events found.')

if __name__ == "__main__":
    reminder = RemindMe()

    while True:
        print('\n===== Menu =====')
        print('1. Add Event')
        print('2. Delete Event')
        print('3. View Events for a Date')
        print('4. View All Events')
        print('5. Search for Events')
        print('6. Exit')
        
        choice = input('Enter your choice (1-6): ')

        if choice == '1':
            reminder.store()
        elif choice == '2':
            reminder.delete()
        elif choice == '3':
            reminder.view_for_date()
        elif choice == '4':
            reminder.view_all()
        elif choice == '5':
            reminder.search()
        elif choice == '6':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 6.')
