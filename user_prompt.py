import numpy as np

int_list = np.arange(1,250)
str_list = []
for i in (int_list):
    str_list.append(str(i))

user_text = str(input('Enter a tech stack to extract : '))
stored_text = user_text

# tech stack interns
if(user_text == 'information technology' or user_text == 'Information technology'):
    user_text = 'information-technology'
    str_list = ['1' , '2']
if(user_text == 'computer vision' or user_text == 'Computer vision'):
    user_text = 'computer-vision'
    str_list = ['1']
if(user_text == 'machine learning' or user_text == 'Machine learning' or user_text == 'Ml' or user_text == 'ML' or user_text == 'ml'):
    user_text = 'machine-learning'
    str_list = ['1']
if(user_text == 'data science' or user_text == 'Data science'):
    user_text = 'data-science'
    str_list = ['1' , '2' , '3']
if(user_text == 'artificial intelligence' or user_text == 'Artificial intelligence' or user_text == 'AI' or user_text == 'ai'):
    user_text = 'artificial-intelligence-(ai)'
    str_list = ['1' , '2']
if(user_text == 'android app development' or user_text == 'Android app development' or user_text == 'android' or user_text == 'Android'):
    user_text = 'android-app-development'
    str_list = ['1' , '2' , '3' , '4' , '5' , '6' , '7']
if(user_text == 'ios app development' or user_text == 'ios app' or user_text == 'Ios app'):
    user_text == 'ios-app-development'
    str_list = ['1' , '2' , '3']
if(user_text == 'web development' or user_text == 'Web development'):
    user_text == 'web-development'
    int_list = np.arange(1,26)
    str_list = []
    for i in (int_list):
        str_list.append(str(i))
    #str_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
if(user_text == 'full stack developemnt' or user_text == 'Full stack development' or user_text == 'Full stack developer' or user_text == 'full stack developer'):
    user_text = 'full-stack-development'
    str_list = ['1' , '2' , '3']
if(user_text == 'front end development' or user_text == 'Front end development' or user_text == 'front end developer' or user_text == 'Front end developer' or user_text == 'front end' or user_text == 'Front end' or user_text == 'frontend' or user_text == 'Frontend'):
    user_text = 'front-end-development'
    str_list = ['1' , '2' , '3' , '4' , '5']
if(user_text == 'backend' or user_text == 'backend development' or user_text == 'Backend development' or user_text == 'Backend'):
    user_text = 'backend-development'
    str_list = ['1' , '2' , '3' , '4' , '5' , '6']
if(user_text == 'flutter' or user_text == 'flutter development' or user_text == 'Flutter development' or user_text == 'Flutter'):
    user_text = 'flutter-development'
    str_list = ['1' , '2' , '3' , '4']
if(user_text == 'angular js' or user_text == 'Angular js' or user_text == 'angular.js'):
    user_text = 'angular.js-development'
    str_list = ['1']
if(user_text == 'php' or user_text == 'php development' or user_text == 'Php development' or user_text == 'PHP' or user_text== 'Php'):
    user_text = 'php-development'
    str_list = ['1' , '2']
if(user_text == 'node js' or user_text == 'Node js' or user_text == 'nodejs' or user_text == 'Nodejs'):
    user_text = 'node.js-development'
    str_list = ['1' , '2']
if(user_text == 'mobile app development' or user_text == 'Mobile app development'):
    user_text = 'mobile-app-development'
    str_list = ['1' , '2' , '3' , '4' , '5' , '6' , '7']
if(user_text == 'blockchain' or user_text == 'Blockchain'):
    user_text = 'blockchain-development'
    str_list = ['1']
if(user_text == 'game development' or user_text == 'Game development'):
    user_text = 'game-development'
    str_list = ['1']
if(user_text == 'javascript' or user_text == 'Javascript'):
    user_text = 'javascript-development'
    str_list = ['1' , '2']
if(user_text == 'wordpress' or user_text == 'Wordpress'):
    user_text = 'wordpress-development'
    str_list = ['1' , '2']
if(user_text == 'python' or user_text == 'django' or user_text == 'Python' or user_text == 'Django'):
    user_text = 'python%2Fdjango'
    str_list = ['1' , '2' , '3']
if(user_text == 'java' or user_text == 'Java'):
    str_list = ['1' , '2']
if(user_text == 'software development' or user_text == 'Software development' or user_text == 'Software developer' or user_text == 'software developer'):
    user_text = 'software-development'
    str_list = ['1' , '2' , '3' , '4' , '5' , '6' , '7']
if(user_text == 'cybersecurity' or user_text == 'Cybersecurity' or user_text == 'Cyber security' or user_text == 'cyber security' or user_text == 'Cyber Security'):
    user_text == 'cyber-security'
    str_list = ['1']
if(user_text == 'ui and ux' or user_text == 'ui/ux' or user_text == 'UI/UX' or user_text == 'Ui/ux'):
    user_text = 'ui%2Fux'
    str_list = ['1' , '2' , '3' , '4']

