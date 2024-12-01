import requests
from bs4 import BeautifulSoup
import geopy.distance

class ApartmentsDotCom:
    def __init__(self):
        self.headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'cul=en-US; ab=%7b%22e%22%3atrue%2c%22r%22%3a%5b%5d%7d; afe=%7b%22e%22%3afalse%7d; fso=%7b%22e%22%3afalse%7d; _ga=GA1.2.1456612625.1728842487; cb=1; s=; gip=%7b%22Display%22%3a%22UNIVERSITYPARK%2c+PA%22%2c%22GeographyType%22%3a2%2c%22Address%22%3a%7b%22City%22%3a%22UNIVERSITYPARK%22%2c%22CountryCode%22%3a%22US%22%2c%22State%22%3a%22PA%22%7d%2c%22Location%22%3a%7b%22Latitude%22%3a40.8092%2c%22Longitude%22%3a-77.8868%7d%2c%22IsPmcSearchByCityState%22%3afalse%7d; ak_bmsc=66559B5D3964610FD26516DD6E4ED36F~000000000000000000000000000000~YAAQ5op4aG/n1wKTAQAAtnniAhmc42Z+Uk+OHtFxYD4vto5A5KmVHdpnTyjwUMB4hTbSUxRUWa4hITLl4itfTu/02AC5go3e872SA2ns00y/jL1hzHCsxhBnPNu5Mk6oV3Ojv2mGpMeKYiggIqD5aCrv8MCrW4ErvIR7Wa6Yxp/IkpziNTk/KUK/oO1Aeo4E+0idd7WQSVPklv86fEd8j7LIffpXgfjDrRSD3s3Cm/kXQwtAidiZ0XPJ9QnvBTJ+vc5ymc63mKY94O63nw+v4b0P1acpiaxl3HzzGtop2mjtoZ1c9w9hCOBf4AGlcMWpB2wfKQ9rZRHdbw2YIMuyHGaqjJv5wz8sC/AqyJY7G1RAsBrTVMNZ/xetnh2sMzA0WSD/1OSsXsR/xZuBUI0=; _gid=GA1.2.1423610045.1730920217; _gat=1; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Nov+06+2024+14%3A12%3A21+GMT-0500+(Eastern+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f33ac648-192f-4c30-ac42-3eff8da8968f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; akaalb_www_apartments_com_main=1730923941~op=ap_rent_trends_exclusions:www_apartments_com_RESTON|apartments_Prd_Edge_US:www_apartments_com_RESTON|~rv=10~m=www_apartments_com_RESTON:0|~os=0847b47fe1c72dfaedb786f1e8b4b630~id=1338df6f973ff7c47b8c92b381b96850; sr=%7B%22Width%22%3A745%2C%22Height%22%3A310%2C%22PixelRatio%22%3A2%7D; lsc=%7B%22Map%22%3A%7B%22BoundingBox%22%3A%7B%22LowerRight%22%3A%7B%22Latitude%22%3A40.77802%2C%22Longitude%22%3A-77.82072%7D%2C%22UpperLeft%22%3A%7B%22Latitude%22%3A40.80128%2C%22Longitude%22%3A-77.88887%7D%7D%2C%22CountryCode%22%3A%22US%22%7D%2C%22Geography%22%3A%7B%22ID%22%3A%22hw08mc2%22%2C%22Display%22%3A%22State%20College%2C%20PA%22%2C%22GeographyType%22%3A2%2C%22Address%22%3A%7B%22City%22%3A%22State%20College%22%2C%22CountryCode%22%3A%22USA%22%2C%22County%22%3A%22Centre%22%2C%22State%22%3A%22PA%22%2C%22MarketName%22%3A%22State%20College%22%2C%22DMA%22%3A%22Johnstown-Altoona-State%20College%2C%20PA%22%7D%2C%22Location%22%3A%7B%22Latitude%22%3A40.788%2C%22Longitude%22%3A-77.853%7D%2C%22BoundingBox%22%3A%7B%22LowerRight%22%3A%7B%22Latitude%22%3A40.76843%2C%22Longitude%22%3A-77.81893%7D%2C%22UpperLeft%22%3A%7B%22Latitude%22%3A40.80757%2C%22Longitude%22%3A-77.8863%7D%7D%2C%22v%22%3A45799%2C%22IsPmcSearchByCityState%22%3Afalse%7D%2C%22Listing%22%3A%7B%7D%2C%22Paging%22%3A%7B%7D%2C%22IsBoundedSearch%22%3Atrue%2C%22ResultSeed%22%3A354982%2C%22Options%22%3A0%2C%22CountryAbbreviation%22%3A%22US%22%7D; bm_mi=149FDB976AE130473765A322498D0F67~YAAQ5op4aNoZ2AKTAQAAygLlAhli2P93Iu5MQEu5s9UOk5ILuLLk/jpHlLOymHUI987360SYRXAKCgft1bgTYTnLepbsXQpMaRg9PixutOo5ijOlB2Hjg4aAVoaZcyIYGNno0/JFE9H449Bb7ScwAY7Y0ZvRpqndvZ4cuBLHoW2VBRuQ0rZE+zufv9tAXdtXPLx03JPXff5WI81S7OP0YnsU1Xwk/CukJir2WBlk+gZq3dv7vj3DenvrLU6HQxs/mhD7CydGmlmAccAVOHaNbMVrKuezxqCR0/YhoO6NEQNp7PKnL/VQg7xXrJa0GeHKYHadGBXSnLf7aQ==~1; bm_sv=52B13520806E525244F33456A36D46AC~YAAQ5op4aNsZ2AKTAQAAygLlAhkLrzMJM7Esw+qQOF9yr+bAlu0AIA7pfNJsSRENyYnrmKBqNl4d+MATpO+8d7AElFavp3iHxJUg/ItC9/6mSsLxrg2BlF68lBUx3/YvuwDwZV0dbxWtx7BBGF+JSzFb2EE13qSRH8Nx5JsYn6qSZ5eN+A6FrzAMlVUwoZ6qYV0zqoyooM3d7HN7MfgEHuqTGFSrZUcI1nA8lb+TDB03YDCONtsB0kOvYQeNoeWz6g/9tw==~1',
        'priority': 'u=0, i',
        'referer': 'https://www.apartments.com/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }


