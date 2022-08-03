from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains



# Variable
url = "https://opensource-demo.orangehrmlive.com/"
username = "Admin"
password = "admin123"

    

class Job(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    #Test Case 11   
    def test_FPQBS_11(self): 
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in 
        time.sleep(1)
        driver.find_element(By.ID,"menu_pim_viewPimModule").click() # klik menu PIM
        time.sleep(1)
        driver.find_element(By.ID,"empsearch_employee_name_empName").send_keys("Sania")    # isi nama employee untuk search  
        time.sleep(1)
        driver.find_element(By.ID,"searchBtn").click() # klik tombol search
   

        # validasi
        response_data = driver.find_element(By.ID,"resultTable").text

        self.assertIn('Sania',response_data)   

    def tearDown(self): 
        self.driver.close() 
if __name__ == "__main__": 
    unittest.main()   