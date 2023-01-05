from bs4 import BeautifulSoup
import requests 

url = "https://www.google.com/maps/search/best+parking+place+in+mumbai/@19.1249468,72.9079687,13z/data=!3m1!4b1"  

response = requests.get(url)
# print(response.status_code)  
# print(response.content) 

htmlcontent = response.content 
  
soup = BeautifulSoup(htmlcontent, 'html.parser')   
print(soup.prettify())
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name) 
# print(soup.p) 
# print(soup.a) 
# print(soup.find_all('a')) 
# print(soup.find('a'))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# for image in soup.find_all('img'):
#     print(image.get('src'))
    
# product = soup.find_all('div', class_='_3pLy-c row')
# # print(product) 

# product = soup.find('div', attrs={'class':'_3pLy-c row'}) 
# print(product) 

# product = soup.area('div', attrs={'class':''}) 

# response = requests.get(url)
# htmlContent = response.content 
# # print(htmlContent) 

# soup = BeautifulSoup(htmlContent,  'html.parser')  
# print(soup.prettify)  