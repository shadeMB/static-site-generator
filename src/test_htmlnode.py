import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props_to_test = {"href": "https://www.google.com", "target": "_blank",}
        node = HTMLNode(None, None, None, props_to_test)
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

    def test_no_values(self):
        node = HTMLNode(None, None, None, None)
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value) 
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_values(self):
        node = HTMLNode(
            "div",
            "This is a test",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "This is a test",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode("p", "This is a test")
        self.assertEqual(
            node.__repr__(),
            "p=This is a test, None, None"
        )

if __name__ == "__main__":
    unittest.main()