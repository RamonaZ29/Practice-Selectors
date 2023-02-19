
from homework_9_verifiers import Login
import unittest
import HtmlTestRunner # pip install html-testRunner

# Faceti o suita care sa contina testele voastre de la tema 9 + testele de la intalnirea 10 (care au clasa).
# Generati raportul
class Test_Suite_tema_10(unittest.TestCase):
	def test_suite(self):
		smoke_testing = unittest.TestSuite()
		smoke_testing.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(Login))
		runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True)
		runner.run(smoke_testing)