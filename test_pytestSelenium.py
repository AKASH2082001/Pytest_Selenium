from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture()
def setUp():
    global driver,Product_search
    Product_search = input("enter the product to be search: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_SearchProduct(setUp):
    driver.get("https://www.google.com/")
    driver.find_element_by_name("q").send_keys("Filpkart")
    driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
    driver.find_element_by_class_name("LC20lb.MBeuO.DKV0Md").click()
    driver.find_element_by_class_name("_2IX_2-.VJZDxU").send_keys("9962873499")
    driver.find_element_by_class_name("_2IX_2-._3mctLh.VJZDxU").send_keys("@Pakash208")
    driver.find_element_by_class_name("_2KpZ6l._2HKlqd._3AWRsL").click()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys(Product_search)
    driver.find_element_by_class_name("_34RNph").click()
    time.sleep(5)




