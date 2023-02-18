from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

# # CERINTE
# #Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
# # ● Id
# #● Link text
# #● Parțial link text
# #● Name
# #● Tag*
# #● Class name*
# #● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
# #observație:
# #- Probabil nu vei găsi un singur website care să cuprindă toate variantele
# #de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
# #- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
# #Interactionează cu un element la alegere din listă.

# REZOLVARE:
driver = webdriver.Chrome() # instantiem obiectul driver
driver.get ('https://phptravels.net/')
driver.maximize_window()
driver.implicitly_wait(5) # asteptam sa se incarce pagina web

#  By ID
driver.find_element(By.ID, 'currency').click() # click pe buttonul USD -care selecteaza moneda
driver.find_element(By.ID, 'ACCOUNT').click() # click pe butonul ACCOUNT
driver.find_element(By.ID, 'hotels-tab').click() # click pe optiunea Hotels (cu iconita in fata)
time.sleep(1)

# By Link text -
driver.find_element(By.LINK_TEXT, 'Offers').click() #click pe sectiunea 'Offers' din partea de sus a paginii
time.sleep(1)
driver.find_element(By.LINK_TEXT, 'Blog').click() #click pe sectiunea 'Blog' din partea de sus a paginii
time.sleep(1)
driver.find_element(By.LINK_TEXT, 'Transfers').click() #click pe sectiunea 'Transfers' din partea de sus a paginii
time.sleep(1)

# By Name
driver.get ('https://phptravels.net/') #revenim pe Homepage (eram pe pagina cu 'Transfers')
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID, 'flights-tab').click() #este necesar sa dam click pe sectiunea 'Flights'precedata de iconita
# asteptam sa se incarce pagina web
driver.find_elements(By.NAME, 'trip')[1].click() #click pe radio button 'Round Trip' din sectiunea 'Flights'
time.sleep(3)
# precedata de iconita
driver.find_elements(By.NAME,'from')[0].send_keys('Henri Coanda') # apoi in sectiunea 'Flying from' introducem
#aeroportul 'Henri Coanda'
driver.find_elements(By.NAME,'to')[0].send_keys('Paris') # iar in sectiunea 'To Destination' introducem 'Paris'
time.sleep(1)

# By Partial link text
driver = webdriver.Chrome()
driver.get ('https://the-internet.herokuapp.com/')
driver.maximize_window()
driver.implicitly_wait(5) # asteptam ca pagina sa se incarce
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sortable').click() #click pe sectiunea 'Sortable Data Tables'
driver.back() # revenim la Homepage
driver.find_element(By.PARTIAL_LINK_TEXT, 'Editor').click() #click pe sectiunea 'WYSIWYG Editor'
driver.back()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Form').click() #click pe sectiunea 'Form Authentication'
time.sleep(1)

# By Tag
driver.get ('https://phptravels.net/')
driver.maximize_window()
driver.implicitly_wait(5) # asteptam sa se incarce pagina web
list_h4 = driver.find_elements(By.TAG_NAME, 'h4')
print(len(list_h4))
for i in range(len(list_h4)):
    print(list_h4[i].text)

#By Class Name
list_same_class_name = driver.find_elements(By.CLASS_NAME, 'c8LPF-icon')
list_same_class_name[0].click()
time.sleep(1)
list_same_class_name_1 = driver.find_elements(By.CLASS_NAME, 'form-control')
list_same_class_name_1[-1].send_keys('ramona.vascul@gmail.com')
time.sleep(1)
list_same_class_name_2 = driver.find_elements(By.CLASS_NAME, 'dropdown-toggle')
list_same_class_name_2[0].click()
time.sleep(1)

#CSS -ID
driver.get ('https://phptravels.net/flights') #intram pe pagina 'Flights'
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '#autocomplete').send_keys('Henri Coanda') # input nu e obligatoriu! #diez-ID
# se completeaza campul "flying from"
time.sleep(1)
# CSS -CLASS
driver.find_element(By.CSS_SELECTOR, 'input.px-5').send_keys('Rotterdam') #input nu e obligatoriu! .punctul- clasa
# se completeaza campul "to destination"
time.sleep(1)
# CSS - Atribut-valoare
placeholder_text = driver.find_element(By.CSS_SELECTOR,'input[type="email"]').send_keys('ramona.vascul@gmail.com')
# se completeaza campul "email" din josul paginii
time.sleep(1)

# #CERINTE
# #Pentru Xpath identifică elemente după criteriile de mai jos:
# # ● 3 după atribut valoare
# # ● 3 după textul de pe element
## ● 1 după parțial text
## ● 1 cu SAU, folosind pipe |
## ● 1 cu *
## ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
## cu (xpath)[1]
## ● 1 în care să folosești parent::
## ● 1 în care să folosești fratele anterior sau de după (la alegere)
## ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
## ce element vreau să interacționez.

