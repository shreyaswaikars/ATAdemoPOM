import unittest
from POM_DemowebshopTests.AllTestMethods import Test
DemoWebShopTestSuite = unittest.TestSuite()

DemoWebShopTestSuite.addTest(Test('test1_RegisterPageTest'))
DemoWebShopTestSuite.addTest(Test('test2_Register'))

# s=unittest.TestRunner()
s=unittest.TestRunner.run(DemoWebShopTestSuite)
# s.run(DemoWebShopTestSuite)