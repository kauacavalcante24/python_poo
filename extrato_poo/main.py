from datetime import date, datetime
from functions import (
    create_category,
    create_transaction,
    final_balance
)
print("="*40)
print()
print("TRANSAÇÕES")
print()

category_roadtrip = create_category('Viagens')
category_money = create_category('Salário')

transaction_roadtrip = create_transaction(
    'Trabalho',
    -54,
    category_roadtrip,
    date.today().strftime('%d/%m/%Y'),
    datetime.now().strftime('%H:%M:%S')
)

transaction_money = create_transaction(
    'Salário Base Mensal',
    1500, category_money,
    date.today().strftime('%d/%m/%Y'),
    datetime.now().strftime('%H:%M:%S')
)

final_balance()

print()
print("="*40)
