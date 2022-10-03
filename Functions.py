def count_clients(date=None, card=None, account=None, account_valid_to=None,
                  client=None, last_name=None, first_name=None, patronymic=None,
                  date_of_birth=None, passport=None, passport_valid_to=None, phone=None,
                  oper_type=None, amount=None, oper_result=None, terminal=None,
                  terminal_type=None, city=None, address=None):

    requires = {}
    for item in ['date', 'card', 'account', 'account_valid_to', 'client',
                 'last_name', 'first_name', 'patronymic', 'date_of_birth',
                 'passport', 'passport_valid_to', 'phone', 'oper_type',
                 'amount', 'oper_result', 'terminal', 'terminal_type', 'city', 'address']:
        exec('''if {} != None:
                    requires["{}"] = {}'''.format(*[item] * 3))

    array = []
    for el in dict:
        for el2 in el:
            arr = el[el2]
            for item in requires:
                if arr[item] == requires[item]:
                    pass
                else:
                    break
            else:
                array.append(el2)

    return array