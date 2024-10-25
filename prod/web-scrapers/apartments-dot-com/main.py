import requests
from requests import Session
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'cul=en-US; ab=%7b%22e%22%3atrue%2c%22r%22%3a%5b%5d%7d; afe=%7b%22e%22%3afalse%7d; fso=%7b%22e%22%3afalse%7d; _ga=GA1.2.1456612625.1728842487; cb=1; s=; ak_bmsc=24DAE93F739D9D7DD45897992ECA157B~000000000000000000000000000000~YAAQbyTDFzTTf5CSAQAAe6+sxRkawWuiiumpu06loTPUIy4MreMsveu9kZT8lBcnjQsILbNWlNlGZipfg4VDqxi/irzywc/7xHYkA+Y2H1rhwDpS+IExSx0HGsfVGcwwE1iOJUHRx2Y7iPBu+sLti+wwf7Iqj+eV/zwqhURCld6N6YbsZcXfCd4zlJvVQHWZI/YhPW9kfujYEjZefWsEE2/zhKJVJ02FedCnJFvtVGmV9AgqPP21XcW6XTyBsNPdvxg8x4rAMB081mI7sTsZ94QMY/gnf8kQ6AI0hX2y87BE0Za3OiwmjIXW4Rbsqxr2HVQe+buxtuOfmYme01FZKXc0IPWqcx4dhi3ODEeK90VBVWeI0p7GhZd3dydn1V9Zx617MgM6DahA5suFOQ==; lsc=%7B%22Map%22%3A%7B%22BoundingBox%22%3A%7B%22LowerRight%22%3A%7B%22Latitude%22%3A40.76843%2C%22Longitude%22%3A-77.81893%7D%2C%22UpperLeft%22%3A%7B%22Latitude%22%3A40.80757%2C%22Longitude%22%3A-77.8863%7D%7D%2C%22CountryCode%22%3A%22US%22%7D%2C%22Geography%22%3A%7B%22ID%22%3A%22hw08mc2%22%2C%22Display%22%3A%22State%20College%2C%20PA%22%2C%22GeographyType%22%3A2%2C%22Address%22%3A%7B%22City%22%3A%22State%20College%22%2C%22CountryCode%22%3A%22USA%22%2C%22County%22%3A%22Centre%22%2C%22State%22%3A%22PA%22%2C%22MarketName%22%3A%22State%20College%22%2C%22DMA%22%3A%22Johnstown-Altoona-State%20College%2C%20PA%22%7D%2C%22Location%22%3A%7B%22Latitude%22%3A40.788%2C%22Longitude%22%3A-77.853%7D%2C%22BoundingBox%22%3A%7B%22LowerRight%22%3A%7B%22Latitude%22%3A40.76843%2C%22Longitude%22%3A-77.81893%7D%2C%22UpperLeft%22%3A%7B%22Latitude%22%3A40.80757%2C%22Longitude%22%3A-77.8863%7D%7D%2C%22v%22%3A45799%2C%22IsPmcSearchByCityState%22%3Afalse%7D%2C%22Listing%22%3A%7B%7D%2C%22Paging%22%3A%7B%7D%2C%22ResultSeed%22%3A259239%2C%22Options%22%3A0%2C%22CountryAbbreviation%22%3A%22US%22%7D; _gid=GA1.2.642542728.1729893283; _gat=1; akaalb_www_apartments_com_main=1729896882~op=ap_rent_trends_exclusions:www_apartments_com_RESTON|apartments_Prd_Edge_US:www_apartments_com_LAX|~rv=29~m=www_apartments_com_RESTON:0|www_apartments_com_LAX:0|~os=0847b47fe1c72dfaedb786f1e8b4b630~id=51478e140e7b2c14832365901b8bde33; bm_mi=529565F7B4D2FBB40DC03A3895A1EC6A~YAAQbyTDFycLgJCSAQAA5RGtxRnqycmdlVuSuvCACsPYapS6BAnxOZMJOQdkf5P5OBiu5ZixpfVSEfY4DWSwEIMqwaG2cWeKQz/Ai8dHGkR4gQBEi1L4dm9IkOetRNpvcnjr+LKu9VK5JsLpL9IMgJcGwki5wl/V/9J1IX554m7p8ZsTR9iROc5xhR59K+dhOqHsWil1FT8B21eQCqRR4G5zjoyl1i/pDOtT2Ghxs8u66dOqMfo5vYpjkg/9+AGI30sYay1nDQUdvvNhB2rEcsnbO3tvCP7sqDD34ldc+W43lavSMOPckR8j88cSiBdipneFc91+AiDC21X+udkRsM+/h8rr1yOnRNdoA/adA7S+m/C8dbhukiObV+tkLUXYvX+o/ANe~1; sr=%7B%22Width%22%3A3824%2C%22Height%22%3A945%2C%22PixelRatio%22%3A1%7D; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+25+2024+17%3A55%3A07+GMT-0400+(Eastern+Daylight+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f33ac648-192f-4c30-ac42-3eff8da8968f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; bm_sv=0ACCAC12DF44C5207ACD40CB7336154C~YAAQbyTDFzQNgJCSAQAAfRWtxRk+pz2gb6awuFVzGOXJhxuBsvGfPSv0jgAWWlC0WHJoU2/JhaL9UpP5uKyjOJexecINHAwHGcAbZuja5hEydsIC0+z43gbFhcb0smbbJ/ce5RERxvTB65FSrfjv/s93KFSvMw8s1U21IOSU9Yoely+DKkYFvmrrpW51jiorTF/2/7JBnME0rc+Gjl4+wNKjbtL5i3ChVDCm/zyWtVyGdHo2nUA8iGwLUnHrnmSoZ+ozZw==~1',
    'origin': 'https://www.apartments.com',
    'priority': 'u=1, i',
    'referer': 'https://www.apartments.com/the-heights-at-state-college-state-college-pa/cy0wffe/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'x-csrf-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3Mjk4OTMzMDYsImV4cCI6MTcyOTk3OTcwNiwiaWF0IjoxNzI5ODkzMzA2LCJpc3MiOiJodHRwczovL3d3dy5hcGFydG1lbnRzLmNvbSIsImF1ZCI6Imh0dHBzOi8vd3d3LmFwYXJ0bWVudHMuY29tIn0.esr245WK4ntvZyC2oyUKlQc0vGGh4SwhBPdn4AXvkG4',
    'x-requested-with': 'XMLHttpRequest',
}

