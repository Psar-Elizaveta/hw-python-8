from datetime import date, datetime


WEEKDAYS = {
    '1':'Monday',
    '2':'Tuesday',
    '3':'Wednesday',
    '4':'Thuesday',
    '5':'Friday',
    '6':'Sunday',
    '7':'Saturday'
}

def get_birthdays_per_week(users):
    birthdays_per_week = {}
    today = date.today()
    for user in users:
        birthdate = user.get('birthday')
        if today.month == 12 and birthdate.month == 1 and birthdate.day < 7:
            current_birthday = birthdate.replace(year=today.year+1)
        else:
            current_birthday = birthdate.replace(year=today.year) 
        
        delta_days = (current_birthday - today).days
        if not (delta_days < 7 and delta_days >= 0):
            continue


        isoweekday = datetime.isoweekday(current_birthday)
        if isoweekday == 6 or isoweekday == 7:
            isoweekday = 1

        try:
            check_day = birthdays_per_week[WEEKDAYS[str(isoweekday)]]
        except KeyError:
            birthdays_per_week.update({WEEKDAYS[str(isoweekday)]:[]})
            check_day = birthdays_per_week[WEEKDAYS[str(isoweekday)]]
        check_day.append(user['name'])    

    return birthdays_per_week


if __name__ == "__main__":
    users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 1, 1).date()},
    {"name": "Kim Kardas", "birthday": datetime(1979, 11, 8).date()},
    {"name": "Kris Minor", "birthday": datetime(2018, 11, 7).date()},
    {"name": "Maria", "birthday": datetime(2004, 11, 9).date()},
    {"name": "Kiril", "birthday": datetime(2002, 11, 10).date()},
]

    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")