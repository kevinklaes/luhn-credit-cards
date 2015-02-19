import unittest

from card_exceptions import CardError
from luhn import Amex, Card, Discover, MasterCard, Visa


class TestCard(unittest.TestCase):

    def test_non_specific_card(self):
        with self.assertRaises(CardError):
            card = Card("583093240")
            card.is_valid_card()


class TestMasterCard(unittest.TestCase):

    def test_valid_card(self):
        card = MasterCard("5555555555554444")
        assert card.is_valid_card()

    def test_wrong_length(self):
        card = MasterCard("555555555555444")
        assert not card.is_valid_card()


class TestVisa(unittest.TestCase):

    def test_valid_card(self):
        card = Visa("4242424242424242")
        assert card.is_valid_card()

    def test_wrong_starts_with(self):
        card = Visa("3012888888881881")
        assert not card.is_valid_card()


class TestAmex(unittest.TestCase):

    def test_valid_card(self):
        card = Amex("378282246310005")
        assert card.is_valid_card()

    def test_wrong_length(self):
        card = Amex("3714496353984315")
        assert not card.is_valid_card()


class TestDiscover(unittest.TestCase):

    def test_valid_card(self):
        card = Discover("6011111111111117")
        assert card.is_valid_card()

    def test_invalid_card(self):
        card = Discover("601111111111111")
        assert not card.is_valid_card()


if __name__ == '__main__':
    unittest.main()


