from datetime import datetime, timedelta


def get_birthdays_per_week(users: list):
    birthday_list = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
        'Next Monday': ''
        }

    start = datetime.now().date()
    end = start + timedelta(days=7)
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%d %B %Y")
        date_b = datetime(start.year, birthday.month, birthday.day)
        if start <= date_b.date() <= end:
            day = date_b.weekday()
            if day == 0:
                birthday_list['Monday'] += user['name']
                birthday_list['Monday'] += ', '
            if day == 1:
                birthday_list['Tuesday'] += user['name']
                birthday_list['Tuesday'] += ', '
            if day == 2:
                birthday_list['Wednesday'] += user['name']
                birthday_list['Wednesday'] += ', '
            if day == 3:
                birthday_list['Thursday'] += user['name']
                birthday_list['Thursday'] += ', '
            if day == 4:
                birthday_list['Friday'] += user['name']
                birthday_list['Friday'] += ', '
            if day in (5, 6):
                birthday_list['Next Monday'] += user['name']
                birthday_list['Next Monday'] += ', '

        else:
            print("No birthday in this week")
    return birthday_list
