from selenium import webdriver
import os


def loadNames():
    path = r"D:\SigEvoSummerSchool\ai_big_data_quantum_compution\resumes"
    resumesFiles = os.listdir(path)

    listOfNames = []
    for resume in resumesFiles:
        with open(os.path.join(path,resume), 'r', encoding="utf-8") as file:
            try:
                for line in file:
                    print(resume)
                    listOfNames.append( (line.split(None, 1)[0], resume))  # add only first word
                    print(line.split(None, 1)[0])
                    break
            except:
                print("error")
                listOfNames.append()

    return listOfNames


def getGender(names):
    webpage = r"http://www.indianhindunames.com/find-gender-from-names.htm"  # edit me

    driver = webdriver.Chrome()
    driver.get(webpage)

    values = []
    rejected = []

    for name in names:
        if len(name[0]) > 3:
            sbox = driver.find_element_by_class_name("txtfieldqs")
            sbox.clear()
            sbox.send_keys(name[0])

            driver.execute_script("javascript:Gender()")
            result = driver.find_element_by_id("result").get_attribute("value")

            if "female" in result:
                values.append(1)
            else:
                values.append(0)
        else:
            rejected.append(name[1])

    driver.quit()
    return values, rejected



def main():
    names = loadNames()


    values, rejected = getGender(names)

    with open('genders.txt', 'w') as f:
        for item in values:
            f.write("{}\n".format(str(item)))

    with open('rejected.txt', 'w') as f:
        for item in rejected:
            f.write("%s\n" % item)



    pass

    # webpage = r"http://www.indianhindunames.com/find-gender-from-names.htm" # edit me
    #
    #
    # searchterm = "Wojtek" # edit me
    #
    # driver = webdriver.Chrome()
    # driver.get(webpage)
    #
    # sbox = driver.find_element_by_class_name("txtfieldqs")
    # sbox.send_keys(searchterm)
    #
    # driver.execute_script("javascript:Gender()")
    #
    #
    # result = driver.find_element_by_id("result").get_attribute("value")
    # print(result)



if __name__ == "__main__":
    main()