import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        # 1. Create a node with some props
        node = HTMLNode(
            "tag",
            "value",
            None,
            {"class": "primary", "href": "https://www.google.com"}
        )

        # 2. Call the method you want to test
        # 3. Use self.assertEqual() to check if the result matches what you expect
        # self.assertEqual(..., ...)

        # Add more test methods here! 
        # Try testing a node with None for props, or different tags.

if __name__ == "__main__":
    unittest.main()