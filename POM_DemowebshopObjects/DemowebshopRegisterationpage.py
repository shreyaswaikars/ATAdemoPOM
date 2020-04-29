from selenium.webdriver.common.by import By

class RegistrationPage():
    genderMaleRadioButton=(By.ID,"gender-male")
    genderFemaleRadioButton=(By.ID,"gender-female")
    firstnameInputbox=(By.ID,"FirstName")
    lastnameInputbox=(By.ID,"LastName")
    emailInputbox=(By.ID,"Email")
    passwordInputbox=(By.ID,"Password")
    confirmpasswordInputbox=(By.ID,"ConfirmPassword")
    registerButton=(By.ID,"register-button")
    continueButton=(By.CSS_SELECTOR,"input[value='Continue']")
    userLink=(By.CLASS_NAME,"account")
    emailRegister="atademo3@ataps.com"
    
    def register(self):      
        self.driver.find_element(*self.genderMaleRadioButton).click()
        self.driver.find_element(*self.firstnameInputbox).send_keys("ATA")
        self.driver.find_element(*self.lastnameInputbox).send_keys("demo3")
        self.driver.find_element(*self.emailInputbox).send_keys(*self.emailRegister)
        self.driver.find_element(*self.passwordInputbox).send_keys("password")
        self.driver.find_element(*self.confirmpasswordInputbox).send_keys("password")
        self.driver.find_element(*self.registerButton).click()
        self.driver.implicitly_wait(6)
        self.driver.find_element(*self.continueButton).click()
        userLoginLink=self.driver.find_element(*self.userLink).text
        return userLoginLink
    
    def __init__(self,driver):
        self.driver=driver