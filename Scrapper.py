# Lets import all the libraries
import pandas as pd
from selenium import webdriver
chrome_path = r"D:\Projects\Zomato\ChromeDriver\chromedriver.exe"


# Url for each neighborhood
url = "https://www.zomato.com/bangalore/frazer-town-restaurants"
# neighborhood
city = "frazer_town_"


wd = webdriver.Chrome(chrome_path)
wd.get(url)

rest_types = wd.find_element_by_xpath('//div[@class="ui vertical pointing menu subzone_category_container"]')
rest_types = rest_types.text.split("\n")
print(rest_types)
wd.quit()

# This function returns all the buttons for navigating each category


def rest_types_buttons():
    buttons = wd.find_elements_by_xpath('//span[@class="zred"]')
    return buttons

# This function returns the link, name and address of restaurant for each page


def name_link_add():
    rest_link = []
    rest_name = []
    restaurants = wd.find_elements_by_xpath('//a[@class="result-title hover_feedback zred bold ln24   fontsize0 "]')
    for name in restaurants:
        rest_link.append(name.get_attribute('href'))
        rest_name.append(name.text)
    restaurants_address = wd.find_elements_by_xpath('//div[@class="col-m-16 search-result-address grey-text nowrap ln22"]')
    rest_address = []
    for rest_add in restaurants_address:
        rest_address.append(rest_add.text)
    return rest_link, rest_name, rest_address

# this function returns the all the data from an individual category (all pages combined)


def get_data_rest_type(rest_type):
    try:
        prev_link, prev_name, prev_add = None, None, None
        rest_link, rest_name, rest_address = name_link_add()
        link = []
        name = []
        address = []
        while prev_link != rest_link:
            prev_link, prev_name, prev_add = rest_link, rest_name, rest_address
            link = link + prev_link
            name = name + prev_name
            address = address + prev_add
            next_page_button = wd.find_element_by_xpath('//i[@class="right angle icon"]')
            next_page_button.click()
            wd.switch_to.window(wd.window_handles[0])
            rest_link, rest_name, rest_address = name_link_add()
            # Below two if conditions are for debugging
            if not (len(rest_address) == len(rest_link) == len(rest_name)):
                print("need to see, name link address mismatch")
                break
            if len(rest_name) == 0:
                print("Empty found")
    except:
        print("unknown error")
    return link, name, address


# For each of the category
type_ = ("_".join(rest_types[0].lower().split(' ')))
print(type_)

# Go inside the category by clicking on the button on the main page
wd = webdriver.Chrome(chrome_path)
wd.get(url)
wd.switch_to.window(wd.window_handles[0])
buttons = rest_types_buttons()
buttons[0].click()
wd.switch_to.window(wd.window_handles[0])

# Collect the data
data_rest_type = get_data_rest_type(type)


# Form a dataframe
add = pd.DataFrame({'link': data_rest_type[0], 'name': data_rest_type[1], 'address': data_rest_type[2]})

# save the file in csv format
filename = city + type_ + "_.csv"
add.to_csv(filename, index=False, columns=['link', 'address', 'name'])


# Lets verify our file name
filename

# 1st Category
type_ = ("_".join(rest_types[1].lower().split(' ')))
print(type_)

wd = webdriver.Chrome(chrome_path)
wd.get(url)
wd.switch_to.window(wd.window_handles[0])
buttons = rest_types_buttons()
buttons[1].click()
wd.switch_to.window(wd.window_handles[0])

data_rest_type = get_data_rest_type(type_)

add = pd.DataFrame({'link' : data_rest_type[0], 'name' : data_rest_type[1], 'address' : data_rest_type[2]} )

filename = city + type_ + "_.csv"
add.to_csv(filename, index=False, columns = ['link', 'address', 'name'])

filename

# 2nd Category
type_ = ("_".join(rest_types[2].lower().split(' ')))
print(type_)

wd = webdriver.Chrome(chrome_path)
wd.get(url)
wd.switch_to.window(wd.window_handles[0])
buttons = rest_types_buttons()
buttons[1].click()
wd.switch_to.window(wd.window_handles[0])

data_rest_type = get_data_rest_type(type_)

add = pd.DataFrame({'link': data_rest_type[0], 'name': data_rest_type[1], 'address': data_rest_type[2]})

filename = city + type_ + "_.csv"
add.to_csv(filename, index=False, columns=['link', 'address', 'name'])

filename

# 3rd Category
type_ = ("_".join(rest_types[3].lower().split(' ')))
print(type_)

wd = webdriver.Chrome(chrome_path)
wd.get(url)
wd.switch_to.window(wd.window_handles[0])
buttons = rest_types_buttons()
buttons[1].click()
wd.switch_to.window(wd.window_handles[0])

data_rest_type = get_data_rest_type(type_)

add = pd.DataFrame({'link': data_rest_type[0], 'name': data_rest_type[1], 'address': data_rest_type[2]})

filename = city + type_ + "_.csv"
add.to_csv(filename, index=False, columns=['link', 'address', 'name'])

filename

# 4th Category
type_ = ("_".join(rest_types[4].lower().split(' ')))
print(type_)

wd = webdriver.Chrome(chrome_path)
wd.get(url)
wd.switch_to.window(wd.window_handles[0])
buttons = rest_types_buttons()
buttons[1].click()
wd.switch_to.window(wd.window_handles[0])

data_rest_type = get_data_rest_type(type_)

add = pd.DataFrame({'link': data_rest_type[0], 'name': data_rest_type[1], 'address': data_rest_type[2]} )

filename = city + type_ + "_.csv"
add.to_csv(filename, index=False, columns=['link', 'address', 'name'])

filename

# 5th Category
type_ = ("_".join(rest_types[5].lower().split(' ')))
print(type_)

wd = webdriver.Chrome(chrome_path)
wd.get(url)
wd.switch_to.window(wd.window_handles[0])
buttons = rest_types_buttons()
buttons[1].click()
wd.switch_to.window(wd.window_handles[0])

data_rest_type = get_data_rest_type(type_)

add = pd.DataFrame({'link': data_rest_type[0], 'name': data_rest_type[1], 'address': data_rest_type[2]} )

filename = city + type_ + "_.csv"
add.to_csv(filename, index=False, columns=['link', 'address', 'name'])

filename

# 6th Category
type_ = ("_".join(rest_types[6].lower().split(' ')))
print(type_)

wd = webdriver.Chrome(chrome_path)
wd.get(url)
wd.switch_to.window(wd.window_handles[0])
buttons = rest_types_buttons()
buttons[1].click()
wd.switch_to.window(wd.window_handles[0])

data_rest_type = get_data_rest_type(type_)

add = pd.DataFrame({'link': data_rest_type[0], 'name': data_rest_type[1], 'address': data_rest_type[2]})

filename = city + type_ + "_.csv"
add.to_csv(filename, index=False, columns=['link', 'address', 'name'])

filename

