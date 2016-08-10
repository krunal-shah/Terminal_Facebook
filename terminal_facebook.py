from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait 
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
import getpass
from bs4 import BeautifulSoup
import terminal_facebook_module
import threading

print "Welcome to Terminal Facebook!"
emailid = raw_input("Facebook email id:")
pwd = getpass.getpass("Facebook password:")

print "The functionalities work like this:"
print "m : private message someone"
print "u : read the unread messages"
print "c : check for unread messages"
print "r : read the recent messages of conversation with someone"
print "p : post something on your wall"
print "w : post on someone's wall"
print "q : quit"

driver = webdriver.Chrome()
main_window = driver.current_window_handle
#Facebook login
driver.get("https://www.facebook.com")
email = driver.find_element_by_name("email")
email.send_keys(emailid)
password = driver.find_element_by_name("pass")
password.send_keys(pwd)
password.submit()


while True:
	inp = raw_input("What would you like to do?"+"\n")
	
	#Check for unread messages
	driver.get("https://www.facebook.com")
	page = driver.page_source
	soup = BeautifulSoup(page,"html.parser")
	num = soup.find('span',id='mercurymessagesCountValue').string
	print ""
	if num != 0:
		print "You have unread messages from %s conversations!"%(num)
	else:
		print "You do not have any unread messages"
	print "" 

	functionality =  inp[0]
	if functionality == "m":
		first_space = inp.find(" ",2,)
		second_space = inp.find(" ",first_space+1,)
		name = inp[2:second_space]
		message = inp[second_space:]
		terminal_facebook_module.message_someone(driver,name,message)
	elif functionality == "u":
		terminal_facebook_module.unread_messages(driver,num)
	elif functionality == "r":
		name = inp[2:]
		terminal_facebook_module.read_recent_messages(driver,name)
	elif functionality == "p":
		first_space = inp.find(" ",2,)
		content = inp[2:]
		terminal_facebook_module.post(driver,content)
	elif functionality == "w":
		first_space = inp.find(" ",2,)
		second_space = inp.find(" ",first_space+1,)
		name = inp[2:second_space]
		message = inp[second_space:]
		terminal_facebook_module.write_on_wall(driver,name,message)
	elif functionality == "q":
		break
'''elif functionality == "c":
		terminal_facebook_module.check_for_messages(driver)'''
	
