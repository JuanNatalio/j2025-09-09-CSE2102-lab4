import unittest
from my_server import trial_division, app

class TestTrialDivision(unittest.TestCase):
    def test_factors_of_12(self):
        self.assertEqual(trial_division(12), [2, 2, 3])

    def test_factors_of_13(self):
        self.assertEqual(trial_division(13), [13])

    def test_factors_of_360(self):
        self.assertEqual(trial_division(360), [2, 2, 2, 3, 3, 5])

    def test_factors_of_1(self):
        self.assertEqual(trial_division(1), [1])


class TestFlaskEndpoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_post_factors_12(self):
        response = self.client.post('/factors', data={'inINT': '12'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"factors": [2, 2, 3]})

    def test_post_factors_prime(self):
        response = self.client.post('/factors', data={'inINT': '13'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"factors": [13]})

    def test_post_factors_1(self):
        response = self.client.post('/factors', data={'inINT': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"factors": [1]})

    def test_post_factors_missing_param(self):
        response = self.client.post('/factors', data={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

if __name__ == "__main__":
    unittest.main()
