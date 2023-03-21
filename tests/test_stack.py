"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack, Node


class TestSrc(unittest.TestCase):

    def test_node_init(self):
        n = Node('a', None)
        m = Node('a', 'n')
        self.assertEqual(n.data, 'a')
        self.assertEqual(m.next_node, 'n')

    def test_stack_init(self):
        s = Stack()
        self.assertEqual(s.top, None)

    def test_stack_push(self):
        s = Stack()
        s.push('data1')
        s.push('data2')
        self.assertEqual(s.top.data, 'data2')
        self.assertEqual(s.top.next_node.data, 'data1')

    def test_stack_pop(self):
        s = Stack()
        s.push('data1')
        s.push('data2')
        data = s.pop()
        self.assertEqual(data, 'data2')

    def test_str(self):
        s = Stack()
        self.assertEqual(str(s), "I'm Stack")

