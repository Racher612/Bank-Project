import json


#функция, которая осуществляет отсев и вывод нужных параметров
def clear_transactions(dict, out):
    data = {}
    required_options = ['date', 'card', 'account', 'account_valid_to', 'client',
                        'last_name', 'first_name', 'patronymic', 'date_of_birth',
                        'passport', 'passport_valid_to', 'phone', 'oper_type',
                        'amount', 'oper_result', 'terminal', 'terminal_type', 'city', 'address']
    if out:
        m = len(max(required_options, key = len))
    for item in required_options:
        data[item] = dict[item]
        if out:
            print(item.ljust(m, "_"), "_"*8, data[item], sep = '')
    return

def reading_file(file):
    with open(file) as f:
        data = json.load(f)         #json нужен для декодирования символов кириллицы

    k = 0
    data = data["transactions"]     #исходные данные заключены во внешний словарь, который требуется очистить
    for item in data:
        data[item] = clear_transactions(data[item], True)
        k += 1
        print()
        if k == 15:
            break



reading_file('transactions.json')