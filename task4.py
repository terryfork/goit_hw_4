from datetime import date, datetime, timedelta

def get_upcoming_birthdays(users):
    DAYS_TO_CONGRAT = 7

    upcom_bds = []
    today = date.today()

    def get_greet_date(year, birthday):
        leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0) # Gregorian calendar leap year
        if (birthday.month == 2 and birthday.day == 29 and not leap_year):
            bd = date(year=year, month=2, day=28)
        else:
            bd = date(year=year, month=birthday.month, day=birthday.day)
        bd_weekday = bd.weekday()
        if bd_weekday > 4:
            bd = bd + timedelta(days=7-bd_weekday)
        return bd


    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], "%Y.%m.%d")
        except ValueError:
            print(f"{user.name} has invalid birthday format")
        else:
            next_bd = get_greet_date(today.year, birthday)
            if next_bd < today:
                next_bd = get_greet_date(today.year+1, birthday)

            delta = next_bd - today

            if delta.days <= DAYS_TO_CONGRAT:
#                print(f"{user['name']}	{user['birthday']}	{next_bd}	in {delta.days} days")
                upcom_bds.append({"name": user["name"], "congratulation_date": next_bd.strftime("%Y.%m.%d")})
    return upcom_bds



users = [
    {"name": "John Doe", "birthday": "1985.10.23"},
    {"name": "Jane Smith", "birthday": "1990.10.27"},
    {"name": "Joe Black", "birthday": "1990.11.23"},
    {"name": "Jake Brown", "birthday": "1980.02.29"},
]

print(get_upcoming_birthdays(users))
