from datetime import datetime, timedelta


def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format")
        return None
    now = datetime.now()
    delta = now - date_obj
    return delta.days


print(get_days_from_today("2025-10-10"))
print(get_days_from_today("2025-10-30"))
print(get_days_from_today("incorrect date"))
