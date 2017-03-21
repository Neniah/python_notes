
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Sep', 'Oct', 'Nov', 'Dec'];

endings = ['st', 'nd','rd'] + 17*['th'] + ['st' , 'nd', 'rd'] + 7*['th'] + ['st']

year = input('Enter current year: ')
month = input('Enter current month: ')
day = input('Enter current day: ')

month_number = int(month)
day_number = int(day)

month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print(month_name + ', ' + ordinal + ', ' + year)
