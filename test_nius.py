import unittest
from unittest.mock import patch
import nius

class TestNius(unittest.TestCase):

    def test_format_hn_text_markdown(self):
        """Test if HTML tags are correctly converted to Markdown-style."""
        raw_html = "Hello <i>world</i><p>This is a <pre><code>code</code></pre>"
        expected = "Hello *world*\n\nThis is a \n\n[CODE]\ncode\n[END CODE]\n"
        
        result = nius.format_hn_text(raw_html)
        self.assertEqual(result, expected)

    def test_format_hn_text_empty(self):
        """Test handling of None or empty strings."""
        self.assertEqual(nius.format_hn_text(None), "")
        self.assertEqual(nius.format_hn_text(""), "")

    @patch('requests.get')
    def test_fetch_item_failure(self, mock_get):
        """Test that the app handles API failures gracefully."""
        # Force the mock internet to return a failure
        mock_get.side_effect = Exception("Connection Timeout")
        
        result = nius.fetch_item(12345)
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()