from selenium.webdriver.common.by import By

class HomePage():
    registerlink=(By.LINK_TEXT,"Register")
    loginlink=(By.LINK_TEXT,"Log in")
    
    def clickRegister(self):
        self.driver.find_element(*self.registerlink).click()
        return self.driver.title
        
    def __init__(self,driver):
        self.driver=driver