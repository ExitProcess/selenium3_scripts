# парсилка SOCKS5 для телеграма
# источник http://spys.one/
# выбирает только сервера со 100% аптаймом

import time
from selenium import webdriver
from selenium.webdriver.support import select

all_time = time.time()

path = 'C:\SeleniumDrivers\Chrome\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://spys.one/proxies/")

# вначале отсортируем по SOCKS5, а только потом отобразим все
sort_socks5 = driver.find_element_by_id("xf5")
sort_socks5.click()
select.Select(sort_socks5).select_by_value("2")

# отобразим на странице 500 элементов
sort_all = driver.find_element_by_id("xpp")
sort_all.click()
select.Select(sort_all).select_by_value("5")

analize_print_time = time.time()
# теперь парсим строки, выбираем сервера со 100% аптаймом
# если аптайм сервака == 100%, то выводим на печать ip:port, страну, аптайм сервака + (количество проверок)
# "//tbody/tr[4]" - "//tbody/tr[503]" -- столько всего строк
for str_count in range(4, 503):
    # локатор аптайма
    percents_xpath = "//tr[" + str(str_count) + "]/td[8]"
    percent_elem = driver.find_element_by_xpath(percents_xpath)

    if percent_elem.text[0:3] == "100":
        # локатор ip:port + получение индекса начала текста ip:port
        ip_port_xpath = "// tr[" + str(str_count) + "] / td[1]"
        ip_port_elem = driver.find_element_by_xpath(ip_port_xpath)
        ip_port_clear = ip_port_elem.text
        index = ip_port_clear.rfind(" ")

        country_xpath = "// tr[" + str(str_count) + "] / td[5]"
        country_elem = driver.find_element_by_xpath(country_xpath)

        print(ip_port_clear[index + 1:], country_elem.text, percent_elem.text)

print("Анализ и печать -- %s seconds" % (time.time() - analize_print_time))
print("Работа скрипта -- %s seconds" % (time.time() - all_time))
driver.close()
driver.quit()

# Анализ и печать -- 28.14160966873169 seconds
# Работа скрипта -- 50.41888380050659 seconds

# Анализ и печать -- 28.42762589454651 seconds
# Работа скрипта -- 47.91574025154114 seconds

# Анализ и печать -- 33.245901584625244 seconds
# Работа скрипта -- 47.558719873428345 seconds