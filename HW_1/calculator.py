def calculate(first_operand: int, second_operand: int, operator: str):
    match operator:
        case '+':
            result = first_operand + second_operand
        case '-':
            result = first_operand - second_operand
        case '*':
            result = first_operand * second_operand
        case '/':
            if second_operand != 0:
                result = first_operand / second_operand
            else:
                raise ArithmeticError("Делить на 0 нельзя!")
        case _:
            raise ValueError("Вы ввели неверный оператор: " + operator)
    return result


def calculate_discount(purchase_amount: float, discount_amount: int):
    if discount_amount < 0:
        raise ArithmeticError("Процент не может быть меньше 0!")
    elif discount_amount > 100:
        raise ArithmeticError("Процент не может быть больше 100!")

    return purchase_amount - discount_amount / 100 * purchase_amount
