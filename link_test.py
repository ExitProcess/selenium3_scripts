# прототип линк-чекера -- скрипта, который ищет ссылки на сайте (в данном случае -- python.org) и переходит по ним

from selenium import webdriver

driver = webdriver.Chrome('C:\SeleniumDrivers\Chrome\chromedriver.exe')

url_base = ["https://python.org/", ]  # список для ссылок
url_base_result = [0, ]  # список для результатов (0, 1, 2 или 3, подробности в описании алгоритма)
index = 0

while 0 in url_base_result:  # выполнять, пока есть ссылки, по которым не было перехода

    driver.get(url_base[index])

    urls_list_from_page = []  # временный список для всех ссылок с текущей страницы (url_base[index])

    elements_list_from_page = driver.find_elements_by_tag_name("a")  # список для элементов с тегом "а"
    for elem in elements_list_from_page:
        try:  # если не получится получить аттрибут, то просто перейти к следующему элементу
            url = elem.get_attribute('href')
        except Exception:
            pass

        # фильтрация ссылок: не проверяются внешние сайты, подсайты -- docs.python.org и прочие
        # игнорируются ссылки внутри страницы (https://www.python.org/about/success/#software-development)
        # игнорируются ссылки на скачивание файлов:
        if "www.python.org" in str(url) and "#" not in str(url):
            if "download" not in str(url) and "ftp" not in str(url):
                urls_list_from_page.append(url)

    unique_urls_list_from_page = list(set(urls_list_from_page))  # временный список для уникальных ссылок

    for unique_url in unique_urls_list_from_page:  # наполнение базы
        if unique_url not in url_base:
            url_base.append(unique_url)  # добавить в базу уникальную ссылку
            url_base_result.append(0)  # по уникальной ссылке не было перехода, значит статус 0

    print(len(url_base))
    print(len(url_base_result))

    print(url_base)
    print(url_base_result)

    url_base_result[index] = 1  # пока заглушка, потом будут проверки для выставления точного статуса
    index += 1

driver.close()
driver.quit()