# Engineering Interns
if(user_text == 'engineering' or user_text == 'Engineering'):
    #str_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37']
    int_list = np.arange(1,38)
    str_list = []
    for i in (int_list):
        str_list.append(str(i))
if(user_text == 'aerospace' or user_text == 'Aerospace'):
    user_text = 'aerospace'
    str_list = ['1']
if(user_text == 'mechanical' or user_text == 'Mechanical' or user_text == 'Mechanical Engineering' or user_text == 'Mechanical engineering'):
    user_text = 'mechanical'
    str_list = ['1' , '2' , '3']
if(user_text == 'civil' or user_text == 'Civil' or user_text == 'Civil engineering' or user_text == 'Civil Engineering'):
    user_text = 'civil'
    str_list = ['1']
if(user_text == 'cs' or user_text == 'CS' or user_text == 'Computer Science' or user_text == 'Computer science'):
    user_text = 'computer-science'
    #str_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32']
    int_list = np.arange(1,33)
    str_list = []
    for i in (int_list):
        str_list.append(str(i))
if(user_text == 'Electronics' or user_text == 'electronics' or user_text == 'ec' or user_text == 'EC'):
    user_text = 'electronics'
    str_list = ['1' , '2' , '3' , '4']
if(user_text == 'Electrical' or user_text == 'electrical' or user_text == 'EEE' or user_text == 'eee'):
    user_text = 'electrical'
    str_list = ['1']
if(user_text == 'network engineering' or user_text == 'Network engineering' or user_text == 'Network Engineering'):
    user_text = 'network-engineering'
    str_list = ['1']

# Design
if(user_text == 'graphic design' or user_text == 'Graphic design'):
    user_text == 'design'
    int_list = np.arange(1,28)
    str_list = []
    for i in (int_list):
        str_list.append(str(i))

# SEO
if(user_text == 'seo' or user_text == 'Seo' or user_text == 'SEO' or user_text == 'search engine optimization' or user_text == 'Search engine optimization' or user_text == 'Search Engine Optimization'):
    user_text = 'search-engine-optimization-(seo)'
    str_list = ['1' , '2' , '3' , '4' , '5' , '6' , '7']

# Teaching
if(user_text == 'teaching' or user_text == 'Teaching'):
    str_list = ['1' , '2' , '3' , '4' , '5' , '6']

# Motion Graphics
if(user_text == 'motion graphics' or user_text == 'Motion graphics' or user_text == 'Motion Graphics'):
    user_text = 'motion-graphics'
    str_list = ['1']

# Embedded Systems
if(user_text == 'Embedded systems' or user_text == 'Embedded Systems' or user_text == 'embedded systems'):
    user_text = 'embedded-systems'
    str_list = ['1' , '2']

# Video Making/Editing
if(user_text == 'Video making' or user_text == 'video making' or user_text == 'Video Making' or user_text == 'video editing' or user_text == 'Video Editing' or user_text == 'Video editing'):
    user_text = 'video-making%2Fediting'
    str_list = ['1','2','3','4','5','6','7','8','9','10','11','12']

# Audio Making/Editing ( not working try again )
if(user_text == 'Audio Making' or user_text == 'Audio making' or user_text == 'audio making' or user_text == 'Audio editing' or user_text == 'Audio Editing' or user_text == 'audio editing'):
    user_text == 'audio-making%2Fediting'
    str_list = ['1']

# Event Management
if(user_text == 'event management' or user_text == 'Event Management' or user_text == 'Event management'):
    user_text = 'event-management'
    str_list = ['1' , '2' , '3']

# Photography
if(user_text == 'photography' or user_text == 'Photography' or user_text == 'photo' or user_text == 'Photo'):
    str_list = ['1' , '2' , '3' , '4']

# Marketing
if(user_text == 'big data' or user_text == 'Big data' or user_text == 'Big Data'):
    user_text = 'big-data'
    str_list = ['1']

# Film Making
if(user_text == 'film making' or user_text == 'Film making' or user_text == 'Film Making'):
    user_text == 'film-making'
    str_list = ['1']

# Finance
if(user_text == 'Finance' or user_text == 'finance'):
    str_list = ['1' , '2' , '3' , '4' , '5' , '6' , '7']

# Fundrasing 
if(user_text == 'fundraising' or user_text == 'Fundraising'):
    str_list = ['1' , '2']

# Law
if(user_text == 'law' or user_text == 'Law'):
    str_list = ['1' , '2' , '3']

if(user_text == 'anchoring' or user_text == 'Anchoring'):
    str_list = ['1']

# MBA
if(user_text == 'mba' or user_text == 'Mba' or user_text == 'MBA'):
    user_text = 'mba'
    int_list = np.arange(1,129)
    str_list = []
    for i in (int_list):
        str_list.append(str(i))
