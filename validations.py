
days_30 = ["April", "June", "September", "November"]
days_31 = ["January", "March", "May", "July", "August", "October", "December"]

def leap_year(year):
    diff = year - 1960
    return (diff % 4) == 0

def days_of_month(year, month):
    if leap_year(int(year)) and (month == "February"): days = 29
    elif (month == "February"): days = 28
    elif (month in days_30): days =30
    else: days = 31
    
    return list(range(1, days+1))

def no_name(year, month, current_day):
    year = int(year)
    current_day = int(current_day)
    
    if month == "February":
        if leap_year(year) and (current_day > 29):
            return 1
        elif (current_day > 28):
            return 1
    
    elif (month in days_30) and current_day > 30:
        return 1
    
    return current_day