#  REZOLVARE :
# By XPath -3 exemple dupa atribut-valoare
driver.get ('https://formy-project.herokuapp.com/')
driver.maximize_window()
driver.implicitly_wait(5) # asteptam sa se incarce pagina web
driver.find_element(By.XPATH, '//a[@id="navbarDropdownMenuLink"]').click() #click pe sectiunea 'Components' din partea
# de sus a paginii
time.sleep(1)
driver.get ('https://formy-project.herokuapp.com/form') #intram pe pagina '/form'
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//select[@class="form-control"]').send_keys('0-1') # se introduce in campul cu anii
# de experienta '0-1'
time.sleep(1)
driver.find_element(By.XPATH, '//input[@placeholder="mm/dd/yyyy"]').send_keys('09/29/2023') # introduce data aleasa
# in campul cu data calendaristica
time.sleep(1)
driver.find_element(By.XPATH, '//a[@role="button"]').click() #click pe butonul 'Submit' din josul paginii
time.sleep(1)

# By XPath -3 exemple dupa textul de pe element
driver.get ('https://formy-project.herokuapp.com/autocomplete') #intram pe pagina '/autocomplete'
driver.maximize_window()
driver.implicitly_wait(5)
elem_containing_street_text = driver.find_elements(By.XPATH, '//*[contains(text(),"Street")]')
print (f'Numarul de elemente care contin textul "Street" este {len(elem_containing_street_text)}')
for i in range(len(elem_containing_street_text)):
    print (f'Acestea sunt : {elem_containing_street_text[i].text}')
elem_containing_country_text = driver.find_element(By.XPATH, '//*[contains(text(),"Country")]').text
print (f'Elementul care contine textul "country" este: {elem_containing_country_text}')
driver.get ('https://formy-project.herokuapp.com/radiobutton') #intram pe pagina '/radiobutton'
driver.maximize_window()
driver.implicitly_wait(5)
elem_containing_radio_text = driver.find_elements(By.XPATH, '//*[contains(text(),"Radio")]')
print (f'Numarul de elemente care contin textul "Radio" este {len(elem_containing_radio_text)}')
for i in range(len(elem_containing_radio_text)):
     print (f'Acestea sunt : {elem_containing_radio_text[i].text}')

# By XPath -1 exemplu dupa partial text
driver.get ('https://formy-project.herokuapp.com/keypress') #intram pe pagina '/keypress'
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_elements(By.XPATH, '//*[contains(@type,"ton")]')[1].click()
text_complet = driver.find_elements(By.XPATH, '//*[contains(@type,"ton")]')[1].text
print(text_complet)
time.sleep(1)

#By Xpath with |
driver.get('https://formy-project.herokuapp.com/checkbox') # intram pe pagina cu checkbox
driver.maximize_window()
driver.implicitly_wait(5)
# driver.find_element(By.XPATH, '//input[@id="checkbox-1"] | //input[@id="checkbox-2"]|//input[@id="checkbox-3"]').click()
time.sleep(1)
# Obs! daca gaseste primul element il completeaza doar pe el, iar daca nici un element nu exista returneaza "Error"
# with or
driver.find_element(By.XPATH, '//input[@id="checkbox-2"or @id="checkbox-1"]').click() #il bifeaza pe "check-box1"
#deoarece pe acela il gaseste primul
time.sleep(1)

#BY Xpath cu *
driver.get ('https://formy-project.herokuapp.com/radiobutton') #intram pe pagina '/radiobutton'
driver.maximize_window()
driver.implicitly_wait(5)
elem_containing_radio_text = driver.find_elements(By.XPATH, '//*[contains(text(),"Radio")]')
print (f'Numarul de elemente care contin textul "Radio" este {len(elem_containing_radio_text)}')
for i in range(len(elem_containing_radio_text)):
     print (f'Acestea sunt : {elem_containing_radio_text[i].text}')

#By Xpath cu parent:: si cu fratele anterior sau de după
driver.get ('https://formy-project.herokuapp.com/buttons') #intram pe pagina '/buttons'
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element\
    (By.XPATH, '//div/div[@class="input-group"]/div[@class="col-sm-8"]/button/following-sibling::button[5]').click()
# am navigat putin si la final am dat click pe butonul "Link"
time.sleep(1)
# 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu ce element vreau să interacționez.
# exemplu de la clasa
driver = webdriver.Chrome() # instantiem obiectul driver
driver.get ('https://formy-project.herokuapp.com/autocomplete') # pe pagina de autocomplete
driver.maximize_window()
driver.implicitly_wait(5) # asteptam sa se incarce pagina web
def autocomplete_page_input (placeholder_text, input_text):
    input = driver.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]') # au fost identificate 7 elem
    input.clear() #stergem placeholder-ul existent
    input.send_keys(input_text) #trimite noul placeholder introdus prin parametru
autocomplete_page_input('Enter address','function for replacing address') #apelarea functiei pt cele 7 elem
autocomplete_page_input('Street address','function for replacing Street address')
autocomplete_page_input('Street address 2','function for replacing Street address 2')
autocomplete_page_input('City','function for replacing City')
autocomplete_page_input('State','function for replacing State')
autocomplete_page_input('Zip code','function for replacing Zip code')
autocomplete_page_input('Country','function for replacing Country')
time.sleep(3)
driver.quit()




