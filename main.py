import numpy as np
import datetime
import re

class ManagerDates:
    def date_is_valid(self, date):
        try:
            datetime.datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            return False
        else:
            return True

    def date_weekday(self, date):
        day_name = date.strftime('%A')
        return day_name

    def convert_string_to_date(self, date_str):
        patterns = ['%d-%m-%Y', '%d/%m/%Y', '%d%m%Y']
        for fmt in patterns:
            try:
                date_str = datetime.datetime.strptime(date_str, fmt)
            except:
                continue
            else:
                return date_str                
        return False

    def get_all_dates(self, month, year):
        next_month = f'0{int(month)+1}'
        days = np.arange(f'{year}-{month}', f'{year}-{next_month}',
                         dtype='datetime64[D]')
        return days 

    def count_days_mounth(self, month, year):
        next_month = f'0{int(month)+1}'
        n_days = np.busday_count(f'{year}-{month}', f'{year}-{next_month}')
        return n_days

    def get_first_monday(self, year):
        first_mon = np.busday_offset(f'{year}-05', 0, roll='forward',
                                     weekmask='Mon')
        to_date = first_mon.astype('datetime64[D]').item()
        date_to_format = to_date.strftime('%d/%m/%Y')
        return date_to_format
