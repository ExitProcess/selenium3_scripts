# парсилка SOCKS5
# источник http://spys.one/
# выбирает только сервера со 100% аптаймом
# сравнение скорости работы xpath и сss (перебор по одному элементу)
# алгоритм тот же, что и в socks_5_proxy.py -- используется find_element_by, а не find_elements_by
# сравнение find_elements_by_xpath и find_elements_by_css_selector будет потом

import time
from selenium import webdriver
from selenium.webdriver.support import select

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)

css = time.time()

driver.get("http://spys.one/proxies/")

sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

css_loop = time.time()

spy1x = ':nth-of-type('
percent_pos = ') [colspan="1"]:nth-of-type(8)'
ip_port_pos = ') [colspan="1"]:nth-of-type(1)'
country_pos = ') [colspan="2"]'
count_css = 0

for i in range(4, 502):
    percent = driver.find_element_by_css_selector(spy1x + str(i) + percent_pos)
    if "100" in percent.text:
        ip_port = driver.find_element_by_css_selector(spy1x + str(i) + ip_port_pos)
        country = driver.find_element_by_css_selector(spy1x + str(i) + country_pos)
        ip_port = ip_port.text
        index = ip_port.find(' ')
        print(ip_port[index + 1:], country.text, percent.text)
        count_css += 1

css_loop = time.time() - css_loop
css = time.time() - css

print("#"*60)

xpath = time.time()

driver.get("http://spys.one/proxies/")

sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

xpath_loop = time.time()

xpath_start = "//tr["
percent_pos = "]/td[8]"
ip_port_pos = "] / td[1]"
country_pos = "] / td[5]"
count_xpath = 0

for i in range(4, 502):
    percent = driver.find_element_by_xpath(xpath_start + str(i) + percent_pos)
    if "100" in percent.text:
        ip_port = driver.find_element_by_xpath(xpath_start + str(i) + ip_port_pos)
        country = driver.find_element_by_xpath(xpath_start + str(i) + country_pos)
        ip_port = ip_port.text
        index = ip_port.rfind(" ")
        print(ip_port[index + 1:], country.text, percent.text)
        count_xpath += 1

xpath_loop = time.time() - xpath_loop
xpath = time.time() - xpath

print("#"*60)

print("найдено серверов перебором CSS: %s" % count_css)
print("найдено серверов перебором XPATH: %s" % count_xpath)

print("CSS: поиск элементов, анализ и вывод -- %s sec" % css_loop)
print("CSS: время выполнения -- %s sec" % css)

print("XPATH: поиск элементов, анализ и вывод -- %s sec" % xpath_loop)
print("XPATH: время выполнения -- %s sec" % xpath)

if css_loop < xpath_loop:
    print("перебор элементов по CSS быстрее XPATH на %s sec" % (xpath_loop - css_loop))
else:
    print("перебор элементов по XPATH быстрее CSS на %s sec" % (css_loop - xpath_loop))

driver.close()
driver.quit()

# найдено серверов перебором CSS: 64
# найдено серверов перебором XPATH: 64
# CSS анализ и вывод -- 22.93831181526184 sec
# CSS общее время -- 37.411139488220215 sec
# XPATH анализ и вывод -- 28.539632320404053 sec
# XPATH общее время -- 41.58837890625 sec
# перебор элементов по CSS быстрее XPATH на 5.601320505142212 sec
# ...
# перебор элементов по CSS быстрее XPATH на 4.117235422134399 sec
# ...
# перебор элементов по CSS быстрее XPATH на 4.981284856796265 sec
