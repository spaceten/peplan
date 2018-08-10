CYELLOW = '\33[93m'
CRED = '\33[91m'
CGREEN = '\33[32m'
CYELLOWBG = '\x1b[6;30;43m'
CREDBG = '\x1b[6;30;41m'
CEND = '\33[0m'
CENDEND = '\x1b[0m'


old_plan_raw = input('\n' + CRED + '>' + CEND + CYELLOW + ' Choose the ' + CEND + CREDBG + 'current plan' + CENDEND + CYELLOW + \' (1,2 or 3) \n  (1)Private, (2)Business, (3)Business Office: ' + CEND)
mailboxes = input('\n' + CRED + '>' + CEND + CYELLOW + ' The ' + CEND + CREDBG + 'total number of mailboxes' + CENDEND + CYELLOW + \' (including the default one): ' + CEND)
b_cycle = input('\n' + CRED + '> ' + CEND + CREDBG + 'Billing cycle' + CENDEND + CYELLOW + ' (1 or 2)\n  (1)One year, (2)Two years or more: ' + CEND)
expiration_date = input('\n' + CRED + '> ' + CEND + CREDBG + 'Expiration date' + CENDEND + CYELLOW + ' mm' + CRED + '/' + CEND + CYELLOW + 'dd' + CRED + '/' + \ CEND + CYELLOW + 'yy (paste from NC Admin): ' + CEND)

import time
from datetime import datetime, timedelta
date_format = "%m/%d/%Y"
expiration_date = datetime.strptime(expiration_date, date_format)
today = datetime.now() - timedelta(days=1)
days_raw = expiration_date - today
days = days_raw.days

private = ''
business = ''
business_office = ''

if old_plan_raw == "1":
        old_plan = private
        new_plan = input('\n' + CRED + '>' + CEND + CYELLOW + ' Choose the ' + CREDBG + 'new plan' + CENDEND + CYELLOW + ' (2 or 3) \n  (2)Business, (3)Business Office: ' + CEND)
        old_mb_price = 2.98
        if b_cycle == "1":
                old_plan_price = 9.88
        else:
                old_plan_price = 8.88

if old_plan_raw == "2":
        old_plan = business
        new_plan = input('\n' + CRED + '>' + CEND + CYELLOW + ' Choose the ' + CREDBG + 'new plan' + CENDEND + CYELLOW + ' (1 or 3) \n  (1)Private, (3)Business Office: ' + CEND)
        old_mb_price = 14.88
        if b_cycle == "1":
                old_plan_price = 28.88
        else:
                old_plan_price = 25.88

if old_plan_raw == "3":
        old_plan = business_office
        new_plan = input('\n' + CRED + '>' + CEND + CYELLOW + ' Choose the ' + CREDBG + 'new plan' + CENDEND + CYELLOW + ' (1 or 2) \n  (1)Private, (2)Business: ' + CEND)
        old_mb_price = 35.88
        if b_cycle == "1":
                old_plan_price = 49.88
        else:
                old_plan_price = 45.88

if new_plan == "1":
        new_mb_price = 2.98
        if b_cycle == "1":
                new_plan_price = 9.88
        else:
                new_plan_price = 8.88
if new_plan == "2":
        new_mb_price = 14.88
        if b_cycle == "1":
                new_plan_price = 28.88
        else:
                new_plan_price = 25.88
if new_plan == "3":
        new_mb_price = 35.88
        if b_cycle == "1":
                new_plan_price = 49.88
        else:
                new_plan_price = 45.88


old_price = old_mb_price * (int(mailboxes) - 1) + old_plan_price
old_remaining_price = (old_price / 365) * days

new_price = new_mb_price * (int(mailboxes) - 1) + new_plan_price
new_remaining_price = (new_price / 365) * days

if new_plan_price > old_plan_price:
        final_price = new_remaining_price - old_remaining_price
        print(CRED + '____________________________________\n\n>' + CEND + CYELLOW + ' The client has to pay ' + \ CYELLOWBG + '$'  + str(round(final_price, 2)) + CENDEND  + '\n' + CEND)
else:
        final_price = old_remaining_price - new_remaining_price
        print(CRED + '____________________________________\n\n>' + CEND + CYELLOW + ' We owe ' + CEND + \ CYELLOWBG + '$' + str(round(final_price, 2)) + CENDEND + CYELLOW + ' to the client.\n' + CEND)
