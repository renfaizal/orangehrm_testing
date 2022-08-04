from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Variable
url = "https://opensource-demo.orangehrmlive.com/"
username = "Admin"
password = "admin123"

    

class Job(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    #Test Case 46   
    def test_FPQBS_46(self): 
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click() # klik tombol sign in 
        time.sleep(1)
        driver.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click() # klik menu recruitment
        time.sleep(1)
        driver.find_element(By.ID,"menu_recruitment_viewJobVacancy").click() # klik sub menu vacancies
        time.sleep(1)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(1)    
        driver.find_element(By.XPATH,"//option[contains(text(),'QA Engineer')]").click()    # select job title  
        time.sleep(1)            
        driver.find_element(By.ID,"addJobVacancy_name").send_keys("Manual Tester")    # isi nama vacancy  
        time.sleep(1)
        driver.find_element(By.ID,"addJobVacancy_hiringManager").send_keys("Aaliyah Haq")    # isi nama manager  
        time.sleep(1)        
        driver.find_element(By.ID,"addJobVacancy_noOfPositions").send_keys("2")    # isi nama manager  
        time.sleep(1)
        driver.find_element(By.ID,"btnSave").click() # klik tombol save
   

        #wait =  WebDriverWait(driver, 10);
        #el = wait.until(EC.presenceOfElementLocated(By.XPATH("")));   
        #self.assertTrue(el.getText().contains("Successfully saved"));

        #element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='successBodyEdit']')]")))
        #self.assertTrue(element.getText().contains("Successfully saved"))
        # validasi
        #response_data = driver.find_element(By.ID,"resultTable").text
        #self.assertIn('MikroTik',response_data)   

    def tearDown(self): 
        self.driver.close() 
if __name__ == "__main__": 
    unittest.main()   