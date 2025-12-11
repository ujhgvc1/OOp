# --- Queue (OOP) ---
from typing import Generic, TypeVar
from collections import deque

T = TypeVar('T')

class Queue(Generic[T]):
    # --- init --- создаём пустую очередь на deque
    def __init__(self) -> None:
        self._items: deque[T] = deque()

    # --- enqueue --- добавляем в конец
    def enqueue(self, item: T) -> None:
        self._items.append(item)

    # --- dequeue --- забираем из начала (O(1))
    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("очередь пустая")
        return self._items.popleft()

    # --- peek --- смотрим первый без удаления
    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("очередь пустая")
        return self._items[0]

    # --- utils --- проверка и размер
    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

# --- демо ---
if __name__ == "__main__":
    q = Queue[str]()
    q.enqueue("один")
    q.enqueue("два")
    print("Первый:", q.peek())
    print("Достали:", q.dequeue())
    print("Осталось:", q.size())