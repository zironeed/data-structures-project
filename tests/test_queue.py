"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestSrc(unittest.TestCase):

    def test_node_init(self):
        node1 = Node('data')
        node2 = Node('data', 'atad')
        self.assertEqual(node1.data, 'data')
        self.assertEqual(node2.next_node, 'atad')

    def test_queue_init(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('one')
        queue.enqueue('two')
        self.assertEqual(queue.head.data, 'one')
        self.assertEqual(queue.tail.data, 'two')
        self.assertEqual(queue.head.next_node.data, 'two')

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('one')
        queue.enqueue('two')
        self.assertEqual(queue.dequeue(), 'one')
        self.assertEqual(queue.dequeue(), 'two')
        self.assertEqual(queue.dequeue(), None)


