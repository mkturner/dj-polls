import datetime

from django.test import TestCase
from django.utils import timezone

from poll.models import Question

# Create  your tests here.


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        '''
            should return false if published in the Future
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
