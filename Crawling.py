from selenium import webdriver  
import time
from selenium.webdriver.common.by import By
import os

driver = webdriver.Edge()
driver.get("https://bbs.byr.cn/")

username = driver.find_element(By.NAME,"id")  
password = driver.find_element(By.NAME,"passwd")
username.send_keys("xjw985")  
password.send_keys("Xjwxxzj985")

driver.find_element(By.XPATH,"/html/body/section/div[1]/form/input[3]").click() 

time.sleep(2)
driver.find_element(By.XPATH,"/html/body/aside/nav/ul/li[1]/ul/li[4]/span/a").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/section/section/div[2]/table/tbody/tr[16]/td[1]/a").click()

# 获取所有帖子的标题和发布时间
# First page
os.path.exists("/posts") or os.makedirs("/posts")

for i in range(6,31):
   # 存储帖子信息到文件
   with open("/posts/posts1.txt", "w", encoding="utf-8") as f:
    title = driver.find_element(By.XPATH,"/html/body/section/section/div[3]/table/tbody/tr["+str(i)+"]/td[2]/a").text
    timestamp = driver.find_element(By.XPATH,"/html/body/section/section/div[3]/table/tbody/tr["+str(i)+"]/td[3]").text  
    f.write(f"{title} - {timestamp}\n")

# page_number = input("已经爬取23条数据,还需要爬取几页数据(30条/页): ")
# for j in range(page_number):
#    driver.find_element(By.XPATH,"/html/body/section/section/div[4]/div[1]/ul/li[2]/ol/li["+(j+2)+"]/a").click()
#    with open("/posts/posts"+(j+2)+".txt", "w", encoding="utf-8") as f_loop:
#       for k in range(30):  
#         title = driver.find_element(By.XPATH,"/html/body/section/section/div[3]/table/tbody/tr["+(i+1)+"]/td[2]/a").text
#         timestamp = driver.find_element(By.XPATH,"/html/body/section/section/div[3]/table/tbody/tr["+(i+1)+"]/td[3]").text  
#         f_loop.write(f"{title} - {timestamp}\n")
   
display = input("Do you want to quit?(y/n)")
if display=="y":
  driver.quit()