main_page = 'https://www.apartments.com/state-college-pa/1/'

mp = requests.get(main_page, headers=headers)

soup = BeautifulSoup(mp.content, 'html.parser')

pages = soup.find_all('ol')
pages = pages[0].find_all('a')
page_links = [page['href'] for page in pages if 'href' in page.attrs and 'https' in page['href']]

page_links = [main_page] + page_links

def scrape_apartment(apartment):
    try:
        listing_id = apartment.find('article')['data-listingid']
    except (AttributeError, TypeError, KeyError):
        listing_id = None

    try:
        title = apartment.find('span', class_='js-placardTitle').text
    except (AttributeError, TypeError, KeyError):
        title = None

    try:
        address = apartment.find('div', class_='property-address').text
    except (AttributeError, TypeError, KeyError):
        try:
            address = apartment.find('article')['property-streetaddress'] + ', State College, PA 16801'
        except (AttributeError, TypeError, KeyError):
            try:
                address = apartment.find('a', class_='property-link')['aria-label']
            except (AttributeError, TypeError, KeyError):
                address = None

    try:
        web_url = apartment.find('a', class_='property-link')['href']
    except (AttributeError, TypeError, KeyError):
        web_url = None

    try:
        video_url = apartment.find('button', class_='videoPlay')['data-video']
    except (AttributeError, TypeError, KeyError):
        video_url = None

    try:
        virtual_tour_url = apartment.find('button', class_='virtualTour')['data-datasource']
    except (AttributeError, TypeError, KeyError):
        virtual_tour_url = None

    try:
        price = apartment.find('p', class_='property-pricing').text
    except (AttributeError, TypeError, KeyError):
        try:
            price = apartment.find('div', class_='price-range').text
        except (AttributeError, TypeError, KeyError):
            price = None

    try:
        beds = apartment.find('p', class_='property-beds').text
    except (AttributeError, TypeError, KeyError):
        try:
            beds = apartment.find('div', class_='bed-range').text
        except (AttributeError, TypeError, KeyError):
            beds = None

    try:
        amenities = apartment.find('p', class_='property-amenities').text
    except (AttributeError, TypeError, KeyError):
        amenities = None

    try:
        phone = apartment.find('a', class_='phone-link').text
    except (AttributeError, TypeError, KeyError):
        phone = None

    try:
        propertytype = apartment.find('div', class_='property-type-for-rent').text
    except (AttributeError, TypeError, KeyError):
        propertytype = None

    return {
        'listing_id': listing_id,
        'title': title,
        'address': address,
        'web_url': web_url,
        'video_url': video_url,
        'virtual_tour_url': virtual_tour_url,
        'price': price,
        'beds': beds,
        'amenities': amenities,
        'phone': phone,
        'propertytype': propertytype
    }

