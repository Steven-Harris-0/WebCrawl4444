from selenium import webdriver

webd = webdriver.Firefox() #Opens firefox,
webd.get("https://www.cnn.com/")#uses Selenium driver to open CNN through FireFox

print (webd.find_element_by_xpath('//*[@id="homepage3-zone-1"]/div[6]/div/div[5]/ul').text) # Prints the element of Tech
print (webd.find_element_by_xpath('//*[@id="homepage3-zone-1"]/div[6]/div/div[7]/ul').text)# Prints the element Entertainment
print (webd.find_element_by_xpath('//*[@id="homepage3-zone-1"]/div[6]/div/div[8]/ul').text)#prints the element Travel


