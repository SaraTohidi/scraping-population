from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

def southAmericaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the 14 links that we want to use south america has 14 countries
    links = linkfind[0:14]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def caribbeanPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use caribbean has 28 countries
    links = linkfind[0:28]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def centralAmericaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use scentralAmerica has 8 countries
    links = linkfind[0:8]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def northAmericaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use noeth america has 5 countries
    links = linkfind[0:5]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def southAsiaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use south asia has 9 countries
    links = linkfind[0:9]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def eastAsiaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use east asia has 8 countries
    links = linkfind[0:8]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def southEastAsiaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use south east asia has 11 countries
    links = linkfind[0:11]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def westAsiaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use west asia has 18 countries
    links = linkfind[0:18]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def centerAsiaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use centerAsia has 5 countries
    links = linkfind[0:5]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def westAfricaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use west Africa has 17 countries
    links = linkfind[0:17]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def eastAfricaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use wast Africa has 20 countries
    links = linkfind[0:20]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def northAfricaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use north Africa has 7 countries
    links = linkfind[0:7]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def middleAfricaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use middle Africa has 10 countries
    links = linkfind[0:10]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def southAfricaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use south Africa has 5 countries
    links = linkfind[0:5]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def westEuropePopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use west Europe has 9 countries
    links = linkfind[0:9]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def eastEuropePopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use east Europe has 10 countries
    links = linkfind[0:10]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def northEuropePopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use north Europe has 13 countries
    links = linkfind[0:13]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def southEuropePopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use soputh Europe has 16 countries
    links = linkfind[0:16]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def australiaNZPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use australiaNZ has 2 countries
    links = linkfind[0:2]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def melanesiaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use melanesia has 5 countries
    links = linkfind[0:5]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def polynesiaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use polynesia has 9 countries
    links = linkfind[0:9]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame

def micronesiaPopulation(url):
    #url: The website that has the table relats to population
    #linkfind: finds all the countries in the table
    html = requests.get(url).content
    #parsing HTML
    soup = BeautifulSoup(html, 'html.parser')
    #getting the link of all population
    linkfind = soup.find_all('a', {'href': re.compile("/world-population/")})
    #ge the links that we want to use micronesi has 7 countries
    links = linkfind[0:7]
    dfs =[]
    #get the region of each county into the .csv table
    for link in links:
        head_link = "https://www.worldometers.info"
        link = link.get('href')
        head_link += link
        html = requests.get(head_link).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        dfs.append(df)
    frame = pd.concat(dfs)
    return frame


