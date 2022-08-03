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
    
    #Test Case 1   
    def test_a_addJob(self): 
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in 
        time.sleep(1)
        driver.find_element(By.ID,"menu_admin_viewAdminModule").click()
        time.sleep(1)
        Hover = ActionChains(driver).move_to_element(driver.find_element(By.ID,"menu_admin_Job")).move_to_element(driver.find_element(By.ID,"menu_admin_viewJobTitleList"))
        time.sleep(1)       
        Hover.click().perform()
        time.sleep(2)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(3)
        driver.find_element(By.ID,"jobTitle_jobTitle").send_keys("DevOps") # isi Job Title      
        time.sleep(1)
        driver.find_element(By.ID,"jobTitle_jobDescription").send_keys("") # isi Job Desc      
        time.sleep(1)
        driver.find_element(By.ID,"jobTitle_note").send_keys("") # isi Job note      
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click() # klik tombol save
   

        # validasi
        response_data = driver.find_element(By.ID,"resultTable").text

        self.assertIn('DevOps',response_data)   

    def tearDown(self): 
        self.driver.close() 
if __name__ == "__main__": 
    unittest.main()   