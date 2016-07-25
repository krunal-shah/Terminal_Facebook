from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait 
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#import getpass
from bs4 import BeautifulSoup
import time

def message_someone(driver,name,content):
	action= ActionChains(driver)
	driver.get("https://www.facebook.com/messages/krunal.shah.iit.delhi")
	search = driver.find_elements_by_xpath("//div/div[1]/div/div[2]/div[1]/div[2]/span/span/input")
	action.click(search[0])
	action.perform()
	search[0].send_keys(name)
	search[0].send_keys(Keys.RETURN)
	message = driver.find_element_by_name("message_body")
	message.send_keys(content)
	message.send_keys(Keys.RETURN)

def unread_messages(driver,num):
	for i in range(int(num)):
		driver.get("https://www.facebook.com/messages")
		page = driver.page_source
		soup = BeautifulSoup(page,"html.parser")
		my_divs = soup.find_all("div","_l4")[i]
		a = str(my_divs.find_all("span")[0].string)
		print a+" : "+"\n"
		search = driver.find_elements_by_xpath("//div/div[1]/div/div[2]/div[1]/div[2]/span/span/input")
		search[0].send_keys(a)
		time.sleep(3)
		search[0].send_keys(Keys.RETURN)
		url = driver.current_url
		start = url.find('search/')+7
		end = url.find('?')
		username = url[start:end]
		url = "https://www.facebook.com/messages/"+str(username)+"/"
		driver.get(url)
		time.sleep(2)
		page = driver.page_source
		soup = BeautifulSoup(page,"html.parser")
		length = len(soup.find_all("div","_38 direction_ltr"))
		index=0
		for i in range(length):
			div = soup.find_all("div","_38 direction_ltr")[length-i-1]
			if str(div.parent.parent.parent.previous_sibling.find_all("a")[0].string)=="Krunal Shah":
				index = length-1-i
				break
		for j in range(index+1,length):
			print soup.find_all("div","_38 direction_ltr")[j].string
		print ""

def check_for_messages(driver):
	driver.get("https://www.facebook.com")
	page = driver.page_source
	soup = BeautifulSoup(page,"html.parser")
	num = soup.find('span',id='js_1').contents[0].string
	if num != 0:
		print "You have unread messages from %d conversations!"%(num)
	else:
		print "You do not have any unread messages"

def read_recent_messages(driver,name):
	driver.get("https://www.facebook.com/messages/krunal.shah.iit.delhi")
	search = driver.find_elements_by_xpath("//div/div[1]/div/div[2]/div[1]/div[2]/span/span/input")
	search[0].send_keys(name)
	search[0].send_keys(Keys.RETURN)
	time.sleep(3)
	url = driver.current_url
	start = url.find('search/')+7
	end = url.find('?')
	username = url[start:end]
	url = "https://www.facebook.com/messages/"+str(username)+"/"
	driver.get(url)
	time.sleep(2)
	page = driver.page_source
	soup = BeautifulSoup(page,"html.parser")
	for div in soup.find_all("div","_38 direction_ltr"):
		print str(div.parent.parent.parent.previous_sibling.find_all("a")[0].string) + " : " + str(div.string)

def post(driver,content):
	driver.get("https://www.facebook.com")
	action= ActionChains(driver)
	post = driver.find_element_by_name("xhpc_message")
	action.click(post)
	action.perform()
	post.send_keys(content)
	post.submit()

def write_on_wall(driver,name,content):
	driver.get("https://www.facebook.com/messages/krunal.shah.iit.delhi")
	search = driver.find_elements_by_xpath("//div/div[1]/div/div[2]/div[1]/div[2]/span/span/input")
	search[0].send_keys(name)
	search[0].send_keys(name)
	search[0].send_keys(Keys.RETURN)
	url = driver.current_url
	start = url.find('search/')+7
	end = url.find('?')
	username = url[start:end]
	url = "https://www.facebook.com/messages/"+str(username)+"/"
	message = driver.find_element_by_name("xhpc_message_text")
	message.send_keys(content)
	message.submit()


