import datetime
from dateutil.relativedelta import relativedelta

# this get_past_date function is to convert # #
# today, yesterday,days, years, mon  to # # s = '2017-08-16'
# https://docs.python.org/3/library/datetime.html visit this for details on abbrv

def get_past_date(str_days_ago):
    TODAY = datetime.date.today()
    splitted = str_days_ago.split()
    if len(splitted) == 1 and splitted[0].lower() == 'today':
        return str(TODAY.isoformat())
    elif len(splitted) == 1 and splitted[0].lower() == 'yesterday':
        date = TODAY - relativedelta(days=1)
        return str(date.isoformat())
    elif splitted[1].lower() in ['hour', 'hours', 'hr', 'hrs', 'h']:
        date = datetime.datetime.now() - relativedelta(hours=int(splitted[0]))
        return str(date.date().isoformat())
    elif splitted[1].lower() in ['day', 'days', 'd']:
        date = TODAY - relativedelta(days=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['wk', 'wks', 'week', 'weeks', 'w']:
        date = TODAY - relativedelta(weeks=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['mon', 'mons', 'month', 'months', 'm']:
        date = TODAY - relativedelta(months=int(splitted[0]))
        return str(date.isoformat())
    elif splitted[1].lower() in ['yrs', 'yr', 'years', 'year', 'y']:
        date = TODAY - relativedelta(years=int(splitted[0]))
        return str(date.isoformat())
    else:
        return "Wrong Argument format"

last_seen = 'yesterday'

y = get_past_date(last_seen)
print(y)
# # print(get_past_date('yesterday'))
# #
# # s = '2017-08-16'
# now convert '2017-08-16' to epoch
epoch = datetime.datetime.strptime(y, "%Y-%m-%d").timestamp()
print(epoch)
# # epoch = datetime.datetime.strptime(get_past_date('yesterday'), "%Y-%m-%d").timestamp()
# # print(epoch)

# to convert 07.10.2020 10:24 AM to epoch
dt = datetime.datetime.strptime('07.10.2020 10:24 AM', '%m.%d.%Y %I:%M %p').timestamp()
print(dt)

#to convert 'Dec/10/2020 10:32AM', to epoch
dates='Dec/10/2020 10:32AM'
epoch1 = datetime.datetime.strptime(dates, '%b/%d/%Y %H:%M%p').timestamp()
print("Dec/10/2020 10:32AM",epoch1,"epoch")
