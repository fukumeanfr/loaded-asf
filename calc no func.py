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
        if not history:
            print("История пуста")
        print("------------ История -------------")
        for i, record in enumerate(history, 1):
            print(f"{i}) {record}")
        continue

    if user_input == 'clear':
        history.clear()
        print("История очищена")
        continue

    parts: list = user_input.split()
    if len(parts) != 3:
        print("Ошибка формата (пример: 5 + 3)")
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
            print("Ошибка: деление на ноль")
            continue
        result = num1 / num2
    else:
        print(f"Ошибка: оператор '{op}' не поддерживается")
        continue

    if result == int(result):
        result = int(result)

    print(f"Результат: {result}")
    history.append(f"{user_input} = {result}")
    if len(history) > 5:
        history.pop(0)