class ScrapeApartmentsDotCom(ApartmentsDotCom):
    def __init__(self, URL:str):
        super().__init__()
        self.URL = URL
        self.URLs = self.load_url()
    
    def load_url(self):
        if self.URL:
            if 'https://www.apartments.com/' in self.URL:
                search_links = [self.URL+'1/']
                r = requests.get(self.URL, headers=self.headers)
                if r.status_code == 200:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    paging = soup.find('nav', {'id': 'paging'})
                    for a in paging.find_all('a', href=True):
                        search_links.append(a['href'])
                    return search_links
                else:
                    raise ValueError(f'Invalid URL: {self.URL}')
            else:
                raise ValueError(f'Invalid URL: {self.URL}')
        else:
            raise ValueError('URL is empty')

    def __extract_property(self, listing:BeautifulSoup):
        property = {}
        
        if 'data-listingid' in listing.attrs:
            property['property_listing_id'] = listing['data-listingid']
        else:
            property['property_listing_id'] = None

        if 'data-url' in listing.attrs:
            property['property_url'] = listing['data-url']
        else:
            return None

        if 'data-streetaddress' in listing.attrs:
            property['property_street_address'] = listing['data-streetaddress']
        else:
            property['property_street_address'] = None

        if 'data-countrycode' in listing.attrs:
            property['property_country_code'] = listing['data-countrycode']
        else:
            property['property_country_code'] = None

        # Title
        title = listing.find('div', {'class': 'property-title'})
        if title:
            title = title.text.strip()
            property['property_title'] = title
        elif listing.find('p', {'class': 'property-title'}):
            title = listing.find('p', {'class': 'property-title'})
            if title:
                title = title.text.strip()
                property['property_title'] = title
        else:
            title = None
            property['property_title'] = title
        
        # Full Address
        full_address = listing.find('div', {'class': 'property-address'})

        if full_address:
            full_address = full_address.text.strip()
            property['property_full_address'] = full_address
        elif listing.find('p', {'class': 'property-address'}):
            full_address = listing.find('p', {'class': 'property-address'})
            if full_address:
                full_address = full_address.text.strip()
                property['property_full_address'] = full_address
        else:
            if property['property_street_address'] in property['property_title']:
                property['property_full_address'] = property['property_title']
            else:
                full_address = None
                property['property_full_address'] = full_address

        # Property Management
        property_management = listing.find('div', {'class': 'property-logo'})
        if property_management:
            if 'aria-label' in property_management.attrs:
                property_management = property_management['aria-label']
                property['property_management'] = property_management
            else:
                property_management = None
                property['property_management'] = property_management
        elif listing.find('p', {'class': 'property-logo'}):
            property_management = listing.find('p', {'class': 'property-logo'})
            if property_management:
                if 'aria-label' in property_management.attrs:
                    property_management = property_management['aria-label']
                    property['property_management'] = property_management
            else:
                property_management = None
                property['property_management'] = property_management
        else:
            property_management = None
            property['property_management'] = property_management

        # Property Image
        property_image = listing.find('div', {'class': 'carousel-item active us'})
        if property_image:
            if 'style' in property_image.attrs:
                property_image = property_image['style']
                if 'background-image: url(' in property_image:
                    property_image = property_image.split('background-image: url("')[1].split('");')[0]
                property['property_image'] = property_image
        else:
            property_image = None
            property['property_image'] = property_image

        # Property Pricing Range
        pricing_range = listing.find('p', {'class': 'property-pricing'})
        if pricing_range:
            pricing_range = pricing_range.text.strip()
            property['property_pricing_range'] = pricing_range
        elif listing.find('p', {'class': 'property-rents'}):
            pricing_range = listing.find('p', {'class': 'property-rents'})
            if pricing_range:
                pricing_range = pricing_range.text.strip()
                property['property_pricing_range'] = pricing_range
            else:
                pricing_range = None
                property['property_pricing_range'] = pricing_range
        elif listing.find('div', {'class': 'price-range'}):
            pricing_range = listing.find('div', {'class': 'price-range'})
            if pricing_range:
                pricing_range = pricing_range.text.strip()
                property['property_pricing_range'] = pricing_range
        else:
            pricing_range = None
            property['property_pricing_range'] = pricing_range

        # Property Bed Range
        beds = listing.find('p', {'class': 'property-beds'})
        if beds:
            beds = beds.text.strip()
            property['property_bed_range'] = beds
        elif listing.find('div', {'class': 'bed-range'}):
            beds = listing.find('div', {'class': 'bed-range'})
            if beds:
                beds = beds.text.strip()
                property['property_bed_range'] = beds
        else:
            beds = None
            property['property_bed_range'] = beds

        # Property Phone Number
        phone_number = listing.find('a', {'class': 'phone-link'})
        if phone_number:
            phone_number = phone_number.text.strip()
            property['property_phone_number'] = phone_number
        else:
            phone_number = None
            property['property_phone_number'] = phone_number

        # Property Amenities
        amenities = listing.find('p', {'class': 'property-amenities'})
        if amenities:
            amenities = amenities.find_all('span')
        if amenities:
            property['property_amenities'] = [amenity.text.strip() for amenity in amenities]
        else:
            property['property_amenities'] = None

        # Property Type
        property_type = listing.find('div', {'class': 'property-type-for-rent'})
        if property_type:
            property_type = property_type.text.strip()
            property['property_type'] = property_type
        else:
            property_type = None
            property['property_type'] = property_type

        return property
                
    def scrape_properties(self):
        properties = []
        for URL in self.URLs:
            r = requests.get(URL, headers=self.headers)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                listings = soup.find_all('article', {'class': 'placard'})
                for i, listing in enumerate(listings):
                    property = self.__extract_property(listing)
                    properties.append(property)

        return properties
    
    def scrape_property(self, property:dict):
        r = requests.get(property['property_url'], headers=self.headers)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # Phone Number
            phone_number = soup.find('span', {'class': 'phoneNumber'})
            if phone_number:
                phone_number = phone_number.text.strip()
                property['property_phone_number'] = phone_number
            else:
                phone_number = None
                property['property_phone_number'] = phone_number
            
            price_bed_bath_area = soup.find('ul', {'class': 'priceBedRangeInfo'})
            if price_bed_bath_area:
                price_bed_bath_area = price_bed_bath_area.find_all('li')
                for info in price_bed_bath_area:
                    key = "property_"+info.find('p', {'class': 'rentInfoLabel'}).text.lower().replace(' ', '_')
                    value = info.find('p', {'class': 'rentInfoDetail'}).text
                    property[key] = value

            # Property Description
            description = soup.find('section', {'class': 'descriptionSection'})
            if description:
                description = description.find('p')
                if description:
                    description = description.text.strip()
                    property['property_description'] = description
                else:
                    description = None
                    property['property_description'] = description
            else:
                description = None
                property['property_description'] = description
            
            # Apartment Website
            apartment_website = soup.find('section', {'id': 'officeHoursSection'})
            if apartment_website:
                apartment_website = apartment_website.find('div', {'class': 'mortar-wrapper'})

                if apartment_website:
                    apartment_website = apartment_website.find('a')
                    if apartment_website:
                        apartment_website = apartment_website['href']
                        property['property_website'] = apartment_website
                    else:
                        apartment_website = None
                        property['property_website'] = apartment_website
                else:
                    apartment_website = None
                    property['property_website'] = apartment_website
            else:
                apartment_website = None
                property['property_website'] = apartment_website

            # Even More Amenities
            # even_more_amenities = soup.find_all('li', {'class': 'specInfo'})
            # if even_more_amenities:
            #     even_more_amenities = [amenity.text.strip() for amenity in even_more_amenities]
            #     even_more_amenities = '\n'.join(even_more_amenities)
            #     property['property_amenities'] = even_more_amenities
            # else:
            #     property['property_amenities'] = None
            
            # Fees
            fees = ""
            fee = soup.find('div', {'class': 'feespolicies'})
            if fee:
                fee = fee.find_all('li')
                for f in fee:
                    try:
                        key = f.find('div', {'class': 'feeName ellipsis'}).text
                        value = f.find('div', {'class': 'column-right'}).text
                        fees += f"{key}: {value}\n"
                    except:
                        continue
            else:
                fees = None
            property['property_fees'] = fees

            # Latitude and Longitude
            latitude = soup.find('meta', {'property': 'place:location:latitude'})
            longitude = soup.find('meta', {'property': 'place:location:longitude'})

            if latitude:
                latitude = latitude['content']
                property['property_latitude'] = float(latitude)
            else:
                property['property_latitude'] = None

            if longitude:
                longitude = longitude['content']
                property['property_longitude'] = float(longitude)
            else:
                property['property_longitude'] = None

            unit_list = []
            units = soup.find('div', {'data-tab-content-id': 'all'})
            if units:
                units = units.find_all('div', {'class': 'pricingGridItem'})
                for unit in units:

                    unit_rental_key = unit.find('div', {'class': 'priceGridModelWrapper'})
                    if unit_rental_key:
                        unit_rental_key = unit_rental_key['data-rentalkey']
                    else:
                        unit_rental_key = None

                    unit_name = unit.find('span', {'class': 'modelName'})
                    if unit_name:
                        unit_name = unit_name.text.strip()
                    else:
                        unit_name = None

                    rent_label = unit.find('span', {'class': 'rentLabel'})
                    if rent_label:
                        rent_label = rent_label.text.strip()
                        if '\r\n                                        / Person' in rent_label:
                            rent_label = rent_label.replace('\r\n                                        / Person', '')
                        if '–' in rent_label:
                            rent_label = rent_label.split('–')[1].strip()
                    else:
                        rent_label = None

                    floorplan_image = unit.find('div', {'class': 'floorPlanButtonImage'})
                    if floorplan_image:
                        if 'data-background-image' in floorplan_image.attrs:
                            floorplan_image = floorplan_image['data-background-image']
                        else:
                            floorplan_image = None
                    else:
                        floorplan_image = None

                    details = unit.find_all('span', {'class': 'detailsTextWrapper'})
                    details = [detail.text.strip() for detail in details][0]
                    details = details.split('\n')
                    unit_beds = None
                    unit_baths = None
                    unit_sq_ft = None
                    for detail in details:
                        if 'bed' in detail.lower():
                            unit_beds = detail.strip().lower().replace(',','')
                        elif 'bath' in detail.lower():
                            unit_baths = detail.strip().lower().replace(',','')
                        elif 'sq ft' in detail.lower():
                            unit_sq_ft = detail.strip().lower().replace(',','')
                            if ' – ' in unit_sq_ft:
                                unit_sq_ft = unit_sq_ft.split('–')[1]

                    unit_availability = unit.find('div', {'class': 'availability'})

                    if unit_availability:
                        unit_availability = unit_availability.text.strip()
                    else:
                        unit_availability = None
                    
                    unit = {
                        'unit_rental_key': unit_rental_key,
                        'unit_name': unit_name,
                        'unit_rent_label': rent_label,
                        'unit_beds': unit_beds,
                        'unit_baths': unit_baths,
                        'unit_sq_ft': unit_sq_ft,
                        'unit_availability': unit_availability,
                        'unit_floorplan_image': floorplan_image
                    }
                    unit_list.append(unit)
            
            property['units'] = unit_list

            # Distance to campus
            if property['property_latitude'] and property['property_longitude']:
                dist = geopy.distance.distance((40.7964667, -77.8650293), (property['property_latitude'], property['property_longitude'])).miles
                property['distance_to_campus'] = dist
            else:
                property['distance_to_campus'] = None

                      
            return property
        
            
if __name__ == '__main__':
    data = []        
    URL = 'https://www.apartments.com/apartments/state-college-pa/'
    scrape = ScrapeApartmentsDotCom(URL)
    properties = scrape.scrape_properties()
    for property in properties:
        if property:
            property = scrape.scrape_property(property)
            data.append(property)

    import pandas as pd
    final_dataset = []
    for property in data:
        units_df = pd.DataFrame(property['units'])
        units_df['property_listing_id'] = property['property_listing_id']
        if len(units_df) > 0:
            property_df = pd.DataFrame([property])
            rows = units_df.merge(property_df, how='left', on='property_listing_id')
            final_dataset.append(rows)
        else:
            property_df = pd.DataFrame([property])
            final_dataset.append(property_df)

    final_dataset = pd.concat(final_dataset)
    final_dataset = final_dataset.drop(columns=['units'])
    final_dataset['unit_name'] = final_dataset['unit_name'].str.replace(',', '')

    final_dataset.to_csv('prod/data/apartments.csv', index=False, sep=';')