apartments_scraped = []

for page in page_links:
    print('Scraping page:', page, end='\n')
    mp = requests.get(page, headers=headers)
    soup = BeautifulSoup(mp.content, 'html.parser')
    apartments = soup.find_all('li', class_='mortar-wrapper')
    for apartment in apartments:
        apartments_scraped.append(scrape_apartment(apartment))

def extract_apartment_info(soup):
    property_name = soup.find('h1', class_='propertyName').text.strip() if soup.find('h1', class_='propertyName') else None
    address = ', '.join([span.text.strip() for span in soup.select('.propertyAddressContainer span')])
    phone_number = soup.find('span', class_='phoneNumber').text.strip() if soup.find('span', class_='phoneNumber') else None
    description = soup.find('p', class_='aboutSnippet').text.strip() if soup.find('p', class_='aboutSnippet') else None
    rent_details = [f"{item.find('p', class_='rentInfoLabel').text.strip()}: {item.find('p', class_='rentInfoDetail').text.strip()}" for item in soup.select('.priceBedRangeInfo .column')]
    amenities = [amenity.text.strip() for amenity in soup.select('.unitDetails .amenity')]
    units_info = [{'Unit Name': unit.find('span', class_='modelName').text.strip(),
                   'Rent': unit.find('span', class_='rentLabel').text.strip(),
                   'Details': unit.find('h4', class_='detailsLabel').text.strip()}
                  for unit in soup.find_all('div', class_='priceGridModelWrapper')]
    images = [img['src'] for img in soup.find_all('img') if 'apartments.com' in img['src']]
    
    return {
        "Property Name": property_name,
        "Address": address,
        "Phone Number": phone_number,
        "Description": description,
        "Rent Details": rent_details,
        "Amenities": amenities,
        "Units Information": units_info,
        "Images": images
    }

def extract_apartment_complex_info(soup):
    title = soup.find('title').text.strip()
    property_name = title.split('-')[0].strip()
    address = ', '.join([span.text.strip() for span in soup.select('.propertyAddressContainer span')])
    description = soup.find('meta', attrs={'name': 'description'})['content'].strip() if soup.find('meta', attrs={'name': 'description'}) else None
    latitude = soup.find('meta', property="place:location:latitude")['content'] if soup.find('meta', property="place:location:latitude") else None
    longitude = soup.find('meta', property="place:location:longitude")['content'] if soup.find('meta', property="place:location:longitude") else None
    rent_range = soup.find('div', class_='rentRange').text.strip() if soup.find('div', class_='rentRange') else None
    amenities = [amenity.text.strip() for amenity in soup.select('.amenity')]
    units_info = [{'Unit Name': unit.find('span', class_='modelName').text.strip(),
                   'Rent': unit.find('span', class_='rentLabel').text.strip(),
                   'Details': unit.find('h4', class_='detailsLabel').text.strip()}
                  for unit in soup.find_all('div', class_='priceGridModelWrapper')]
    images = [img['src'] for img in soup.find_all('img') if 'apartments.com' in img['src']]
    
    return {
        "Property Name": property_name,
        "Address": address,
        "Description": description,
        "Latitude": latitude,
        "Longitude": longitude,
        "Rent Range": rent_range,
        "Amenities": amenities,
        "Units Information": units_info,
        "Images": images
    }

