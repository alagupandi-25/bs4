import os
import requests as rq
from pprint import pprint
from bs4 import BeautifulSoup


def check_country(name):
    correct_country = ['United States', 'China', 'Japan','England','Germany', 'India', 'France', 'Italy', 'Canada', 'Brazil', 'Russia', 'South Korea', 'Australia', 'Mexico', 'Spain', 'Indonesia', 'Netherlands', 'Saudi Arabia', 'Turkey', 'Switzerland', 'Taiwan', 'Poland', 'Argentina', 'Belgium', 'Sweden', 'Ireland', 'Thailand', 'Norway', 'Israel', 'Singapore', 'Austria', 'Nigeria', 'United Arab Emirates', 'Vietnam', 'Malaysia', 'Philippines', 'Bangladesh', 'Denmark', 'South Africa', 'Hong Kong', 'Egypt', 'Pakistan', 'Iran', 'Chile', 'Romania', 'Colombia', 'Czech Republic', 'Finland', 'Peru', 'Iraq', 'Portugal', 'New Zealand', 'Kazakhstan', 'Greece', 'Qatar', 'Algeria', 'Hungary', 'Kuwait', 'Ethiopia', 'Ukraine', 'Morocco', 'Slovakia', 'Ecuador', 'Dominican Republic', 'Puerto Rico', 'Kenya', 'Angola', 'Cuba', 'Oman', 'Guatemala', 'Bulgaria', 'Venezuela', 'Uzbekistan', 'Luxembourg', 'Tanzania', 'Turkmenistan', 'Croatia', 'Lithuania', 'Costa Rica', 'Uruguay', 'Panama', 'Ivory Coast', 'Sri Lanka', 'Serbia', 'Belarus', 'Azerbaijan', 'DR Congo', 'Slovenia', 'Ghana', 'Myanmar', 'Jordan', 'Tunisia', 'Uganda', 'Cameroon', 'Latvia', 'Sudan', 'Libya', 'Bolivia', 'Bahrain', 'Paraguay', 'Nepal', 'Estonia', 'Macau', 'El Salvador', 'Honduras', 'Papua New Guinea', 'Senegal', 'Cyprus', 'Cambodia', 'Zimbabwe', 'Zambia', 'Iceland', 'Bosnia and Herzegovina', 'Trinidad and Tobago', 'Georgia', 'Haiti', 'Lebanon', 'Armenia', 'Guinea', 'Burkina Faso', 'Mali', 'Gabon', 'Albania', 'Afghanistan', 'Mozambique', 'Palestine', 'Botswana', 'Yemen', 'Malta', 'Benin', 'Nicaragua', 'Jamaica', 'Mongolia', 'Niger', 'Guyana', 'Brunei', 'Madagascar', 'North Korea', 'Moldova', 'Syria', 'North Macedonia', 'Equatorial Guinea', 'Mauritius', 'Bahamas', 'Laos', 'Namibia', 'Rwanda', 'Congo', 'Tajikistan', 'Kyrgyzstan', 'Chad', 'Malawi', 'Mauritania', 'New Caledonia', 'Kosovo', 'Togo', 'Somalia', 'Monaco', 'Bermuda', 'Montenegro', 'South Sudan', 'Maldives', 'Liechtenstein', 'Barbados', 'French Polynesia', 'Cayman Islands', 'Fiji', 'Eswatini', 'Liberia', 'Djibouti', 'Andorra', 'Aruba', 'Sierra Leone', 'Suriname', 'Burundi', 'Belize', 'Greenland', 'Central African Republic', 'Curaçao', 'Bhutan', 'Eritrea', 'Lesotho', 'Cape Verde', 'Gambia', 'Saint Lucia', 'East Timor', 'Seychelles', 'Guinea-Bissau', 'Antigua and Barbuda', 'San Marino', 'Zanzibar', 'Solomon Islands', 'British Virgin Islands', 'Comoros', 'Grenada', 'Vanuatu', 'Saint Kitts and Nevis', 'Saint Vincent and the Grenadines', 'Turks and Caicos Islands', 'Samoa', 'Sint Maarten', 'Dominica','São Tomé and Príncipe', 'Tonga', 'Micronesia', 'Marshall Islands', 'Cook Islands', 'Palau', 'Anguilla', 'Kiribati', 'Nauru', 'Montserrat', 'Tuvalu']

    for list_string in correct_country:
        if name.lower().strip() == list_string.lower().strip():
          return True
    return False

def deatils_func(country_var):
    request_url = rq.get(f"https://www.britannica.com/place/{country_var}")
    
    if request_url.status_code == 200:  
        soup_object = BeautifulSoup(request_url.text,"html.parser")

        with open(f"{country_var}.txt", "a", encoding="utf-8") as file:

            p_tags = soup_object.find_all('p',class_="topic-paragraph")

            print(f"Writing the details of the {country_var} in {country_var}.txt file")

            file.write("------------------------------------------------Deatils----------------------------\n\n")

            for tags in p_tags:
                para = tags.get_text().strip().split(" ")

                file.write("\n\t")

                for word in range(0,len(para),25):
                    file.write(" ".join(para[word:word+25])+"\n")

            print("Your file located at "+os.path.realpath(file.name))

    else:
        print(" Failed to request the url. Try the again.")
    
def list_func(country_var):
    request_url = rq.get(f"https://www.britannica.com/facts/{country_var}")
    
    if request_url.status_code == 200:  
        soup_object = BeautifulSoup(request_url.text,"html.parser")

        with open(f"{country_var}.txt", "w", encoding="utf-8") as file:

            file.write(f"-------------------------------------------------------------{country_var}-------------------------------------------------------------\n\n")
            
            table_tags = soup_object.find('table',class_="quick-facts-table table font-14")

            file.write("-------------------------------------------------Facts------------------------------\n\n")

            print(f"Writing the Facts of the {country_var} in {country_var}.txt file")

            for tr_tags in table_tags.tbody.find_all('tr'):
                td_tags = tr_tags.find('td')
                th_tags = tr_tags.find('th')
                
                if th_tags is not None:
                   file.write(th_tags.get_text().strip() + "  :  " + td_tags.get_text().strip() + "\n")


    else:
        print("Failed to request the url. Try the again.")
        

if __name__ == "__main__":

    try: 
        while(True): 
            print('\n-----------------------------Country detail -----------------------------------------')
            
            country_var = input("\nEnter the Country name : ")
                
            if check_country(country_var):
                list_func(country_var)
                deatils_func(country_var)

                print("Press ctrl + c to exit.")
                
            else:
                print(f'{country_var} is not listed country. Check spelling')
                continue

    except KeyboardInterrupt:
        
        print('!!FINISH!!')
    
    
    




