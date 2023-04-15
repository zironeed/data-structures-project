class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data: str, next_node: str = None) -> None:
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self) -> list:
        node_list = []
        node = self.head

        while node:
            node_list.append(list(node.data.values()))
            node = node.next_node

        return node_list

    def get_data_by_id(self, id) -> Node:
        node_list = []
        node = self.head

        while node:
            try:
                if node.data["id"] == id:
                    return node.data
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
            node = node.next_node
