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
    
    #Test Case 41   
    def test_FPQBS_41(self): 
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in 
        time.sleep(1)
        driver.find_element(By.ID,"menu_time_viewTimeModule").click() # klik menu Time
        time.sleep(1)
        Hover = ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_ProjectInfo")).move_to_element(driver.find_element(By.ID,"menu_admin_viewCustomers"))
        time.sleep(1)       
        Hover.click().perform()
        time.sleep(2)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(1)        
        driver.find_element(By.ID,"addCustomer_customerName").send_keys("MikroTik")    # isi nama employee untuk search  
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click() # klik tombol search
   

        # validasi
        response_data = driver.find_element(By.ID,"resultTable").text
        self.assertIn('MikroTik',response_data)   

    def tearDown(self): 
        self.driver.close() 
if __name__ == "__main__": 
    unittest.main()   