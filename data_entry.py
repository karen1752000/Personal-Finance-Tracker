from datetime import datetime

#prompt is what the app is going to ask the user to input before the user gives the app the date
#allow default will tell the app if we should have a default value of today's date. so the user could just hit enter and 
#by default it will just select the current date

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if  allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        vaild_date = datetime.strptime(date_str, date_format)
        return vaild_date.strftime(date_format)
    except ValueError:
        print("Invalid date frmat. Please enter the in dd-mm-yyyy format")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES: 
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category


def get_description():
   return input("Enter a description (optional): ")



























#data_entry file is a place where I can write all of the functions related to getting informantion from the user
