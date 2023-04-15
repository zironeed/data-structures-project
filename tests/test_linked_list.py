"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList, Node


class TestSrc(unittest.TestCase):
    def test_node_init(self):
        node1 = Node('data')
        node2 = Node('data', 'data2')
        self.assertEqual(node1.data, 'data')
        self.assertEqual(node1.next_node, None)
        self.assertEqual(node2.data, 'data')
        self.assertEqual(node2.next_node, 'data2')

    def test_linkedlist_init(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.tail, None)
        self.assertEqual(linked_list.head, None)

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning('1')
        self.assertEqual(ll.head.data, '1')
        self.assertEqual(ll.tail.data, '1')
        ll.insert_beginning('2')
        self.assertEqual(ll.head.data, '2')
        self.assertEqual(ll.tail.data, '1')

    def insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end('1')
        self.assertEqual(ll.head.data, '1')
        self.assertEqual(ll.tail.data, '1')
        ll.insert_at_end('2')
        self.assertEqual(ll.head.data, '1')
        self.assertEqual(ll.tail.data, '2')

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertEqual(ll.to_list(), [[1, 'lazzy508509'], [2, 'mosh_s']])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        self.assertEqual(ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})

        node = ll.get_data_by_id(22)
        self.assertIsNone(node)
