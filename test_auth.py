import unittest
import auth_service


class TestRegistration(unittest.TestCase):
    def setUp(self):
        auth_service.users.clear()

    def test_successful_registration(self):
        result = auth_service.register_user("alice@example.com", "a-strong-pass-123")
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["state"], "pending_verification")

    def test_duplicate_registration(self):
        auth_service.register_user("alice@example.com", "a-strong-pass-123")
        result = auth_service.register_user("alice@example.com", "a-strong-pass-123")
        self.assertEqual(result["status"], 409)

    def test_short_password_rejected(self):
        result = auth_service.register_user("bob@example.com", "short")
        self.assertEqual(result["status"], 400)


if __name__ == "__main__":
    unittest.main()