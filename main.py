
#program to provide link to donload a particular if it available online or the book closest to that book

from selenium import webdriver
from selenium.webdriver.common.keys import Keys






book_name=input()


def capital(s):
    l=s.split(" ")
    for i in range(len(l)):
            l[i]=l[i].capitalize()
    k=" ".join(l)
    return k

book_name=capital(book_name)


driver=webdriver.Chrome(r"C:\Users\himan\Downloads\chromedriver.exe")
driver.get("https://b-ok.cc/")

search = driver.find_element_by_id("searchFieldx")
search.send_keys(book_name,Keys.RETURN)

 # auth = driver.find_element_by_xpath("//*[@id='searchResultBox']/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div[2]/a[2]")
#  atext = auth.text

book = driver.find_element_by_xpath("//*[@id='searchResultBox']/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3/a")
book.click()






