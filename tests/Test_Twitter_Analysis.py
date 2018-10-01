
import unittest
import xmlrunner
from nltk.corpus import stopwords

class TestStringMethods(unittest.TestCase):

    def test_stop_words_content(self):
        stopwords_set = set(stopwords.words("english"))
        self.assertIn("against",stopwords_set,"Stop words content passed")
       # self.assertEqual('foo'.upper(), 'FOO')

    def test_stop_words_size(self):
        stopwords_set = set(stopwords.words("english"))
        print(len(stopwords_set))
        self.assertEqual(179,len(stopwords_set),"Stop words size passed")
       # self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':


    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports.xml'),
        failfast=False,
        buffer=False,
        catchbreak=False)