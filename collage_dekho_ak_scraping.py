import requests,os,json
from bs4 import BeautifulSoup
from pprint import pp, pprint

def colloge_dekho():
    college_url = "https://www.collegedekho.com/btech-mechanical_engineering-colleges-in-india/"
    req=requests.get(college_url)
    # pprint(req.text)
    college_shop=BeautifulSoup(req.text,"html.parser")
    clg_name_req=college_shop.find("div",class_="middle-container").find_all("div",class_="box")
    clg_rateing_req=college_shop.find(class_="rating-per")
    clg_type_list=[]
    clg_name_list=[]
    clg_detail_dict={}
    for i  in clg_name_req:
        name_link=("https://www.collegedekho.com/"+i.find("a").get('href'))
        clg_name2=(i.find("a").get("title"))
        clg_name_list.append(clg_name2)
        clg_type_req=(i.find(class_="title").find(class_="info").find_all("li"))
        clg_type_req1=(clg_type_req[1].text)      
        iner_req=requests.get(name_link)        
        iner_soup=BeautifulSoup(iner_req.text,"html.parser")
        clg_2=iner_soup.find(class_="reviewData")
        clg_2=(clg_rateing_req.find('span', class_="star-ratings-sprite-rating").get('style'))[6:-3]
        clg_2=int(clg_2)
        clg_rating=(clg_2/20)
        clg_contact_req=iner_soup.find(class_="addressList").find_all("li")
        clg_faciliti_req=iner_soup.find(class_="block facilitiesBlock").find(class_="box").find_all(class_="title")
        facility=[]
        a=0
        for faciliti in clg_faciliti_req:
            facility.append(faciliti.text)
            a+=1
        b=[]
        p=0
        for k in clg_contact_req:
            if p==0:
                contact=(k.text.strip().split()[2])
            elif p==1:
                Email1=(k.text.strip().split()[2])
            elif p==2:
                clg_visiting_site=(k.text.strip()[40::])
            elif p==3:
                clg_address=(k.text.strip()[40::])            
            p+=1
        clg_detail_dict["name"]=clg_name2        
        clg_detail_dict["type"]=clg_type_req1
        clg_detail_dict["contact"]=contact
        clg_detail_dict["Email_ID"]=Email1
        clg_detail_dict["clg_visiting_site"]=clg_visiting_site
        clg_detail_dict["clg_Address"]=clg_address
        clg_detail_dict["clg_facilities"]=facility
        clg_detail_dict["Rating"]=clg_rating
        
        file=open("college_scrap_ak.json","a")
        json.dump(clg_detail_dict,file,indent=4)
        file.close()
        print("yes",a)             

        # return clg_detail_dict
(colloge_dekho())