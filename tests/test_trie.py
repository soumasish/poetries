import unittest

from poetries.trie import Trie


class TestTrie(unittest.TestCase):
    def test_add_find(self):
        trie = Trie()
        trie.add('foo')
        trie.find('bar')
        self.assertEqual(trie.find('foo'), True)

    def test_all_words_with_prefix(self):
        trie = Trie()
        trie.add('foo')
        trie.add('foof')
        trie.add('foob')
        trie.add('foobar')
        arr = list(trie.all_words_with_prefix('foo'))
        self.assertEqual(len(arr), 4)
