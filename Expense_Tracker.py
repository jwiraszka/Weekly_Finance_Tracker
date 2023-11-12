# this program gathers daily input of expenses, categorizes them, records them in a file and visualised weekly spending habits
import io

from matplotlib import pyplot as plt

# read in weekly_expenses.txt file if there is data in the file
expense_list = []


def read_data():
    data = open('weekly_expenses.txt', 'r')
    try:
        for each_line in data:
            # check if the file is empty,if not append existing data to the list
            if each_line[0] != '\n':
                expense_list.append(each_line.strip().split(','))

    except io.UnsupportedOperation:
        print()

    data.close()


def menu():
    correct = False

    # display header
    print('-' * 30 + 'WEEKLY EXPENSE TRACKER', '-' * 30 + '\n')

    # display menu options
    print('MAIN MENU:')
    print('1. Get general expense report for the week.')
    print('2. Get expense report for the week organised by day.')
    print('3. Get detailed expense report for the week including full expense descriptions.')
    print('4. Get expense report for the week listed by category.')
    print('5. Add an entry for the week.')
    print('6. Delete all entries for this week.')
    print('7. Exit')

    while correct == False:
        option = input('Enter your option: ')
        print('\n')
        if option == '1':
            correct = True
            weekly_report()
        elif option == '2':
            correct = True
            daily_report()
        elif option == '3':
            correct = True
            detailed_report()
        elif option == '4':
            category_report()
        elif option == '5':
            correct = True
            add_entry()
        elif option == '6':
            correct = True
            delete_entries()
        elif option == '7':
            correct = True
            print('Goodbye.')
            print('Program has been terminated.')
        else:
            print('ERROR: Invalid option. Please enter a number.')


def weekly_report():
    # display a weekly expense report to the user
    print('-' * 14, 'WEEKLY EXPENSE REPORT ', '-' * 14)
    print('{:20}{:20}{:20}'.format(' DATE', ' CATEGORY', ' AMOUNT(£)'))
    try:
        if len(expense_list) <= 0:
            print('{:20}{:20}{:20}'.format(' -', ' -', ' -'))
            print('\nThere has been no data recorded for this week.')
        else:
            for each_line in expense_list:
                print('{:20}{:20}{:20}'.format(each_line[2], each_line[1], each_line[3]))

            total_expenses()

    except IndexError:
        print()

    # allow user to return to main menu
    return_to_menu()


def daily_report():
    # display a weekly expense report to the user organised by day of the week
    organised = []
    print('-' * 14, 'WEEKLY EXPENSE REPORT', '-' * 14)
    print('{:20}{:20}{:20}'.format(' DATE', ' CATEGORY', ' AMOUNT(£)'))

    try:
        if len(expense_list) <= 0:
            print('{:20}{:20}{:20}'.format(' -', ' -', ' -'))
            print('\nThere has been no data recorded for this week.')
        else:
            for each_line in expense_list:
                if 'Monday' in each_line[2]:
                    print('{:20}{:20}{:20}'.format(each_line[2], each_line[1], each_line[3]))

            for each_line in expense_list:
                if 'Tuesday' in each_line[2]:
                    print('{:20}{:20}{:20}'.format(each_line[2], each_line[1], each_line[3]))

            for each_line in expense_list:
                if 'Wednesday' in each_line[2]:
                    print('{:20}{:20}{:20}'.format(each_line[2], each_line[1], each_line[3]))

            for each_line in expense_list:
                if 'Thursday' in each_line[2]:
                    print('{:20}{:20}{:20}'.format(each_line[2], each_line[1], each_line[3]))

            for each_line in expense_list:
                if 'Friday' in each_line[2]:
                    print('{:20}{:20}{:20}'.format(each_line[2], each_line[1], each_line[3]))

            for each_line in expense_list:
                if 'Saturday' in each_line[2]:
                    print('{:20}{:20}{:20}'.format(each_line[2], each_line[1], each_line[3]))

            for each_line in expense_list:
                if 'Sunday' in each_line[2]:
                    print('{:20}{:20}{:20}'.format(each_line[2], each_line[1], each_line[3]))

            total_expenses()

    except IndexError:
        print()

    # allow user to return to main menu
    return_to_menu()


def detailed_report():
    # display a weekly expense report to the user including the description
    print('-' * 30, 'WEEKLY EXPENSE REPORT', '-' * 30)
    print('{:20}{:20}{:20}{:50}'.format(' DATE', ' CATEGORY', ' AMOUNT(£)', 'DESCRIPTION'))
    try:
        if len(expense_list) <= 0:
            print('{:20}{:20}{:20}{:50}}'.format(' -', ' -', ' -', ' -'))
            print('\nThere has been no data recorded for this week.')
        else:
            for each_line in expense_list:
                print('{:20}{:20}{:20}{:50}'.format(each_line[2], each_line[1], each_line[3], each_line[0]))

            total_expenses()

    except IndexError:
        print()

    # allow user to return to main menu
    return_to_menu()


