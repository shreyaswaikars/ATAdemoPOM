import unittest
from POM_DemowebshopTests.WebdriverUtility import supplydriver
from POM_DemowebshopObjects.DemowebshopHomepage import HomePage
from POM_DemowebshopObjects.DemowebshopRegisterationpage import RegistrationPage

class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver=supplydriver("chrome")
        self.homepage=HomePage(self.driver)
        self.registrationpage=RegistrationPage(self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://demowebshop.tricentis.com/")
    
    @classmethod
    def tearDownClass(self):
        self.driver.close()
    
    def test1_RegisterPageTest(self):
        temp1=self.homepage.clickRegister()
        self.assertEqual(temp1, "Demo Web Shop. Register", "test1_RegisterPageTest failed")
    def test2_Register(self):
        temp2=self.registrationpage.register()
        self.assertEqual(temp2, self.registrationpage.emailRegister, "test2_Register failed")

    # def __init__(self,driver):
    #     self.driver=driver