from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import re
import json

url = 'http://www.otd.kr/bbs/board.php?bo_table=album&wr_id=203710'

driver = webdriver.Chrome()

driver.get(url)

#FINDING POST ID
url_current = driver.current_url
start = url_current.find("&wr_id=") + len("&wr_id=")
end = url_current.find("&page=")
post_id = url_current[start:end]

#FINDING POST TITLE
post_title = driver.find_element(By.CSS_SELECTOR, "div[style='color:#505050; font-size:13px; font-weight:bold; word-break:break-all;']").text

#FINDING AUTHOR NAME
post_author_full = driver.find_element(locate_with(By.TAG_NAME, "a").near({By.CLASS_NAME: "member"})).get_attribute("title")
author_name = post_author_full.split("]",1)[1] 
author_id = re.search(r"\[(\w+)\]", post_author_full).group(1)

#FINDING TEXT BODY
contents = driver.find_element(By.CLASS_NAME, "view-img").get_attribute("innerHTML").replace('''src="http://www.otd.kr/gn/''', '''src="''').replace('''href=\"http://www.otd.kr/gn''', '''href="''')





#OUTPUT TO JSON
output = [post_id, post_title, author_name, author_id, contents]

with open("data.json", "w") as outfile:
    json.dump(output, outfile)