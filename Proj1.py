def show_history(history: list) -> None:
    """
    Отображает историю вычислений

    history: Список с записями истории
    """
    if not history:
        print("История пуста")
        return
    print("------------ История -------------")
    for i, record in enumerate(history, 1):
        print(f"{i}) {record}")


def add_to_history(history: list, expression: str, result: int | float) -> None:
    """
    Добавляет запись в историю вычислений
    Хранит не более 5 последних записей

    history: Список для хранения истории
    expression: Строка с выражением (например, '5 + 3')
    result: Результат вычисления
    """
    history.append(f"{expression} = {result}")
    if len(history) > 5:
        history.pop(0)


history: list = []

print("--------- Калькулятор ---------")
print("""Пример: 5 + 3
Команды:
history - показать историю
clear - очистить историю
exit - выйти из программы""")

while True:
    print("--------- Введите пример ---------")
    user_input: str = input().strip()

    if user_input == 'exit':
        print("------- Выход из программы -------")
        break

    if user_input == 'history':
        show_history(history)
        continue

    if user_input == 'clear':
        history.clear()
        print("История очищена")
        continue

    parts: list = user_input.split()
    if len(parts) != 3:
        print("Ошибка формата (пиши через пробел)")
        continue

    try:
        num1: float = float(parts[0])
        op: str = parts[1]
        num2: float = float(parts[2])
    except ValueError:
        print("Ошибка: введите числа")
        continue

    result: int | float | None = None
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Ошибка: деление на ноль невозможно")
            continue
        result = num1 / num2
    else:
        print(f"Ошибка: оператор '{op}' не поддерживается")
        continue

    if result == int(result):
        result = int(result)

    print(f"Результат: {result}")
    add_to_history(history, user_input, result)