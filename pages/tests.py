from django.test import SimpleTestCase

HTTP_OK = 200


class SimpleTests(SimpleTestCase):

    def _check_status_code(self, target, status):
        self.assertEqual(self.client.get(target).status_code, status)

    def test_home_page_status_code(self):
        self._check_status_code(target='/', status=HTTP_OK)

    def test_about_page_status_code(self):
        self._check_status_code(target='/about/', status=HTTP_OK)
