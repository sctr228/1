def checker(*exc_types):
    def checker(function):
        def checker(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except (exc_types) as exc:
                print(f'We heve a problem {exc}')
            else:
                print(f'No problems. Result - {result}')
        return checker
    return checker

@checker(NameError,TypeError,SyntaxError,ZeroDivisionError)
def calculate(expression):
    return eval(expression)

a = input('Введіть приклад: ')
calculate(f'{a}')