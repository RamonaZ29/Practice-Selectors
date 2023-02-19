from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Implementează o clasă Login care să moștenească unittest.TestCase
# Gasește elementele în partea de sus folosind ce selectors dorești:
# - setUp()
# - Driver
# https://the-internet.herokuapp.com/
# Click pe Form Authentication
# tearDown()
# Quit browser
class Login(unittest.TestCase):

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get("https://the-internet.herokuapp.com/")
		self.driver.maximize_window()
		self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
		self.driver.implicitly_wait(3)

	def tearDown(self) -> None:
		self.driver.quit()

	# Test 1 - Verifică dacă noul url e corect
	def test_1(self):
		current_link = self.driver.current_url
		assert current_link == 'https://the-internet.herokuapp.com/login',\
			f' The expected URL: "https://the-internet.herokuapp.com/login" but went: {current_link}'

	# Test 2 - Verifică dacă page title e corect
	def test_2(self):
		page_title = self.driver.title
		assert page_title == 'The Internet', f'Expected the title "The Internet" but went: {page_title}'

	# Test 3 - Verifică textul de pe elementul xpath=//h2 e corect
	def test_3(self):
		text_check_on_element = self.driver.find_element(By.XPATH, '//h2').text
		assert text_check_on_element == 'Login Page', f'Expected the text "Login Page" but went: {text_check_on_element}'

	# Test 4 - Verifică dacă butonul de login este displayed
	def test_4(self):
		self.driver.find_element(By.CSS_SELECTOR, '[class="radius"]').is_displayed()

	#Test 5 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
	def test_5(self):
		elemental_selenium_link = self.driver.find_element(By.LINK_TEXT,'Elemental Selenium').get_attribute('href')
		assert elemental_selenium_link == 'http://elementalselenium.com/',\
			f'The expected link is "http://elementalselenium.com/" but went: {elemental_selenium_link}'

	#Test 6
	# - Lasă goale user și pass
	# - Click login
	# - Verifică dacă eroarea e displayed
	def test_6(self):
		self.driver.find_element(By.CSS_SELECTOR, '[class="radius"]').click()
		self.driver.find_element(By.CSS_SELECTOR, '.flash').is_displayed()

	#Test 7
	#- Completează cu user și pass invalide
	#- Click login
	#- Verifică dacă mesajul de pe eroare e corect
	#- Este și un x pus acolo extra așa că vom folosi soluția de mai jos
	#expected = 'Your username is invalid!'
	#self.assertTrue(expected in actual, 'Error message text is incorrect')
	def test_7(self):
		self.driver.find_element(By.ID, 'username').send_keys('ramonaz')
		self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPass123')
		self.driver.find_element(By.CSS_SELECTOR, '[class="radius"]').click()
		error_message = self.driver.find_element(By.CSS_SELECTOR, '.flash').text
		assert 'Your username is invalid!' in error_message, \
			f'The expected message is: "Your username is invalid!" but went: {error_message}'

	# Test 8
	# - Lasă goale user și pass
	# - Click login
	# - Apasă x la eroare
	# - Verifică dacă eroarea a dispărut
	def test_8(self):
		self.driver.find_element(By.CSS_SELECTOR, '[class="radius"]').click()
		self.driver.find_element(By.XPATH, '//a[@class="close"]').click()
		self.driver.implicitly_wait(10)
		assert not self.driver.find_element(By.ID, 'flash').is_displayed()

	# Test 9
	# - Ia ca o listă toate //label
	# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)
	# - Aici e ok să avem 2 asserturi
	def test_9(self):
		label_tag_list = self.driver.find_elements(By.XPATH, '//label')
		assert label_tag_list[0].text == 'Username', f'The expected text is: "Username" but went {label_tag_list[0].text}'
		assert label_tag_list[1].text == 'Password', f'The expected text is :"Password" but went {label_tag_list[1].text}'

	# Test 10
	# - Completează cu user și pass valide
	# - Click login
	# - Verifică ca noul url CONTINE /secure
	# - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
	# - Verifică dacă elementul cu clasa=’flash succes’ este displayed
	# - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
	def test_10(self):
		self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
		self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
		self.driver.find_element(By.CSS_SELECTOR, '[class="radius"]').click()
		self.driver.implicitly_wait(2)
		new_url = self.driver.current_url
		assert '/secure' in new_url, f'The expected url is : "/secure" but went {new_url}'
		# explicit wait
		WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="flash success"]')))
		# verifica daca elem cu clasa='flash succes' este afisat
		assert self.driver.find_element(By.XPATH, '//*[@class="flash success"]').is_displayed()
		# verifica daca mesajul contine 'secure area!'
		succes_login_message = self.driver.find_element(By.XPATH, '//*[@class="flash success"]').text
		containing_message = 'secure area!'
		assert containing_message in succes_login_message, f'The actual text does not contain {containing_message}'

	# Test 11
	# - Completează cu user și pass valide
	# - Click login
	# - Click logout
	# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
	def test_11(self):
		self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
		self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
		self.driver.find_element(By.CSS_SELECTOR, '[class="radius"]').click()
		self.driver.find_element(By.CLASS_NAME, 'icon-signout').click()
		login_url = self.driver.current_url
		assert login_url == 'https://the-internet.herokuapp.com/login',\
			f' The expected url is "https://the-internet.herokuapp.com/login" but went: {login_url}'
		self.driver.quit()

