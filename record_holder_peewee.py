from peewee import *

# Create variable for database
db = SqliteDatabase('chainsaw_juggling_db.sqlite')

# Create a model class
class Records(Model):

    # Class objects
    name = CharField()
    country = CharField()
    number_catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} is from {self.country} with {self.number_catches} performed catches'

# Connect to database
db.connect()

# Create table from the model
db.create_tables([Records])

# Adding record to the database
def add_record_holder():

    # Get the user input about the record holder info
    name = input('Enter the record holder name: ')
    country = input('Enter the country where the record holder from: ')
    number_catches = int(input('Enter the number of catches: '))

    add_record_info = Records(name= name, country= country, number_catches= number_catches)
    
    # Save to update the database
    add_record_info.save() 

# Search record holder by their name from database
def search_record_holder():

    # Get the user input of the name that they would like to find
    search_name = input('Enter the name that you would like to find: ')

    # Get the record if the name is exists in the database
    for record in Records.select().where(Records.name == search_name):
        print(record)

# Update the number of catches by their name in database
def update_record_holder():
    
    # Get the user input about the name that need to be update and the new updated number of catches
    update_name = input('Enter the name of the record holder that need to be updated: ')
    new_number_catches = int(input('Enter the new number of catches: '))

    # Update the number of catches
    update_number_catches = Records.update(number_catches= new_number_catches).where(Records.name == update_name)

    update_number_catches.execute()

# Delete record in database by record holder's name
def delete_record_holder():

    # Get the user input of the name that need to be deleted
    delete_name = input("Enter the name of the person in the record that you want to delete: ")

    # Delete the record by their name
    delete_record = Records.delete().where(Records.name == delete_name)

    delete_record.execute()

# Display of the menu options for the user
def menu_options():
    print('-Chainsaw Juggling Record Holders July 2018- \n')
    print('1. Add Record Holder')
    print('2. Search record holder name')
    print('3. Update the number of catches')
    print('4. Delete record by name')
    print('5. Quit')
    user_input = int(input('Enter choice: '))

    # if the user enter number outside 1-6 print error message
    if not 1 <= user_input < 6:
        print('Error: please enter a number between 1-5.')
    else:
        return user_input    

# Main method
def main():

    running = True
    while running:
        # Display the menu
        user_choices = menu_options()

        # Call the appropriate method depend on the number option the user choose
        if user_choices == 1:
            add_record_holder()
        elif user_choices == 2:
            search_record_holder()
        elif user_choices == 3:
            update_record_holder()
        elif user_choices == 4:
            delete_record_holder()
        elif user_choices == 5:
            running = False
            print('Thank you and goodbye!')

    return user_choices

# Record Errors
class RecordError(Exception):
    pass

if __name__ == '__main__':
    main()
    