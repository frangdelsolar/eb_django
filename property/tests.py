from django.test import TestCase

# Create your tests here.


class ListViewTest(TestCase):
    def test_call_view_load(self):
        """
        Tests ListView loads properly and uses the right template
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'property/list.html')
