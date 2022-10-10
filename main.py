import requests
from bs4 import BeautifulSoup
from time import sleep
import time
from user_prompt import *

Time  = float(input("Enter time : "))
x = 0
sleep(Time)
print("Extracting {} internships".format(stored_text))
start = time.time()
for i in range(len(str_list)):
    url = 'https://internshala.com/internships/'+user_text+'-internship/page-'+str_list[i]+'/'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml') 
    Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
    for Intern in Interns:
        Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
        Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
        Location = Intern.find('div',id='location_names').text.strip()
        Start_date = Intern.find('div',id='start-date-first').text.strip()
        Stipend = Intern.find('span',class_='stipend').text
        Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
        Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
        Hiring = Intern.find('div',class_='actively_hiring_badge')
        Covid_info = Intern.find('div',class_='covid_wfh_alert_info')
        Posted_status = Intern.find('div',class_='status status-small status-success')
        Posted_Info = Intern.find('div',class_='status status-small status-info')
        Posted_inactive = Intern.find('div',class_='status status-small status-inactive').text
        #total = Intern.find('span',id='total_pages').text
        #Total = Intern.find('div',class_='page_number heading_6')
        #over_all = Intern.find('span' , id ='pagination')
        if(Hiring == None):
            Hiring = 'Unavailable'
        else:
            Hiring = Intern.find('div',class_='actively_hiring_badge').text.lstrip().rstrip()
        if(Posted_status == None):
            Posted_status = 'Unavailable'
        else:
            Posted_status = Intern.find('div',class_='status status-small status-success').text
        if(Posted_Info == None):
            Posted_status == 'Unavailable'
        else:
            Posted_status = Intern.find('div',class_='status status-small status-info').text
        if(Posted_inactive == 'Internship'):
            Posted_status = 'This Internship is posted about more than a week/month'
        if(Covid_info == None):
            Covid_info = 'Unavailable'
        else:
            Covid_info = Intern.find('div',class_='covid_wfh_alert_info').text.lstrip().rstrip() 
        if (Duration[57:64] == '1Month' or Duration[40:47] == '1Month' or Duration[42:49] == '1Month'):
         Duration = '1 Month'
        if (Duration[57:64] == '2Months' or Duration[40:47] == '2Months' or Duration[42:49] == '2Months'):
            Duration = '2 Months'
        if (Duration[57:64] == '3Months' or Duration[40:47] == '3Months' or Duration[42:49] == '3Months'):
            Duration = '3 Months'
        if (Duration[57:64] == '4Months' or Duration[40:47] == '4Months' or Duration[42:49] == '4Months'):
            Duration = '4 Months'
        if (Duration[57:64] == '5Months' or Duration[40:47] == '5Months' or Duration[42:49] == '5Months'):
            Duration = '5 Months'
        if (Duration[57:64] == '6Months' or Duration[40:47] == '6Months' or Duration[42:49] == '6Months'):
            Duration = '6 Months'
        if(Duration[39:46] == '1Month' or Duration[35:42] == '1Month' or Duration[41:48] == '1Month'):
            Duration = '1 Month'
        if(Duration[39:46] == '2Months' or Duration[35:42] == '2Months' or Duration[41:48] == '2Months'):
            Duration = '2 Months'
        if(Duration[39:46] == '3Months' or Duration[35:42] == '3Months' or Duration[41:48] == '3Months'):
            Duration = '3 Months'
        if(Duration[39:46] == '4Months' or Duration[35:42] == '4Months' or Duration[41:48] == '4Months'):
            Duration = '4 Months'
        if(Duration[39:46] == '5Months' or Duration[35:42] == '5Months' or Duration[41:48] == '5Months'):
            Duration = '5 Months'
        if(Duration[39:46] == '6Months' or Duration[35:42] == '6Months' or Duration[41:48] == '6Months'):
            Duration = '6 Months'
        if(Duration[57:63] == '1Week' or Duration[42:48] == '1Week' or Duration[39:45] == '1Week'):
            Duration = '1 Week'
        if(Duration[57:63] == '2Weeks' or Duration[42:48] == '2Weeks' or Duration[39:45] == '2Weeks'):
            Duration = '2 Weeks'
        if(Duration[57:63] == '3Weeks' or Duration[42:48] == '3Weeks' or Duration[39:45] == '3Weeks'):
            Duration = '3 Weeks'
        if(Duration[57:63] == '4Weeks' or Duration[42:48] == '4Weeks' or Duration[39:45] == '4Weeks'):
            Duration = '4 Weeks'
        if(Duration[57:63] == '5Weeks' or Duration[42:48] == '5Weeks' or Duration[39:45] == '5Weeks'):
            Duration = '5 Weeks'
        if(Duration[57:63] == '6Weeks' or Duration[35:41] == '6Weeks' or Duration[39:45] == '6Weeks'):
            Duration = '6 Weeks'
        if(Start_date[18:29] == 'Immediately'):
            Start_date = 'Immediately'
        if(len(Stipend) == 12):
            Stipend = ' Not provided'
        if(Stipend == 'Unpaid'):
            Stipend = ' Unpaid'
        if(Duration[41:52] == 'NotProvided' or Duration[39:50] == 'NotProvided'):
            Duration = 'Not Provided'

        print()
        print("Company: {}".format(Company_name))
        sleep(Time)
        print("Role: {}".format(Role))
        sleep(Time)
        print("Location: {}".format(Location))
        sleep(Time)
        print("Start Date: {}".format(Start_date))
        sleep(Time)
        print("Stipend:{}".format(Stipend))
        sleep(Time)
        print("Internship/Job: {}".format(Type))
        sleep(Time)
        print("Duration: {}".format(Duration))
        sleep(Time)
        print("Hiring Info : {}".format(Hiring))
        sleep(Time)
        print("Covid WFH Alert Info : {}".format(Covid_info))
        sleep(Time)
        print("Posted on : {}".format(Posted_status))
        x = x+1    
end = time.time()
print()
#print("Total companies {}".format(Total))
#print(over_all)
print("No.of Companies scraped : {}".format(x))
elapsed_time = end - start
minutes = elapsed_time/60
print("Elapsed time(seconds) : {} seconds".format(elapsed_time))
print("Elapsed time(Minutes) : {} minutes".format(minutes))