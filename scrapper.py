
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import os

link = 'https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
page = requests.get(link)

soup = bs(page.content, 'html.parser')
#it gives us the visual representation of data
print(soup.prettify())

# name of product
name=soup.find('div',class_="_4rR01T")
print(name.text)

# get rating of a product
rating=soup.find('div',class_="_3LWZlK")
print(rating.text)

# get other details and specifications of the product
specification=soup.find('div',class_ = "fMghEO")
for each in specification:
    spec=each.find_all('li',class_ = 'rgWa7D')
    print(spec[0].text)
    print(spec[1].text)
    print(spec[2].text)
    print(spec[3].text)
    print(spec[4].text)


# get price of the product
price = soup.find('div', class_ = '_30jeq3 _1_WHN1')
print(price.text)

products = []            # List to store the name of the product
prices = []              # List to store price of the product
ratings = []             # List to store rating of the product
memory = []              # List to store memory of ram and rom
battery = []             # List to store battery
camera = []              # List to store camera resolution
processor = []           # List to store processor
display = []             # List to store display screen size


for data in soup.findAll('div', class_ = '_3pLy-c row'):
    names = data.find('div', attrs = {'class': '_4rR01T'})
    price = data.find('div', attrs = {'class': '_30jeq3 _1_WHN1'})
    rating = data.find('div', attrs = {'class': '_3LWZlK'})
    specification = data.find('div', attrs = {'class': 'fMghEO'})

    for each in specification:

        col = each.find_all('li', attrs={'class': 'rgWa7D'})
        memorytxt = col[0].text
        displaytxt = col[1].text
        cameratxt = col[2].text
        batterytxt = col[3].text
        processortxt = col[4].text

    products.append(names.text)   # Add product name to list
    prices.append(price.text)   # Add price to list
    memory.append(memorytxt)  # Add memory specifications to list
    battery.append(batterytxt)   # Add battery specifications to list
    processor.append(processortxt)   # Add processor specifications to list
    display.append(displaytxt)   # Add display specifications to list
    camera.append(cameratxt)   # Add camera resolution to list
    ratings.append(rating.text)   #Add rating  to list
#printing the length of list
print(len(products))
print(len(ratings))
print(len(prices))
print(len(memory))
print(len(battery))
print(len(processor))
print(len(display))
print(len(camera))

# storing the data in the structured dataframe using pandas
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.DataFrame({'Product Name':products,'Display':display, 'Camera':camera, 'Memory':memory,'Battery':battery,"Processor":processor,'Price(in Rupees)':prices,'Rating':ratings})
df['Price(in Rupees)'] = df['Price(in Rupees)'].str.replace('₹', "")
df['Price(in Rupees)'] = df['Price(in Rupees)'].str.replace(',' ,"")
df['Price(in Rupees)'] = df['Price(in Rupees)'].astype(int)
print(df.head(5))


# create a csv file in a new folder using os
if (os.path.exists(os.path.join(os.getcwd(), 'F:\\webScrapper', 'flipkart.csv'))) is False:
    os.makedirs('F:\\webScrapper', exist_ok=True)
    df.to_csv('F:\\webScrapper\\flipkart.csv', encoding='utf_8')


