from typing import TypeVar, Generic
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None: #пустой стэк
        self._items: list[T] = []

    def push(self, item: T) -> None: #добавляем элемент в стэк
        self._items.append(item)

    def pop(self) -> T: #удаляем элемент из стэка
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T: #просматриваем верхний элемент стэка
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]


    def is_empty(self) -> bool: #проверяем пустой ли стэк
        return len(self._items) == 0

    def size(self) -> int: #возвращаем размер стэка
        return len(self._items)

if __name__ == "__main__":
    my_stack: Stack[str] = Stack()# создаём стек для строк
    print(f"Стек пуст? {my_stack.is_empty()}")

    my_stack.push("hello")
    my_stack.push("world")
    print(f"Размер стека: {my_stack.size()}")
    print(f"Верхний элемент: {my_stack.peek()}")

    item = my_stack.pop()
    print(f"Вытащили: {item}")  # world
    print(f"Размер после pop: {my_stack.size()}")
    print(f"Стек пуст? {my_stack.is_empty()}")

    item2 = my_stack.pop() # теперь удаляем оставшийся "hello"
    print(f"Вытащили: {item2}")
    print(f"Размер после pop: {my_stack.size()}")
    print(f"Стек пуст? {my_stack.is_empty()}") 