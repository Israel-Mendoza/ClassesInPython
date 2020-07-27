import pytz
from Bank import Bank
from time import sleep
from random import randint, choice

banamex = Bank("CitiBanamex")
mx_tz = pytz.timezone("America/Mexico_City")
my_account = banamex.create_account("Israel", "Mendoza", 5000, mx_tz)
transactions = [my_account.deposit, my_account.withdraw, my_account.apply_interest]

for i in range(0, 25):
    method = choice(transactions)
    if method is transactions[2]:
        method()
    else:
        method(randint(0, 5000))
    sleep(.5)

for txn in my_account.transaction_list:
    print(txn.transaction_id)

last_txn = banamex.transaction_lookup(txn.transaction_id)

print(last_txn)
