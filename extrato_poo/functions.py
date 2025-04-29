from category import Category
from transaction import Transaction


TRANSACTION_LIST = []
CATEGORY_LIST = []


def create_category(category):
    category_object = Category(category)
    CATEGORY_LIST.append(category_object)
    return category_object


def create_transaction(detail, value, category, date, time):
    transaction_object = Transaction(
        detail=detail,
        value=value,
        category=category,
        date=date,
        time=time,
    )
    TRANSACTION_LIST.append(transaction_object)
    return transaction_object


def final_balance():
    final = 0
    print()
    for obj in TRANSACTION_LIST:
        final += obj.value
        print(obj)
        print()
    print()
    return print(f'Saldo final: {final}')