if __name__ == "__main__":
    #America
    dfs_america = []
    dfs_america_regions = []
    url_northAmerica = 'https://www.worldometers.info/world-population/northern-america-population'
    html = requests.get(url_northAmerica).content
    df_list = pd.read_html(html)
    dfs_america.append(df_list[1])
    url_southAmerica = 'https://www.worldometers.info/world-population/south-america-population'
    html = requests.get(url_southAmerica).content
    df_list = pd.read_html(html)
    dfs_america.append(df_list[1])
    url_Caribbean = 'https://www.worldometers.info/world-population/caribbean-population'
    html = requests.get(url_Caribbean).content
    df_list = pd.read_html(html)
    dfs_america.append(df_list[1])
    url_centralAmerica = 'https://www.worldometers.info/world-population/central-america-population'
    html = requests.get(url_centralAmerica).content
    df_list = pd.read_html(html)
    dfs_america.append(df_list[1])
    frame = pd.concat(dfs_america)
    frame.to_csv("regions_population/america_countries.csv")

    dfs_america_regions.append(southAmericaPopulation(url_southAmerica))
    dfs_america_regions.append(caribbeanPopulation(url_Caribbean))
    dfs_america_regions.append(centralAmericaPopulation(url_centralAmerica))
    dfs_america_regions.append(northAmericaPopulation(url_northAmerica))
    frame = pd.concat(dfs_america_regions)
    frame.to_csv("country_population/america_regions.csv")
    print("america done.")

    # ASIA
    dfs_asia = []
    dfs_asia_regions = []
    url_southAsia = 'https://www.worldometers.info/world-population/southern-asia-population'
    html = requests.get(url_southAsia).content
    df_list = pd.read_html(html)
    dfs_asia.append(df_list[1])
    url_eastAsia = 'https://www.worldometers.info/world-population/eastern-asia-population'
    html = requests.get(url_eastAsia).content
    df_list = pd.read_html(html)
    dfs_asia.append(df_list[1])
    url_soutEeastAsia = 'https://www.worldometers.info/world-population/south-eastern-asia-population'
    html = requests.get(url_soutEeastAsia).content
    df_list = pd.read_html(html)
    dfs_asia.append(df_list[1])
    url_westAsia = 'https://www.worldometers.info/world-population/western-asia-population'
    html = requests.get(url_westAsia).content
    df_list = pd.read_html(html)
    dfs_asia.append(df_list[1])
    url_centerAsia = 'https://www.worldometers.info/world-population/central-asia-population'
    html = requests.get(url_centerAsia).content
    df_list = pd.read_html(html)
    dfs_asia.append(df_list[1])
    frame = pd.concat(dfs_asia)
    frame.to_csv("regions_population/asia_countries.csv")

    dfs_asia_regions.append(southAsiaPopulation(url_southAsia))
    dfs_asia_regions.append(eastAsiaPopulation(url_eastAsia))
    dfs_asia_regions.append(southEastAsiaPopulation(url_soutEeastAsia))
    dfs_asia_regions.append(westAsiaPopulation(url_westAsia))
    dfs_asia_regions.append(centerAsiaPopulation(url_centerAsia))
    frame = pd.concat(dfs_asia_regions)
    frame.to_csv("country_population/asia_regions.csv")
    print("asia done.")

    #Africa
    dfs_africa = []
    dfs_africa_regions =[]
    url_westAfrica = 'https://www.worldometers.info/world-population/western-africa-population'
    html = requests.get(url_westAfrica).content
    df_list = pd.read_html(html)
    dfs_africa.append(df_list[1])
    url_eastAfrica = 'https://www.worldometers.info/world-population/eastern-africa-population'
    html = requests.get(url_eastAfrica).content
    df_list = pd.read_html(html)
    dfs_africa.append(df_list[1])
    url_northAfrica = 'https://www.worldometers.info/world-population/northern-africa-population'
    html = requests.get(url_northAfrica).content
    df_list = pd.read_html(html)
    dfs_africa.append(df_list[1])
    url_middleAfrica = 'https://www.worldometers.info/world-population/middle-africa-population'
    html = requests.get(url_middleAfrica).content
    df_list = pd.read_html(html)
    dfs_africa.append(df_list[1])
    url_southAfrica = 'https://www.worldometers.info/world-population/southern-africa-population'
    html = requests.get(url_southAfrica).content
    df_list = pd.read_html(html)
    dfs_africa.append(df_list[1])
    frame = pd.concat(dfs_africa)
    frame.to_csv("regions_population/africa_countries.csv")

    dfs_africa_regions.append(westAfricaPopulation(url_westAfrica))
    dfs_africa_regions.append(eastAfricaPopulation(url_eastAfrica))
    dfs_africa_regions.append(northAfricaPopulation(url_northAfrica))
    dfs_africa_regions.append(middleAfricaPopulation(url_middleAfrica))
    dfs_africa_regions.append(southAfricaPopulation(url_southAfrica))
    frame = pd.concat(dfs_africa_regions)
    frame.to_csv("country_population/africa_regions.csv")
    print("africa done.")

    # Europe
    dfs_europe = []
    dfs_europe_regions = []
    url_westEurope = 'https://www.worldometers.info/world-population/western-europe-population'
    html = requests.get(url_westEurope).content
    df_list = pd.read_html(html)
    dfs_europe.append(df_list[1])
    url_eastEurope = 'https://www.worldometers.info/world-population/eastern-europe-population'
    html = requests.get(url_eastEurope).content
    df_list = pd.read_html(html)
    dfs_europe.append(df_list[1])
    url_northEurope = 'https://www.worldometers.info/world-population/northern-europe-population'
    html = requests.get(url_northEurope).content
    df_list = pd.read_html(html)
    dfs_europe.append(df_list[1])
    url_southEurope = 'https://www.worldometers.info/world-population/southern-europe-population'
    html = requests.get(url_southEurope).content
    df_list = pd.read_html(html)
    dfs_europe.append(df_list[1])
    frame = pd.concat(dfs_europe)
    frame.to_csv("regions_population/europe_countries.csv")

    dfs_europe_regions.append(westEuropePopulation(url_westEurope))
    dfs_europe_regions.append(eastEuropePopulation(url_eastEurope))
    dfs_europe_regions.append(northEuropePopulation(url_northEurope))
    dfs_europe_regions.append(southEuropePopulation(url_southEurope))
    frame = pd.concat(dfs_europe_regions)
    frame.to_csv("country_population/europe_regions.csv")
    print("europe done.")

    # Oceania
    dfs_oceania = []
    dfs_oceania_regions = []
    url_australiaNZ = 'https://www.worldometers.info/world-population/australia-and-new-zealand-population'
    html = requests.get(url_australiaNZ).content
    df_list = pd.read_html(html)
    dfs_oceania.append(df_list[1])
    url_melanesia = 'https://www.worldometers.info/world-population/melanesia-population'
    html = requests.get(url_melanesia).content
    df_list = pd.read_html(html)
    dfs_oceania.append(df_list[1])
    url_polynesia = 'https://www.worldometers.info/world-population/polynesia-population'
    html = requests.get(url_polynesia).content
    df_list = pd.read_html(html)
    dfs_oceania.append(df_list[1])
    url_micronesia = 'https://www.worldometers.info/world-population/micronesia-population'
    html = requests.get(url_micronesia).content
    df_list = pd.read_html(html)
    dfs_oceania.append(df_list[1])
    frame = pd.concat(dfs_oceania)
    frame.to_csv("regions_population/oceania_countries.csv")

    dfs_oceania_regions.append(australiaNZPopulation(url_australiaNZ))
    dfs_oceania_regions.append(melanesiaPopulation(url_melanesia))
    dfs_oceania_regions.append(polynesiaPopulation(url_polynesia))
    dfs_oceania_regions.append(micronesiaPopulation(url_micronesia))
    frame = pd.concat(dfs_oceania_regions)
    frame.to_csv("country_population/oceania_regions.csv")
    print("oceania done.")

