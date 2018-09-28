from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestDjango(TestCase):

    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({'name': 'Create Tests'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])


""" #Basic test
class TestDjango(TestCase):

    def test_is_this_thing_on(self):
        self.assertEqual(1, 1) """
