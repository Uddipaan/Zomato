from Zomato_API import api_info
from Zomato_Reviews import review_info
from Zomato_Scrapper import res_info

if __name__ == '__main__':

    api_list = []
    review_list = []
    res_list = []
    api_list = api_info("fe063c59eadd9c02ee6637e4104e769a")
    review_list = review_info()
    res_list = res_info()
