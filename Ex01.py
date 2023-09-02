# 📌 Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


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
                if len(self.results) > self.amount:
                    self.results.pop(0)

        return self.results


def main():
    master = Factorial(3)
    print(master(5))            # здесь у экземпляра вызываем __call__(5) - подсчет факториала 5! и показывает последние 3 значения

    print(Factorial(3)(5))  # amount = 3, limit = 5

    print(Factorial()())

    print(Factorial(5)(8))


if __name__ == '__main__':
    main()
    