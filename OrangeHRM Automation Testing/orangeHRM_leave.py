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
    
    #Test Case 36   
    def test_FPQBS_36(self): 
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in 
        time.sleep(1)
        driver.find_element(By.ID,"menu_leave_viewLeaveModule").click() # klik menu Leave
        time.sleep(1)
        Hover = ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_leave_Entitlements")).move_to_element(driver.find_element(By.ID,"menu_leave_addLeaveEntitlement"))
        time.sleep(1)       
        Hover.click().perform()
        time.sleep(2)        
        driver.find_element(By.ID,"entitlements_employee_empName").send_keys("Aaliyah Haq")   # isi nama employee untuk search  
        time.sleep(1)
        driver.find_element(By.XPATH,"//option[contains(text(),'US - Vacation')]").click()    # select leave type  
        time.sleep(1)
        driver.find_element(By.XPATH,"//option[contains(text(),'2023-01-01 - 2023-12-31')]").click()   # select leave period 
        time.sleep(1)
        driver.find_element(By.ID,"entitlements_entitlement").send_keys("14")    # isi nama employee untuk search  
        time.sleep(1)        
        driver.find_element(By.ID,"btnSave").click() # klik tombol search
        time.sleep(1)  
   

        # validasi
        response_data = driver.find_element(By.XPATH,"//table[@id='resultTable']").text
        self.assertIn('Added',response_data)   

    def tearDown(self): 
        self.driver.close() 
if __name__ == "__main__": 
    unittest.main()   