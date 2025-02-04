from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import re

def data_clean(data):
    data = re.sub('&amp;','&',str(data))
    data = re.sub('&quot;',"'",str(data))
    data = re.sub('&nbsp;','',str(data))
    data = re.sub('&#39;;',"';",str(data))
    data = re.sub('&#39;',"';",str(data))
    data = re.sub('&#xD;&#xA;',' ',str(data))
    data = re.sub('#x27;',"'",str(data))
    data = re.sub('&#xD;&#xA;'," ",str(data))
    data = re.sub('&#x2B;',"+",str(data))
    data = re.sub('\t'," ",str(data))
    data = re.sub('\n'," ",str(data))
    data = re.sub('\r'," ",str(data))
    return data


def single_regex(pattern, target_string):
    data = re.findall(pattern, target_string)
    return data[0] if data else ''

with open("input_property_number.txt", "r") as file:
    data_list = [line.strip() for line in file]

output_data = "Input ID\tLocation\tAcres\tOwner\tLand_use\tParticular\tAppraised\tAssessed\n"
with open ("Output.txt",'w') as OP:
    OP.write(output_data)
    
data_list = ["00970"]
for input_id in data_list:

    driver = webdriver.Chrome()

    main_url = "https://realestate.co.logan.oh.us/Search/Number"
    driver.get(main_url)
    time.sleep(5)

    property_number_click = driver.find_element(By.XPATH,'//*[@id="Number"]').click()
    time.sleep(2)
    property_number_clear = driver.find_element(By.XPATH,'//*[@id="Number"]').clear()
    time.sleep(2)
    property_number_pass = driver.find_element(By.XPATH,'//*[@id="Number"]').send_keys(input_id)
    time.sleep(1)
    click_search = driver.find_element(By.XPATH,'//*[@id="SearchForm"]/div[2]/button[1]').click()
    time.sleep(5)

    content = driver.page_source
    with open ("Result_Page.html",'w',encoding = 'utf-8') as RP:
        RP.write(content)

    content = data_clean(content)
    
    location = single_regex(r'Location\s*<[^>]*?>\s*<[^>]*?>\s*<[^>]*?>([^>]*?)<',str(content))
    location = data_clean(location)
    acres = single_regex(r'Acres\s*[^>]*?>\s*[^>]*?>([^>]*?)<',str(content))
    owner = single_regex(r'label\">Owner\s*[^>]*?>\s*[^>]*?>([^>]*?)<\/div>',str(content))
    land_use = single_regex(r'row card-deck\">\s*<div[^>]*?mt\-3\">\s*[^>]*?>Values[\w\W]*?Land Use\s*[^>]*?>\s*[^>]*?>([^>]*?)<',str(content))

    values_block = single_regex(r'row card-deck\">\s*<div[^>]*?mt\-3\">\s*[^>]*?>Values[\w\W]*?Land Use\s*[^>]*?>\s*[^>]*?>[^>]*?<[\w\W]*?table([\w\W]*?)<\/table',str(content))
    values_block = re.sub(r'<span[^>]*?>',' ',str(values_block))
    values_block = re.sub(r'<\/span>',' ',str(values_block))

    values_data = re.findall(r'<tr>\s*<td\s*class\=\"font[^>]*?>([^>]*?)<\/td>\s*<td[^>]*?>([^>]*?)<\/td>\s*<td[^>]*?>([^>]*?)<\/td>',str(values_block))

    for value in values_data:
        value = list(value)
        particular = value[0]
        appraised = value[1]
        assessed = value[2]
        
        output_data = str(input_id) + '\t' + str(location) + '\t' + str(acres) + '\t' + str(owner) + '\t' + str(land_use) + '\t' + str(particular) + '\t' + str(appraised) + '\t' + str(assessed) + '\n'
        with open("OutPut.txt", 'a') as OP:
            OP.write(output_data)
    print("completed ID: ",str(input_id))
    driver.quit()
print("Completed")    
        















