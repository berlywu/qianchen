# from selenium import webdriver
# import time
#
#
# start_url = "https://reg.jd.com/reg/person?ReturnUrl=https://www.jd.com/2017?"
# phone_num = "15387093519"
#
# i = 1
# while i > 100:
#     driver = webdriver.PhantomJS()
#     driver.get(start_url)
#     driver.find_element_by_xpath("//div[@id='mobilediv']/div[@class='login_txt register_txt']/input").send_keys(phone_num)
#     driver.find_element_by_xpath("//div[@class='loginRight registerRight']/div[@class='login_txt register_txt']/input").send_keys("12345678")
#     driver.find_element_by_xpath("//div[@id='registerForm']/input[@id='register_btn']").click()
#
#     time.sleep(3)
#     i += 1
a = 'abccef'
def firstCharacterList(tstr):
    for s in tstr:
        if tstr.count(s) == 1:
            print(s)
            return s

firstCharacterList(a)
