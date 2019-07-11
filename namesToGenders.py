from selenium import webdriver


def main():
    webpage = r"http://www.indianhindunames.com/find-gender-from-names.htm" # edit me


    searchterm = "Wojtek" # edit me

    driver = webdriver.Chrome()
    driver.get(webpage)

    sbox = driver.find_element_by_class_name("txtfieldqs")
    sbox.send_keys(searchterm)

    driver.execute_script("javascript:Gender()")


    result = driver.find_element_by_id("result").get_attribute("value")
    print(result)

    searchterm = "Anna"  # edit me

    sbox = driver.find_element_by_class_name("txtfieldqs")
    sbox.send_keys(searchterm)

    driver.execute_script("javascript:Gender()")

    result = driver.find_element_by_id("result").get_attribute("value")
    print(result)


if __name__ == "__main__":
    main()