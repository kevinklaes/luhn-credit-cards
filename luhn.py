#!/usr/bin/python
"""
Use the Luhn alogrithm to sanity check submitted credit card numbers.
While we can't verify these are legit, we can prevent useless calls to
payment sites by using this technique.
"""

from card_exceptions import CardError


class Card:
    valid_card = None
    card_number = None
    starts_with = []
    accepted_length = []

    def __init__(self, number):
        if not number:
            raise CardError("You must specifyc a card number.")
        self.card_number = number

    def is_valid_card(self):
        if self.valid_card == None:
            self._validate_card()
        return self.valid_card

    def _luhn_algo(self, card_str):
        """
        Luhn Algorithim
        http://en.wikipedia.org/wiki/Luhn_algorithm
        """
        total = 0
        for i, num in enumerate(card_str[::-1]):
            if (i+1) % 2 == 0:
                # Double every other number.
                num = int(num) * 2
            for j in str(num):
                total += int(j)
        if total % 10 == 0:
            return True
        else:
            return False

    def _prefix_check(self, card_str):
        """
        Check the prefix of the card to see if it matches the card type.
        """
        return False if not any(
            [card_str.startswith(str(sw)) for sw in self.starts_with]
        ) else True

    def _length_check(self, card_str):
        """
        Check the length of the card to see if it matches the card length
        """
        return False if not len(card_str) == self.accepted_length else True

    def _validate_card(self):
        """
        Sets self.valid_card to True if the card passes these sanity checks
        and False if it doesn't. Doesn't reprocess when the card doesn't pass
        since a new instance should be instantiated.
        """
        if not all([self.starts_with, self.accepted_length]):
            raise CardError(
                "You must specify the length of the card number and the "
                "number of digits in the card."
            )
        if not self.valid_card:
            # Check the simple things
            card_str = str(self.card_number)
            self.valid_card = True if all([
                self._length_check(card_str),
                self._prefix_check(card_str),
                self._luhn_algo(card_str)
            ]) else False


class MasterCard(Card):
    starts_with = [51, 52, 53, 54, 55]
    accepted_length = 16


class Visa(Card):
    starts_with = [4]
    accepted_length = 16


class Amex(Card):
    starts_with = [34, 37]
    accepted_length = 15


class Discover(Card):
    starts_with = [6011]
    accepted_length = 16


