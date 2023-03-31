class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self) -> None:
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data) -> None:
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        if not self.head:
            self.tail = node
            self.head = self.tail
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self) -> str:
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head:
            deleted_node = self.head.data
            new_head = self.head.next_node
            self.head = new_head
            return deleted_node
        else:
            return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return ''
