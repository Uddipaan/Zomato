from Zomato_API import api_info
from Zomato_Reviews import review_info
from Zomato_Scrapper import res_info

if __name__ == '__main__':

    api_list = []
    review_list = []
    res_list = []
    api_list = api_info("GENERATE AND ENTER YOUR API KEY FROM https://developers.zomato.com/api")
    review_list = review_info()
    res_list = res_info()
