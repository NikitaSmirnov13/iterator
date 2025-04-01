import types  # Импортируем модуль types для проверки типа генератора


class FlatIterator:
    """Итератор для плоского представления списка списков."""

    def __init__(self, list_of_list):
        # Инициализируем исходный список и индексы
        self.list_of_list = list_of_list  # Входной список списков
        self.outer_index = 0  # Текущий индекс внешнего списка
        self.inner_index = 0  # Текущий индекс во внутреннем списке

    def __iter__(self):
        # Возвращаем сам итератор
        return self

    def __next__(self):
        # Метод возвращает следующий элемент или вызывает StopIteration
        while self.outer_index < len(self.list_of_list):
            current_sublist = self.list_of_list[self.outer_index]
            if self.inner_index < len(current_sublist):
                # Получаем текущий элемент
                item = current_sublist[self.inner_index]
                self.inner_index += 1
                return item
            # Переходим к следующему подсписку
            self.outer_index += 1
            self.inner_index = 0
        # Если все элементы пройдены
        raise StopIteration


def flat_generator(list_of_lists):
    """Генератор для плоского представления списка списков."""
    for sublist in list_of_lists:  # Итерируемся по каждому подсписку
        for item in sublist:  # Итерируемся по каждому элементу подсписка
            yield item  # Возвращаем элемент


def test_1():
    """Тест для проверки FlatIterator."""

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # Проверяем корректность работы итератора
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item, f"Ожидалось {check_item}, получено {flat_iterator_item}"

    # Проверяем преобразование в список
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None], \
        "Неправильное плоское представление"


def test_2():
    """Тест для проверки flat_generator."""

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # Проверяем корректность работы генератора
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item, f"Ожидалось {check_item}, получено {flat_iterator_item}"

    # Проверяем преобразование в список
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None], \
        "Неправильное плоское представление"

    # Проверяем, что это действительно генератор
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType), \
        "flat_generator не является генератором"


if __name__ == '__main__':
    test_1()  # Запускаем тест итератора
    test_2()  # Запускаем тест генератора