def category_report():
    personal_total = 0
    recreational_total = 0
    food_total = 0
    transport_total = 0
    household_total = 0
    mortgage_total = 0
    healthcare_total = 0
    other_total = 0

    # display a weekly expense report to the user categories by category
    print('-' * 10, 'WEEKLY EXPENSE REPORT', '-' * 10)
    print('{:23}{:20}'.format('CATEGORY', 'TOTAL AMOUNT(£)'))

    if len(expense_list) <= 0:
        print('{:23}{:<20}'.format(' -', ' -'))
        print('\nThere has been no data recorded for this week.')
    else:
        for each_line in expense_list:
            if 'Personal Care' in each_line[1]:
                personal_total = personal_total + float(each_line[3])
            elif 'Recreational/Leisure' in each_line[1]:
                recreational_total = recreational_total + float(each_line[3])
            elif 'Food' in each_line[1]:
                food_total = food_total + float(each_line[3])
            elif 'Transport' in each_line[1]:
                transport_total = transport_total + float(each_line[3])
            elif 'Household Goods' in each_line[1]:
                household_total = household_total + float(each_line[3])
            elif 'Mortgage/Rent' in each_line[1]:
                mortgage_total = mortgage_total + float(each_line[3])
            elif 'Healthcare' in each_line[1]:
                healthcare_total = healthcare_total + float(each_line[3])
            else:
                other_total = other_total + float(each_line[3])

        # print all categories and totals
        print('{:23}{:<20}'.format('Personal Care', personal_total))
        print('{:23}{:<20}'.format('Recreational/Leisure', recreational_total))
        print('{:23}{:<20}'.format('Food', food_total))
        print('{:23}{:<20}'.format('Transport', transport_total))
        print('{:23}{:<20}'.format('Household Goods', household_total))
        print('{:23}{:<20}'.format('Mortgage/Rent', mortgage_total))
        print('{:23}{:<20}'.format('Healthcare', healthcare_total))
        print('{:23}{:<20}'.format('Other', other_total))

    # bar chart data
    category_amount = [personal_total, recreational_total, food_total, transport_total,
                     household_total, mortgage_total, healthcare_total, other_total]
    category_list = ['Personal Care', 'Leisure', 'Food', 'Transport',
                     'Household', 'Rent', 'Healthcare', 'Other']

    # plot bar chart
    plt.bar(category_list, category_amount, 0.5,
            color=('royalblue', 'orchid', 'c', 'y', 'olivedrab', 'goldenrod', 'mediumslateblue', 'brown'))
    plt.title("Weekly Spending's Per Category")
    plt.ylabel('Amount spent')
    plt.show()

    # allow user to return to main menu
    return_to_menu()


def total_expenses():
    total = 0

    # add up the total amount for all expenses for the week
    for each_line in expense_list:
        total = total + float(each_line[3])
    print('\nTotal expense for the week: £', total)


def add_entry():
    file = open('weekly_expenses.txt', 'a')
    expense_entry = []
    another = True

    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    correct_category = False
    correct_day = False

    # prompt user for input
    print('WEEKLY EXPENSES')
    while another == True:
        # prompt user for description
        description = input('Description of purchase: ')

        # allow user to add the expense to a category
        print('\nCategories include:')
        print('1. Personal Care (clothing, cosmetics)')
        print('2. Recreational/Leisure')
        print('3. Food')
        print('4. Transport')
        print('5. Household Goods')
        print('6. Mortgage/Rent')
        print('7. Healthcare')
        print('8. Other')
        while correct_category == False:
            option = input('Option (number): ')
            if option == '1':
                category = 'Personal Care'
                correct_category = True
            elif option == '2':
                category = 'Recreational/Leisure'
                correct_category = True
            elif option == '3':
                category = 'Food'
                correct_category = True
            elif option == '4':
                category = 'Transport'
                correct_category = True
            elif option == '5':
                category = 'Household Goods'
                correct_category = True
            elif option == '6':
                category = 'Mortgage/Rent'
                correct_category = True
            elif option == '7':
                category = 'Healthcare'
                correct_category = True
            elif option == '7':
                category = 'Other'
                correct_category = True
            else:
                print('ERROR: Incorrect category input. Please enter a number listed.')
                correct_category = False

        # day of the week
        while correct_day == False:
            day = input('\nDay: ')
            if day.lower() in week_days:
                correct_day = True
            else:
                print('ERROR: Invalid day has been entered. please re-enter the date.')

        # prompt user for amount
        expense = input('\nAmount: £')

        # append all data to the expense_list
        expense_entry.append(description.capitalize())
        expense_entry.append(category)
        expense_entry.append(day.capitalize())
        expense_entry.append(expense)

        # add entry to expense_list
        expense_list.append(expense_entry)

        # add entry to file, remove brackets and quotes
        file.write(str(expense_entry).strip().strip('[' + ']').replace("'", '') + '\n')

        # ask if the user would like to add another entry
        another_expense = input('Would you like to enter another entry? (y/n)')

        if another_expense == 'y' or another_expense == 'Y':
            another = True
            # restart correctors and clear expense_entry for the next entry
            expense_entry.clear()
            correct_category = False
            correct_day = False
        else:
            another = False

    # close file after use
    file.close()
    # allow user to return to main menu
    return_to_menu()


def delete_entries():
    if len(expense_list) <= 0:
        print('\nThe file is already empty.')
    else:
        # remove all contents in file
        open('weekly_expenses.txt', 'w').close()
        # remove all contents in expense_list
        expense_list.clear()

        print('All entries have been successfully deleted.')

    # allow user to return to main menu
    return_to_menu()


def return_to_menu():
    to_menu = input('Would you like to return to the main menu? (y/n) ')
    if to_menu.lower() == 'y':
        print('\n')
        menu()
    else:
        print('Goodbye.')
        print('Program has been terminated.')


# call functions to read data and initialise the menu
read_data()
menu()
