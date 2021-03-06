import unittest

from httplib2 import Credentials

from user import User


class TestUser(unittest.TestCase):
    """
    test class that tests cases for the User class

    Args:
        unittest.Testcase: class that helps create test cases
    """

    def setUp(self):
        """
        set up method to run before each test case
        """
# create a user object
        self.new_user = User("kwepo", "7710")

    def tearDown(self):
        """
        method to clean up after each test
        """
        User.user_list = []

    def test_init(self):
        """
        to test if object is properly initialised
        """

        self.assertEqual(self.new_user.user_name, "Kwepo")
        self.assertEqual(self.new_user.user_password, "7710")

    def test_log_in(self):
        """
        test to establish whether user can log into their credentials
        """
        # start by saving user
        self.new_user.save_user()

        test_user = User("Hughes", "Mugera")

        test_user.save_user()

        found_credentials = User.log_in("Hughes", "Mugera")

        self.assertEqual(found_credentials, Credentials.credentials_list)

    def test_user_exists(self):
        """
        test to check if we can return return boolean if user does not exist
        """

        # first we save a user
        self.new_user.save_user()

        test_user = User("kwepo", "7710")  # new user

        test_user.save_user()

        # then with the existing contact
        user_exists = User.user_exists("kwepo")

        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main(verbosity=2)
