from django.test import TestCase

# Create your tests here.
from snippets.models import Snippet

class SnippetTestCase(TestCase):
    def setUp(self):
        Snippet.objects.create(title="test", code="test", linenos=False, language="python", style="friendly")

    def test_can_get_snippet(self):
        snippet = Snippet.objects.get(title="test")
        self.assertEqual(snippet.language, 'python')