def extract_house_info(soup):
    title = soup.find('title').text.strip()
    property_name = title.split('-')[0].strip()
    address = ', '.join([span.text.strip() for span in soup.select('.propertyAddressContainer span')])
    rent = soup.find('span', class_='rent').text.strip() if soup.find('span', class_='rent') else None
    bedrooms = soup.find('span', class_='bedrooms').text.strip() if soup.find('span', class_='bedrooms') else None
    bathrooms = soup.find('span', class_='bathrooms').text.strip() if soup.find('span', class_='bathrooms') else None
    description = soup.find('meta', attrs={'name': 'description'})['content'].strip() if soup.find('meta', attrs={'name': 'description'}) else None
    latitude = soup.find('meta', property="place:location:latitude")['content'] if soup.find('meta', property="place:location:latitude") else None
    longitude = soup.find('meta', property="place:location:longitude")['content'] if soup.find('meta', property="place:location:longitude") else None
    images = [img['src'] for img in soup.find_all('img') if 'apartments.com' in img['src']]
    
    return {
        "Property Name": property_name,
        "Address": address,
        "Rent": rent,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Description": description,
        "Latitude": latitude,
        "Longitude": longitude,
        "Images": images
    }

def extract_townhouse_info(soup):
    title = soup.find('title').text.strip()
    property_name = title.split('-')[0].strip()
    address = ', '.join([span.text.strip() for span in soup.select('.propertyAddressContainer span')])
    rent = soup.find('span', class_='rent').text.strip() if soup.find('span', class_='rent') else None
    bedrooms = soup.find('span', class_='bedrooms').text.strip() if soup.find('span', class_='bedrooms') else None
    bathrooms = soup.find('span', class_='bathrooms').text.strip() if soup.find('span', class_='bathrooms') else None
    description = soup.find('meta', attrs={'name': 'description'})['content'].strip() if soup.find('meta', attrs={'name': 'description'}) else None
    amenities = [amenity.text.strip() for amenity in soup.select('.amenity')]
    latitude = soup.find('meta', property="place:location:latitude")['content'] if soup.find('meta', property="place:location:latitude") else None
    longitude = soup.find('meta', property="place:location:longitude")['content'] if soup.find('meta', property="place:location:longitude") else None
    images = [img['src'] for img in soup.find_all('img') if 'apartments.com' in img['src']]
    
    return {
        "Property Name": property_name,
        "Address": address,
        "Rent": rent,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Description": description,
        "Amenities": amenities,
        "Latitude": latitude,
        "Longitude": longitude,
        "Images": images
    }

for apartment in apartments_scraped:
    print('Scraping apartment:', apartment['web_url'], end='\n')
    mp = requests.get(apartment['web_url'], headers=headers)
    soup = BeautifulSoup(mp.content, 'html.parser')
    try:
        new_apartment_info = extract_apartment_info(soup)
    except:
        try:
            new_apartment_info = extract_apartment_complex_info(soup)
        except:
            try:
                new_apartment_info = extract_house_info(soup)
            except:
                new_apartment_info = extract_townhouse_info(soup)
    apartment.update(new_apartment_info)

df = pd.DataFrame(apartments_scraped)
df.to_csv('prod/data/apartmentsdotcom.csv', index=False)    



