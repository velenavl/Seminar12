# 📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.


import json


class Factorial:

    def __init__(self, amount: int = 1) -> None:
        self.results = []
        self.amount = amount

    def __call__(self, limit: int = 1) -> list[int]:
        if limit < 0:
            raise ValueError("Incompatible value")
        if limit in (0, 1):
            self.results.append(1)
        else:
            result = 1
            for i in range(1, limit + 1):
                result *= i
                self.results.append(result)


        return self.results[-self.amount:]

    def __repr__(self):
        return f'{self.results}'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('result.json', 'w', encoding="UTF-8") as file:
            json.dump(self.results, file)


def main():
    with Factorial(5) as fact:
        print(fact(10))


if __name__ == '__main__':
    main()
    