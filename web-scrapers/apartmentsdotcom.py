import requests
from bs4 import BeautifulSoup

cookies = {
    'cul': 'en-US',
    'ab': '%7b%22e%22%3atrue%2c%22r%22%3a%5b%5d%7d',
    'afe': '%7b%22e%22%3afalse%7d',
    'fso': '%7b%22e%22%3afalse%7d',
    '_ga': 'GA1.2.1456612625.1728842487',
    'cb': '1',
    'gip': '%7b%22Display%22%3a%22Ashburn%2c+VA%22%2c%22GeographyType%22%3a2%2c%22Address%22%3a%7b%22City%22%3a%22Ashburn%22%2c%22CountryCode%22%3a%22US%22%2c%22State%22%3a%22VA%22%7d%2c%22Location%22%3a%7b%22Latitude%22%3a39.0438%2c%22Longitude%22%3a-77.4879%7d%2c%22IsPmcSearchByCityState%22%3afalse%7d',
    'ak_bmsc': '6173B8FC01C7D345645F895DF40E4B8C~000000000000000000000000000000~YAAQDcgwF+mKq6ySAQAAurJTrxnX8nSPGU0n+VVGe6Zv6KVUBDMgE90Es2fRNACfaNXYiX5j9cpD4RKMxLv3F+eCKUJA4bOdxuihD/KuA+6LFEbTrFyf3KJfhQ8jUduGym5IhUfWu+Ag8Mg4LXJt49M9SnYcVLBwCCbIvxoRomYtPjhHVNCqsP3tUrQvE2btUdhmqsb9O2N+4ad8jBmNG+1l59cmdmInJqAhCM2Glr/aN72qku5UlFqLobAEOpt7iJvPejz3ctW+b9DsUaRNhJ8DPmA4YdELGghzMrWMTueJyfW3uY3kdm7OTEqYPxp2eM8cmKjvoEgx+E8gbgtRzYbXNtUompsTBSILktslv1mET9Pho+oHB7/ETqBIMJJlrS7T57caK8+dhTmnHg==',
    '_gid': 'GA1.2.148414591.1729518351',
    'akaalb_www_apartments_com_main': '1729521953~op=ap_rent_trends_exclusions:www_apartments_com_LAX|apartments_Prd_Edge_US:www_apartments_com_RESTON|~rv=9~m=www_apartments_com_LAX:0|www_apartments_com_RESTON:0|~os=0847b47fe1c72dfaedb786f1e8b4b630~id=956c8fff1231ba73143fb4017f2da59f',
    's': '',
    'sr': '%7B%22Width%22%3A1512%2C%22Height%22%3A328%2C%22PixelRatio%22%3A2%7D',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Oct+21+2024+09%3A47%3A56+GMT-0400+(Eastern+Daylight+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f33ac648-192f-4c30-ac42-3eff8da8968f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false',
    '_gat': '1',
    'lsc': '%7B%22Map%22%3A%7B%22BoundingBox%22%3A%7B%22LowerRight%22%3A%7B%22Latitude%22%3A40.77854%2C%22Longitude%22%3A-77.78379%7D%2C%22UpperLeft%22%3A%7B%22Latitude%22%3A40.80414%2C%22Longitude%22%3A-77.9352%7D%7D%2C%22CountryCode%22%3A%22US%22%7D%2C%22Geography%22%3A%7B%22ID%22%3A%22hw08mc2%22%2C%22Display%22%3A%22State%20College%2C%20PA%22%2C%22GeographyType%22%3A2%2C%22Address%22%3A%7B%22City%22%3A%22State%20College%22%2C%22CountryCode%22%3A%22USA%22%2C%22County%22%3A%22Centre%22%2C%22State%22%3A%22PA%22%2C%22MarketName%22%3A%22State%20College%22%2C%22DMA%22%3A%22Johnstown-Altoona-State%20College%2C%20PA%22%7D%2C%22Location%22%3A%7B%22Latitude%22%3A40.788%2C%22Longitude%22%3A-77.853%7D%2C%22BoundingBox%22%3A%7B%22LowerRight%22%3A%7B%22Latitude%22%3A40.76843%2C%22Longitude%22%3A-77.81893%7D%2C%22UpperLeft%22%3A%7B%22Latitude%22%3A40.80757%2C%22Longitude%22%3A-77.8863%7D%7D%2C%22v%22%3A45799%2C%22IsPmcSearchByCityState%22%3Afalse%7D%2C%22Listing%22%3A%7B%7D%2C%22Paging%22%3A%7B%22Page%22%3A2%2C%22CurrentPageListingKey%22%3A%22hz3twq3%22%7D%2C%22IsBoundedSearch%22%3Atrue%2C%22ResultSeed%22%3A624661%2C%22Options%22%3A0%2C%22CountryAbbreviation%22%3A%22US%22%7D',
    'bm_mi': '35430EA6CB071C8E74CD57D50A537D4E~YAAQDcgwFySJrKySAQAAE79XrxnFH+vmlFs9jczfNon+CfLJrRoLQZjp8+9xcY40HncLfn87w3cj86AlYeA2sSARFniWHXFTKhdxCcbixUiWbjfzv5wpzyNeyj7hfnBOGV4Msz3S/YMlYOj5lP47FksYUF+NAeaOk8q2zMo+fDOPOS8pepHoL0DaoHharSWv7M4DyZP7eRRRXXP58zuEPzVJmO8FUGoR4fXGrq9vuEi1T5epDt+Sva7S6lkr/XxDfHNOu1VLn4qoIhdLttv1X4Y2RmZ/ew74qKaNSj55BAdqhWanW9N2KC9aae/egykDMEwKPUiLfss=~1',
    'bm_sv': 'E3908AF8BD8ECFC9C816BCFA46F8C704~YAAQDcgwFz+JrKySAQAAO79Xrxn2GkXUDPBDBhlq0FIGcd4SODJpOFWyG8CtHbkXTCPveitGWkdv363fqtkqG7emieno0anpwLqFsIq6+KOgUjueyVQbgJYl17JlgZsAa2q0sccs9HKBXvoQUGiiG1ZfNYA/CH2tZ+5xJ4L6EdcD0R3jgxBrU+USZX838HZtKvbYPt8vBXGQvAnYC/nvFyNYJjOwsE+Q2LB9JXT7VoKPX/em7fSksUaoUqAbpyuPdbeeuGQ=~1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'cul=en-US; ab=%7b%22e%22%3atrue%2c%22r%22%3a%5b%5d%7d; afe=%7b%22e%22%3afalse%7d; fso=%7b%22e%22%3afalse%7d; _ga=GA1.2.1456612625.1728842487; cb=1; gip=%7b%22Display%22%3a%22Ashburn%2c+VA%22%2c%22GeographyType%22%3a2%2c%22Address%22%3a%7b%22City%22%3a%22Ashburn%22%2c%22CountryCode%22%3a%22US%22%2c%22State%22%3a%22VA%22%7d%2c%22Location%22%3a%7b%22Latitude%22%3a39.0438%2c%22Longitude%22%3a-77.4879%7d%2c%22IsPmcSearchByCityState%22%3afalse%7d; ak_bmsc=6173B8FC01C7D345645F895DF40E4B8C~000000000000000000000000000000~YAAQDcgwF+mKq6ySAQAAurJTrxnX8nSPGU0n+VVGe6Zv6KVUBDMgE90Es2fRNACfaNXYiX5j9cpD4RKMxLv3F+eCKUJA4bOdxuihD/KuA+6LFEbTrFyf3KJfhQ8jUduGym5IhUfWu+Ag8Mg4LXJt49M9SnYcVLBwCCbIvxoRomYtPjhHVNCqsP3tUrQvE2btUdhmqsb9O2N+4ad8jBmNG+1l59cmdmInJqAhCM2Glr/aN72qku5UlFqLobAEOpt7iJvPejz3ctW+b9DsUaRNhJ8DPmA4YdELGghzMrWMTueJyfW3uY3kdm7OTEqYPxp2eM8cmKjvoEgx+E8gbgtRzYbXNtUompsTBSILktslv1mET9Pho+oHB7/ETqBIMJJlrS7T57caK8+dhTmnHg==; _gid=GA1.2.148414591.1729518351; akaalb_www_apartments_com_main=1729521953~op=ap_rent_trends_exclusions:www_apartments_com_LAX|apartments_Prd_Edge_US:www_apartments_com_RESTON|~rv=9~m=www_apartments_com_LAX:0|www_apartments_com_RESTON:0|~os=0847b47fe1c72dfaedb786f1e8b4b630~id=956c8fff1231ba73143fb4017f2da59f; s=; sr=%7B%22Width%22%3A1512%2C%22Height%22%3A328%2C%22PixelRatio%22%3A2%7D; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Oct+21+2024+09%3A47%3A56+GMT-0400+(Eastern+Daylight+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f33ac648-192f-4c30-ac42-3eff8da8968f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; _gat=1; lsc=%7B%22Map%22%3A%7B%22BoundingBox%22%3A%7B%22LowerRight%22%3A%7B%22Latitude%22%3A40.77854%2C%22Longitude%22%3A-77.78379%7D%2C%22UpperLeft%22%3A%7B%22Latitude%22%3A40.80414%2C%22Longitude%22%3A-77.9352%7D%7D%2C%22CountryCode%22%3A%22US%22%7D%2C%22Geography%22%3A%7B%22ID%22%3A%22hw08mc2%22%2C%22Display%22%3A%22State%20College%2C%20PA%22%2C%22GeographyType%22%3A2%2C%22Address%22%3A%7B%22City%22%3A%22State%20College%22%2C%22CountryCode%22%3A%22USA%22%2C%22County%22%3A%22Centre%22%2C%22State%22%3A%22PA%22%2C%22MarketName%22%3A%22State%20College%22%2C%22DMA%22%3A%22Johnstown-Altoona-State%20College%2C%20PA%22%7D%2C%22Location%22%3A%7B%22Latitude%22%3A40.788%2C%22Longitude%22%3A-77.853%7D%2C%22BoundingBox%22%3A%7B%22LowerRight%22%3A%7B%22Latitude%22%3A40.76843%2C%22Longitude%22%3A-77.81893%7D%2C%22UpperLeft%22%3A%7B%22Latitude%22%3A40.80757%2C%22Longitude%22%3A-77.8863%7D%7D%2C%22v%22%3A45799%2C%22IsPmcSearchByCityState%22%3Afalse%7D%2C%22Listing%22%3A%7B%7D%2C%22Paging%22%3A%7B%22Page%22%3A2%2C%22CurrentPageListingKey%22%3A%22hz3twq3%22%7D%2C%22IsBoundedSearch%22%3Atrue%2C%22ResultSeed%22%3A624661%2C%22Options%22%3A0%2C%22CountryAbbreviation%22%3A%22US%22%7D; bm_mi=35430EA6CB071C8E74CD57D50A537D4E~YAAQDcgwFySJrKySAQAAE79XrxnFH+vmlFs9jczfNon+CfLJrRoLQZjp8+9xcY40HncLfn87w3cj86AlYeA2sSARFniWHXFTKhdxCcbixUiWbjfzv5wpzyNeyj7hfnBOGV4Msz3S/YMlYOj5lP47FksYUF+NAeaOk8q2zMo+fDOPOS8pepHoL0DaoHharSWv7M4DyZP7eRRRXXP58zuEPzVJmO8FUGoR4fXGrq9vuEi1T5epDt+Sva7S6lkr/XxDfHNOu1VLn4qoIhdLttv1X4Y2RmZ/ew74qKaNSj55BAdqhWanW9N2KC9aae/egykDMEwKPUiLfss=~1; bm_sv=E3908AF8BD8ECFC9C816BCFA46F8C704~YAAQDcgwFz+JrKySAQAAO79Xrxn2GkXUDPBDBhlq0FIGcd4SODJpOFWyG8CtHbkXTCPveitGWkdv363fqtkqG7emieno0anpwLqFsIq6+KOgUjueyVQbgJYl17JlgZsAa2q0sccs9HKBXvoQUGiiG1ZfNYA/CH2tZ+5xJ4L6EdcD0R3jgxBrU+USZX838HZtKvbYPt8vBXGQvAnYC/nvFyNYJjOwsE+Q2LB9JXT7VoKPX/em7fSksUaoUqAbpyuPdbeeuGQ=~1',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

response = requests.get('https://www.apartments.com/state-college-pa/', headers=headers)

selector = '#placardContainer > ul'

soup = BeautifulSoup(response.text, 'html.parser')
apartments = soup.select(selector)[0]

properties = []

# Loop through each property article
for article in apartments.find_all('article', class_='placard'):
    # Extract image URL
    image_tag = article.find('img')
    image_url = image_tag['src'] if image_tag else None

    # Extract property name
    property_link = article.find('a', {'aria-label': True})
    property_name = property_link['aria-label'] if property_link else None

    # Extract property pricing
    pricing_tag = article.find('p', class_='property-pricing')
    pricing = pricing_tag.get_text(strip=True) if pricing_tag else None

    # Extract number of beds
    beds_tag = article.find('p', class_='property-beds')
    beds = beds_tag.get_text(strip=True) if beds_tag else None

    # Extract amenities
    amenities = []
    amenities_container = article.find('p', class_='property-amenities')
    if amenities_container:
        amenities = [span.get_text(strip=True) for span in amenities_container.find_all('span')]

    # Extract phone number
    phone_tag = article.find('a', class_='phone-link')
    phone = phone_tag.get_text(strip=True) if phone_tag else None

    # Append property data to the list
    properties.append({
        'image_url': image_url,
        'property_name': property_name,
        'pricing': pricing,
        'beds': beds,
        'amenities': amenities,
        'phone': phone
    })

# Now do transformation

properties_transformed = []

for property in properties:
    property_transformed = {
        'image_url': property['image_url'],
        'property_name': property['property_name'],
        'beds': property['beds'],
        'phone': property['phone']
    }

    for amenity in property['amenities']:
        property_transformed[amenity] = True
    if property['pricing'] is None:
        continue
    else:
        pricing_low = int(property['pricing'].split(' - ')[0].replace('$', '').replace(',', ''))
        pricing_high = int(property['pricing'].split(' - ')[1].replace('$', '').replace(',','')) if property['pricing'] is not None and ' - ' in property['pricing'] else None

    property_transformed['pricing_low'] = pricing_low
    property_transformed['pricing_high'] = pricing_high

    properties_transformed.append(property_transformed)