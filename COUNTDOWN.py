from datetime import datetime, date

def calculate_birthday_countdown(birthdate):
    today = date.today()
    next_birthday = birthdate.replace(year=today.year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    days_left = (next_birthday - today).days

    return next_birthday, days_left

def main():
    birthdate = datetime.strptime('12-05-1999', '%d-%m-%Y').date()
    next_birthday, days_left = calculate_birthday_countdown(birthdate)

    print("Your birth date:", birthdate.strftime('%d %B %Y'))
    print("Days left until your next birthday:", days_left,"days")

if __name__ == "__main__":
    main()
