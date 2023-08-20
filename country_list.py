import requests
import bs4

def flat(lis):
    flatList = []
  
    for element in lis:
        if type(element) is list:
            for item in element:
                flatList.append(item)   
        else:
            flatList.append(element)
            
    return flatList

list_country = []

request =requests.get("https://www.scrapingbee.com/documentation/country_codes/")
soup = bs4.BeautifulSoup(request.text,'html.parser')
info_table = soup.find('table')

for tr_tags in info_table.tbody.find_all('tr'):

    list_country.append(str(tr_tags.contents[0].string))

country = flat(list_country)
print(country)
    
li=[['United States'], ['China'], ['Japan'], ['Germany'], ['India'], ['United Kingdom'], ['France'],['Italy'], ['Canada'], ['Brazil'], ['Russia'], ['South Korea'], ['Australia'], ['Mexico'], ['Spain'], ['Indonesia'],['Netherlands'], ['Saudi Arabia'], ['Turkey'], ['Switzerland'], ['Taiwan'], ['Poland'], ['Argentina'], ['Belgium'],['Sweden'], ['Ireland'], ['Thailand'], ['Norway'], ['Israel'], ['Singapore'], ['Austria'], ['Nigeria'], ['United Arab Emirates'],['Vietnam'], ['Malaysia'], ['Philippines'], ['Bangladesh'], ['Denmark'], ['South Africa'], ['Hong Kong'], ['Egypt'], ['Pakistan'], ['Iran'], ['Chile'], ['Romania'], ['Colombia'], ['Czech Republic'], ['Finland'], ['Peru'], ['Iraq'], ['Portugal'], ['New Zealand'], ['Kazakhstan'], ['Greece'], ['Qatar'], ['Algeria'], ['Hungary'], ['Kuwait'], ['Ethiopia'], ['Ukraine'], ['Morocco'], ['Slovakia'], ['Ecuador'], ['Dominican Republic'], ['Puerto Rico'], ['Kenya'], ['Angola'], ['Cuba'], ['Oman'], ['Guatemala'], ['Bulgaria'], ['Venezuela'], ['Uzbekistan'], ['Luxembourg'], ['Tanzania'], ['Turkmenistan'], ['Croatia'], ['Lithuania'], ['Costa Rica'], ['Uruguay'], ['Panama'], ['Ivory Coast'], ['Sri Lanka'], ['Serbia'], ['Belarus'], ['Azerbaijan'], ['DR Congo'], ['Slovenia'], ['Ghana'], ['Myanmar'], ['Jordan'], ['Tunisia'], ['Uganda'], ['Cameroon'], ['Latvia'], ['Sudan'], ['Libya'], ['Bolivia'], ['Bahrain'], ['Paraguay'], ['Nepal'], ['Estonia'], ['Macau'], ['El Salvador'], ['Honduras'], ['Papua New Guinea'], ['Senegal'], ['Cyprus'], ['Cambodia'], ['Zimbabwe'], ['Zambia'], ['Iceland'], ['Bosnia and Herzegovina'], ['Trinidad and Tobago'], ['Georgia'], ['Haiti'], ['Lebanon'], ['Armenia'], ['Guinea'], ['Burkina Faso'], ['Mali'], ['Gabon'], ['Albania'], ['Afghanistan'], ['Mozambique'], ['Palestine'], ['Botswana'], ['Yemen'], ['Malta'], ['Benin'], ['Nicaragua'], ['Jamaica'], ['Mongolia'], ['Niger'], ['Guyana'], ['Brunei'], ['Madagascar'], ['North Korea'], ['Moldova'], ['Syria'], ['North Macedonia'], ['Equatorial Guinea'], ['Mauritius'], ['Bahamas'], ['Laos'], ['Namibia'], ['Rwanda'], ['Congo'], ['Tajikistan'], ['Kyrgyzstan'], ['Chad'], ['Malawi'], ['Mauritania'], ['New Caledonia'], ['Kosovo'], ['Togo'], ['Somalia'], ['Monaco'], ['Bermuda'], ['Montenegro'], ['South Sudan'], ['Maldives'], ['Liechtenstein'], ['Barbados'], ['French Polynesia'], ['Cayman Islands'], ['Fiji'], ['Eswatini'], ['Liberia'], ['Djibouti'], ['Andorra'], ['Aruba'], ['Sierra Leone'], ['Suriname'], ['Burundi'], ['Belize'], ['Greenland'], ['Central African Republic'], ['Curaçao'], ['Bhutan'], ['Eritrea'], ['Lesotho'], ['Cape Verde'], ['Gambia'], ['Saint Lucia'], ['East Timor'], ['Seychelles'], ['Guinea-Bissau'], ['Antigua and Barbuda'], ['San Marino'], ['Zanzibar'], ['Solomon Islands'], ['British Virgin Islands'], ['Comoros'], ['Grenada'], ['Vanuatu'], ['Saint Kitts and Nevis'], ['Saint Vincent and the Grenadines'], ['Turks and Caicos Islands'], ['Samoa'], ['Sint Maarten'], ['Dominica'], ['São Tomé and Príncipe'], ['Tonga'], ['Micronesia'],['Marshall Islands'], ['Cook Islands'], ['Palau'], ['Anguilla'], ['Kiribati'], ['Nauru'], ['Montserrat'], ['Tuvalu']]


    
